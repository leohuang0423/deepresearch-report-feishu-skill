import puppeteer from 'puppeteer';
import path from 'node:path'; import { fileURLToPath, pathToFileURL } from 'node:url'; import { mkdir } from 'node:fs/promises';
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const scene = path.resolve(__dirname, 'scenes/xhs-cat-litter-mat.html');
const times = (process.argv[2]||'4,14,26,40,58,86,112,140,152').split(',').map(Number);
const fps=24; const outDir=path.resolve(__dirname,'.preview'); await mkdir(outDir,{recursive:true});
const b=await puppeteer.launch({headless:'new',args:['--no-sandbox','--disable-setuid-sandbox','--disable-dev-shm-usage','--force-color-profile=srgb','--hide-scrollbars','--disable-gpu']});
const p=await b.newPage(); await p.setViewport({width:1080,height:1440,deviceScaleFactor:1});
await p.goto(pathToFileURL(scene).href,{waitUntil:'networkidle0'});
await p.evaluate(async()=>{if(document.fonts&&document.fonts.ready)await document.fonts.ready;});
const dur=await p.evaluate(()=>window.__SCENE__.duration); console.log('duration',dur,'s');
for(const tm of times){const f=Math.round(tm*fps);await p.evaluate((fr,fp)=>window.seek(fr,fp),f,fps);
  await p.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
  const o=path.join(outDir,'t'+String(tm).replace('.','_')+'.jpg');await p.screenshot({path:o,type:'jpeg',quality:90});console.log('saved',path.basename(o));}
await b.close();
