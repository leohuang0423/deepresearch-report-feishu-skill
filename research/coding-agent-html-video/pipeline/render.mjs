#!/usr/bin/env node
/**
 * Deterministic HTML -> MP4 renderer.
 *
 * The scene is a normal HTML file that drives ALL of its animation from a single
 * function `window.seek(frame, fps)` (no wall-clock time, no requestAnimationFrame
 * easing against real time). The harness steps the frame index from 0..N, takes a
 * pixel-exact screenshot of each frame, then encodes the frames with ffmpeg.
 *
 * Because every frame is a pure function of its index, renders are 100% reproducible
 * and you can re-render any single frame, change one number, and diff the output -
 * the core controllability advantage over image/text-to-video models.
 *
 * Usage:
 *   node render.mjs --scene scenes/ecommerce-ad.html --out ../output/ad.mp4 \
 *        --width 1080 --height 1920 --fps 30 --duration 15
 */
import { mkdir, rm, readdir } from 'node:fs/promises';
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
  const a = { width: 1080, height: 1920, fps: 30, duration: null, scene: 'scenes/ecommerce-ad.html',
              out: '../output/out.mp4', crf: 18, keepFrames: false, scale: 1 };
  for (let i = 2; i < argv.length; i++) {
    const k = argv[i].replace(/^--/, '');
    const v = argv[i + 1];
    if (k === 'keepFrames') { a.keepFrames = true; continue; }
    a[k] = v; i++;
  }
  a.width = +a.width; a.height = +a.height; a.fps = +a.fps; a.crf = +a.crf; a.scale = +a.scale;
  if (a.duration != null) a.duration = +a.duration;
  return a;
}

const pad = (n, w = 5) => String(n).padStart(w, '0');

async function main() {
  const args = parseArgs(process.argv);
  const scenePath = path.resolve(__dirname, args.scene);
  const outPath = path.resolve(__dirname, args.out);
  const framesDir = path.resolve(__dirname, '.frames');
  if (!existsSync(scenePath)) throw new Error(`Scene not found: ${scenePath}`);

  await rm(framesDir, { recursive: true, force: true });
  await mkdir(framesDir, { recursive: true });
  await mkdir(path.dirname(outPath), { recursive: true });

  console.log(`[render] scene=${path.relative(process.cwd(), scenePath)}`);
  console.log(`[render] ${args.width}x${args.height} @ ${args.fps}fps  scale=${args.scale}`);

  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage',
           '--force-color-profile=srgb', '--hide-scrollbars', '--disable-gpu'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: args.width, height: args.height, deviceScaleFactor: args.scale });
  await page.goto(pathToFileURL(scenePath).href, { waitUntil: 'networkidle0' });
  await page.evaluate(async () => { if (document.fonts && document.fonts.ready) await document.fonts.ready; });

  // Scene can declare its own duration via window.__SCENE__.duration (seconds).
  const sceneCfg = await page.evaluate(() => (window.__SCENE__ || {}));
  const duration = args.duration ?? sceneCfg.duration ?? 10;
  const total = Math.round(duration * args.fps);
  console.log(`[render] duration=${duration}s -> ${total} frames`);

  const t0 = Date.now();
  for (let f = 0; f < total; f++) {
    await page.evaluate((frame, fps) => {
      if (typeof window.seek === 'function') window.seek(frame, fps);
    }, f, args.fps);
    // Let layout/paint settle deterministically (two rAFs), without advancing time-based anim.
    await page.evaluate(() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))));
    await page.screenshot({ path: path.join(framesDir, `frame-${pad(f)}.png`), captureBeyondViewport: false });
    if (f % args.fps === 0 || f === total - 1) {
      const pct = (((f + 1) / total) * 100).toFixed(0);
      process.stdout.write(`\r[render] frames ${f + 1}/${total} (${pct}%)   `);
    }
  }
  process.stdout.write('\n');
  await browser.close();
  console.log(`[render] capture done in ${((Date.now() - t0) / 1000).toFixed(1)}s`);

  // Encode H.264 mp4 (yuv420p for universal playback, +faststart for web/ad platforms).
  const inPattern = path.join(framesDir, 'frame-%05d.png');
  const ffArgs = [
    '-y', '-framerate', String(args.fps), '-i', inPattern,
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', String(args.crf),
    '-preset', 'slow', '-movflags', '+faststart',
    '-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2', outPath,
  ];
  console.log(`[ffmpeg] encoding -> ${path.relative(process.cwd(), outPath)}`);
  await execFileP(ffmpegPath, ffArgs);

  // Poster frame (representative still) for thumbnails / ad library covers.
  const poster = outPath.replace(/\.mp4$/, '-poster.jpg');
  const posterFrame = Math.min(total - 1, Math.round(total * 0.35));
  await execFileP(ffmpegPath, ['-y', '-i', path.join(framesDir, `frame-${pad(posterFrame)}.png`),
    '-q:v', '3', poster]);

  if (!args.keepFrames) await rm(framesDir, { recursive: true, force: true });

  const { stdout } = await execFileP(ffmpegPath, ['-i', outPath], { encoding: 'utf8' }).catch(e => ({ stdout: e.stderr || '' }));
  console.log(`[done] ${path.relative(process.cwd(), outPath)}`);
  console.log(`[done] poster ${path.relative(process.cwd(), poster)}`);
  const m = /Duration: ([0-9:.]+).*?(\d+x\d+).*?(\d+(?:\.\d+)?) fps/s.exec(stdout);
  if (m) console.log(`[done] ${m[1]} ${m[2]} ${m[3]}fps`);
}

main().catch(e => { console.error('\n[render] FAILED:', e); process.exit(1); });
