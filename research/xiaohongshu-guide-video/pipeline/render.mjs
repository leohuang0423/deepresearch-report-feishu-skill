#!/usr/bin/env node
/**
 * Deterministic HTML -> MP4 renderer with parallel workers (for long-form video).
 *
 * Same contract as the ad pipeline: the scene drives all animation from
 * window.seek(frame, fps). Here we shard the frame range across N headless
 * Chromium instances to use all CPU cores, write JPEG frames, then encode.
 *
 *   node render.mjs --scene scenes/x.html --out ../output/x.mp4 \
 *        --width 1080 --height 1440 --fps 24 --workers 4 --jpeg
 */
import { mkdir, rm } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import puppeteer from 'puppeteer';
import ffmpegPath from 'ffmpeg-static';

const execFileP = promisify(execFile);
const __dirname = path.dirname(fileURLToPath(import.meta.url));

function parseArgs(argv) {
  const a = { width: 1080, height: 1440, fps: 24, duration: null, workers: 4, crf: 19,
    jpeg: false, quality: 92, scene: 'scenes/xhs-cat-litter-mat.html', out: '../output/out.mp4',
    music: '', keepFrames: false };
  for (let i = 2; i < argv.length; i++) {
    const k = argv[i].replace(/^--/, '');
    if (k === 'jpeg' || k === 'keepFrames') { a[k] = true; continue; }
    a[k] = argv[++i];
  }
  for (const n of ['width','height','fps','workers','crf','quality']) a[n] = +a[n];
  if (a.duration != null) a.duration = +a.duration;
  return a;
}
const pad = (n, w = 5) => String(n).padStart(w, '0');

async function makePage(browser, args, sceneUrl) {
  const page = await browser.newPage();
  await page.setViewport({ width: args.width, height: args.height, deviceScaleFactor: 1 });
  await page.goto(sceneUrl, { waitUntil: 'networkidle0' });
  await page.evaluate(async () => { if (document.fonts && document.fonts.ready) await document.fonts.ready; });
  return page;
}

async function main() {
  const args = parseArgs(process.argv);
  const scenePath = path.resolve(__dirname, args.scene);
  const outPath = path.resolve(__dirname, args.out);
  const framesDir = path.resolve(__dirname, '.frames');
  const sceneUrl = pathToFileURL(scenePath).href;
  if (!existsSync(scenePath)) throw new Error(`Scene not found: ${scenePath}`);

  await rm(framesDir, { recursive: true, force: true });
  await mkdir(framesDir, { recursive: true });
  await mkdir(path.dirname(outPath), { recursive: true });

  // probe duration
  const probe = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox','--disable-setuid-sandbox','--disable-dev-shm-usage','--disable-gpu'] });
  const pp = await makePage(probe, args, sceneUrl);
  const cfg = await pp.evaluate(() => (window.__SCENE__ || {}));
  await probe.close();
  const duration = args.duration ?? cfg.duration ?? 10;
  const total = Math.round(duration * args.fps);
  const ext = args.jpeg ? 'jpg' : 'png';
  console.log(`[render] ${path.basename(scenePath)}  ${args.width}x${args.height}@${args.fps}fps  ${duration}s -> ${total} frames  workers=${args.workers} fmt=${ext}`);

  const t0 = Date.now();
  let done = 0;
  const launchArgs = ['--no-sandbox','--disable-setuid-sandbox','--disable-dev-shm-usage','--force-color-profile=srgb','--hide-scrollbars','--disable-gpu'];

  async function worker(id) {
    const browser = await puppeteer.launch({ headless: 'new', args: launchArgs });
    const page = await makePage(browser, args, sceneUrl);
    for (let f = id; f < total; f += args.workers) {
      await page.evaluate((frame, fps) => { if (typeof window.seek === 'function') window.seek(frame, fps); }, f, args.fps);
      await page.evaluate(() => new Promise(r => requestAnimationFrame(r)));
      const file = path.join(framesDir, `frame-${pad(f)}.${ext}`);
      if (args.jpeg) await page.screenshot({ path: file, type: 'jpeg', quality: args.quality, captureBeyondViewport: false });
      else await page.screenshot({ path: file, captureBeyondViewport: false });
      done++;
      if (done % 24 === 0 || done === total) {
        const pct = ((done / total) * 100).toFixed(0);
        const rate = done / ((Date.now() - t0) / 1000);
        process.stdout.write(`\r[render] ${done}/${total} (${pct}%)  ${rate.toFixed(1)} fps  `);
      }
    }
    await browser.close();
  }
  await Promise.all(Array.from({ length: args.workers }, (_, i) => worker(i)));
  process.stdout.write('\n');
  console.log(`[render] capture done in ${((Date.now() - t0) / 1000).toFixed(1)}s`);

  // encode
  const inPattern = path.join(framesDir, `frame-%05d.${ext}`);
  const ffArgs = ['-y','-framerate', String(args.fps), '-i', inPattern];
  let hasAudio = false;
  if (args.music && existsSync(path.resolve(__dirname, args.music))) {
    ffArgs.push('-i', path.resolve(__dirname, args.music)); hasAudio = true;
  }
  ffArgs.push('-c:v','libx264','-pix_fmt','yuv420p','-crf', String(args.crf),'-preset','medium',
    '-vf','scale=trunc(iw/2)*2:trunc(ih/2)*2','-movflags','+faststart');
  if (hasAudio) ffArgs.push('-c:a','aac','-b:a','160k','-shortest');
  ffArgs.push(outPath);
  console.log(`[ffmpeg] encoding -> ${path.relative(process.cwd(), outPath)}${hasAudio ? ' (+audio)' : ''}`);
  await execFileP(ffmpegPath, ffArgs, { maxBuffer: 1 << 26 });

  const poster = outPath.replace(/\.mp4$/, '-poster.jpg');
  const pf = Math.min(total - 1, Math.round(total * 0.06));
  await execFileP(ffmpegPath, ['-y','-i', path.join(framesDir, `frame-${pad(pf)}.${ext}`), '-q:v','3', poster]);

  if (!args.keepFrames) await rm(framesDir, { recursive: true, force: true });
  const info = await execFileP(ffmpegPath, ['-i', outPath], { encoding: 'utf8' }).catch(e => ({ stderr: e.stderr || '' }));
  const m = /Duration: ([0-9:.]+).*?, (\d+x\d+).*?, (\d+(?:\.\d+)?) fps/s.exec(info.stderr || '');
  console.log(`[done] ${path.relative(process.cwd(), outPath)}  ${m ? m[1]+' '+m[2]+' '+m[3]+'fps' : ''}`);
}
main().catch(e => { console.error('\n[render] FAILED:', e); process.exit(1); });
