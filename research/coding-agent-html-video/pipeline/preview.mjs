import puppeteer from 'puppeteer';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { mkdir } from 'node:fs/promises';
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const scene = path.resolve(__dirname, process.argv[2] || 'scenes/ecommerce-ad.html');
const times = (process.argv[3] || '1.2,3.6,6.2,9.8,11.9,14.2').split(',').map(Number);
const fps = 30;
const outDir = path.resolve(__dirname, '.preview');
await mkdir(outDir, { recursive: true });
const b = await puppeteer.launch({ headless:'new', args:['--no-sandbox','--disable-setuid-sandbox','--disable-dev-shm-usage','--force-color-profile=srgb','--hide-scrollbars','--disable-gpu'] });
const p = await b.newPage();
await p.setViewport({ width:1080, height:1920, deviceScaleFactor:1 });
await p.goto(pathToFileURL(scene).href, { waitUntil:'networkidle0' });
await p.evaluate(async()=>{ if(document.fonts&&document.fonts.ready) await document.fonts.ready; });
for (const tm of times) {
  const f = Math.round(tm*fps);
  await p.evaluate((fr,fp)=>window.seek(fr,fp), f, fps);
  await p.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
  const out = path.join(outDir, `t${String(tm).replace('.','_')}.png`);
  await p.screenshot({ path: out });
  console.log('saved', path.relative(process.cwd(), out));
}
await b.close();
