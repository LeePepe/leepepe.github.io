/* Run: node scripts/test_vault_browser.mjs --output /absolute/handoff/receipts/browser-r2 */
import assert from 'node:assert/strict';
import {readFile, writeFile, mkdir} from 'node:fs/promises';
import {createServer} from 'node:http';
import {resolve, extname, dirname} from 'node:path';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';
const {chromium} = await import(process.env.PLAYWRIGHT_MODULE || '/tmp/tia-pw/node_modules/playwright/index.mjs');
const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const outputArg = process.argv.indexOf('--output');
const output = outputArg >= 0 ? resolve(process.argv[outputArg + 1]) : null;
if (output && (output === root || output.startsWith(root + '/'))) throw new Error('Browser evidence must stay outside the published repository');
if (output) await mkdir(output, {recursive:true});
const checks = [], contrasts = [], errors = [], storageEvidence = [], geometryEvidence = [];
const check = async (name, fn) => {try {await fn(); checks.push({name,status:'PASS'});} catch (e) {checks.push({name,status:'FAIL',reason:e.stack}); console.error('FAIL',name,e.message);}};
const server = createServer(async (req,res) => {
  try {const path = resolve(root, '.' + decodeURIComponent(new URL(req.url,'http://local').pathname)); if (!path.startsWith(root + '/')) throw Error('path'); const file = new URL(req.url,'http://local').pathname.endsWith('/') ? resolve(path,'index.html') : path; const data = await readFile(file); res.setHeader('Content-Type', ({'.html':'text/html','.css':'text/css','.js':'text/javascript','.json':'application/json','.svg':'image/svg+xml'})[extname(file)] || 'application/octet-stream');res.end(data);} catch {res.writeHead(404);res.end('Not found');}
});
await new Promise(r => server.listen(0,'127.0.0.1',r));
const base = `http://127.0.0.1:${server.address().port}`;
let browser;
const deadline = setTimeout(() => {console.error('Browser gate exceeded 300-second bound'); process.exitCode = 1; browser?.close();},300000);
deadline.unref();
const evidence = async (name,value) => {if (output) await writeFile(resolve(output,name),JSON.stringify(value,null,2));};
const visibleRows = list => list.locator('li:visible').allTextContents();
async function dragMouse(page,node,fraction) {
  await node.scrollIntoViewIfNeeded(); const r = await node.boundingBox();
  await page.mouse.move(r.x+r.width/2,r.y+r.height/2); await page.mouse.down();
  const track = await node.locator('..').boundingBox();
  await page.mouse.move(track.x+22+(track.width-44)*fraction,r.y+r.height/2,{steps:12});
  await page.mouse.up();
}
async function screenshot(page,name,locator) {if (output) {await locator?.scrollIntoViewIfNeeded(); await (locator || page).screenshot({path:resolve(output,name),animations:'disabled'});}}
async function contrastRead(specimen) {
  return specimen.evaluate(el => {
    const rgb = s => s.match(/[\d.]+/g).map(Number);
    const luminance = c => {const a = c.slice(0,3).map(v => {v/=255;return v<=.04045?v/12.92:((v+.055)/1.055)**2.4;});return a[0]*.2126+a[1]*.7152+a[2]*.0722;};
    const ratio = (a,b) => {const values=[luminance(a),luminance(b)].sort((x,y)=>x-y);return (values[1]+.05)/(values[0]+.05);};
    const nodes = [...el.querySelectorAll('*')].filter(n => [...n.childNodes].some(c => c.nodeType === 3 && c.textContent.trim()));
    return nodes.map(n => {let p=n,bg;while(p) {const candidate=getComputedStyle(p).backgroundColor; if (rgb(candidate)[3] !== 0) {bg=candidate;break;} p=p.parentElement;} const fg=getComputedStyle(n).color;return {text:n.textContent.trim(),foreground:fg,background:bg,ratio:ratio(rgb(fg),rgb(bg))};});
  });
}
async function geometry(page,name) {
  const data = await page.evaluate(() => {
    const rectangle = node => {const r=node.getBoundingClientRect();return {x:r.x,y:r.y+scrollY,width:r.width,height:r.height};};
    const hits = [], visuals = [];
    function walk(node) {
      const style=getComputedStyle(node), r=node.getBoundingClientRect();
      if (!r.width || !r.height || style.display==='none' || style.visibility==='hidden') return null;
      const checkbox=node.matches('input[type=checkbox]');
      const interactive=node.matches('button,select,input:not([type=checkbox]),summary') || node.matches('label:has(input[type=checkbox])');
      const children=[...node.children].map(walk).filter(Boolean);
      const structural=children.some(c => c.interactive || c.children.length) || node.matches('.vault-live-stage,.vault-mini-specimen,.vault-controls');
      const value={tag:node.tagName,class:node.className,text:interactive?node.textContent.trim().slice(0,100):'',interactive,children};
      if (interactive || structural) value.frame=rectangle(node);
      else if (!checkbox) visuals.push({tag:node.tagName,class:node.className,frame:rectangle(node)});
      if (interactive) hits.push({text:value.text,frame:value.frame});
      return value;
    }
    // Independent stage/control roots follow their own actual descendant containment.
    const children=[...document.querySelectorAll('.vault-live-stage,.vault-mini-specimen,.vault-controls')].filter(n=>!n.hidden&&n.closest('.vault-card')?.hidden!==true).map(walk).filter(Boolean);
    return {viewportWidth:innerWidth,children,hits,noninteractiveVisuals:visuals,scrollWidth:document.documentElement.scrollWidth};
  });
  geometryEvidence.push({name,hits:data.hits.length,scrollWidth:data.scrollWidth});
  await evidence(name,data);
  const small = data.hits.filter(h => h.frame.width<43.99 || h.frame.height<43.99);
  assert.deepEqual(small,[],'44px hit targets');
  assert.ok(data.scrollWidth<=page.viewportSize().width,'no page overflow');
  const overflow=data.hits.filter(h=>h.frame.x<-.01||h.frame.x+h.frame.width>page.viewportSize().width+.01);
  assert.deepEqual(overflow,[],'hit regions remain in viewport');
  // Verify real hit centers, not just dimensions or an invented geometry hierarchy.
  const occluded=await page.evaluate(() => {
    const bad=[];
    for (const stage of document.querySelectorAll('.vault-live-stage')) {
      if (stage.closest('.vault-card').hidden) continue;
      for (const node of stage.querySelectorAll('button,select,input:not([type=checkbox]),label:has(input[type=checkbox])')) {
        const r=node.getBoundingClientRect(); if (!r.width||!r.height) continue;
        const s=stage.getBoundingClientRect();
        if (r.top<s.top-.1||r.bottom>s.bottom+.1||r.left<s.left-.1||r.right>s.right+.1) bad.push({id:stage.dataset.stageId,text:node.textContent,reason:'outside stage',frame:{x:r.x,y:r.y,width:r.width,height:r.height}});
        node.scrollIntoView({block:'center',behavior:'instant'});
        const visible=node.getBoundingClientRect(), hit=document.elementFromPoint(visible.x+visible.width/2,visible.y+visible.height/2);
        if (!hit || !(node.contains(hit) || (node.matches('label') && hit===node.querySelector('input')))) bad.push({id:stage.dataset.stageId,text:node.textContent,reason:'hit center occluded',by:hit?.className});
      }
    }
    return bad;
  }); assert.deepEqual(occluded,[],'required controls remain inside stage budget');
}
try {
  browser = await chromium.launch({headless:true});
  const context = await browser.newContext({viewport:{width:390,height:844},hasTouch:true,permissions:['clipboard-read','clipboard-write']});
  context.setDefaultTimeout(6000);
  const page = await context.newPage(); page.on('pageerror',e=>errors.push(e.message));
  await page.goto(base+'/vault/');
  const stage = id => page.locator(`.vault-pattern .vault-live-stage[data-stage-id="${id}"]`);
  for (let i=1;i<=8;i++) await check(`CL-${String(i).padStart(3,'0')} dual themes, contrast, CTA and Hex+Token copy`,async()=>{
    const id=`CL-${String(i).padStart(3,'0')}`, s=page.locator(`[data-specimen-id="${id}"]`), theme=s.locator('[data-specimen-theme-toggle]');
    await s.scrollIntoViewIfNeeded(); const before=await s.boundingBox();
    const palettes=[];
    for (const mode of ['light','dark']) {
      if (mode==='dark') await theme.click();
      const values=await contrastRead(s); contrasts.push({id,mode,values});
      assert.deepEqual(values.filter(v=>v.ratio<4.5),[],`${id} ${mode} readable text`);
      palettes.push(await s.evaluate(n=>getComputedStyle(n).backgroundColor));
      await s.locator('[data-specimen-cta]').click(); assert.equal(await s.locator('[data-specimen-cta]').getAttribute('aria-pressed'),'true');
      assert.match(await s.locator('.specimen-status').textContent(),/就绪/);
      await s.locator('[data-specimen-cta]').click();
      for (const chip of await s.locator('.vault-swatch').all()) {
        const expected=await chip.getAttribute('data-copy'); assert.match(expected,/^#[0-9A-F]{6} \| (canvas|surface|ink|muted|accent|accent-2|border|on-accent)$/);
        await chip.click(); assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),expected);
      }
      const after=await s.boundingBox(); assert.equal(after.height,before.height); assert.equal(after.width,before.width);
      await screenshot(page,`${id}-${mode}-390.png`,s);
    }
    assert.notEqual(palettes[0],palettes[1]); await theme.click();
  });
  await check('MP-001 folded corner hover/click/keyboard settles',async()=>{
    const s=stage('MP-001'),b=s.locator('button');await b.hover();await page.waitForTimeout(520);
    const transformed=await s.locator('.peel-corner').evaluate(n=>getComputedStyle(n).transform);assert.notEqual(transformed,'none');assert.equal(await b.getAttribute('aria-pressed'),'true');
    await page.mouse.move(0,0);assert.equal(await b.getAttribute('aria-pressed'),'false');
    await b.focus();await page.keyboard.press('Space');assert.equal(await b.getAttribute('aria-pressed'),'true');await page.keyboard.press('Space');assert.equal(await b.getAttribute('aria-pressed'),'false');
  });
  await check('MP-002 actual threshold commit, early cancel, pointer cancel, reset and keyboard alternate',async()=>{
    const s=stage('MP-002'),thumb=s.locator('.stage-thumb');
    await dragMouse(page,thumb,.6);assert.equal(await thumb.getAttribute('aria-valuenow'),'0');assert.match(await s.locator('output').textContent(),/取消/);
    await dragMouse(page,thumb,.9);assert.equal(await thumb.getAttribute('aria-valuenow'),'100');assert.match(await s.locator('output').textContent(),/已确认执行/);
    await s.locator('[data-reset-confirm]').click(); assert.equal(await thumb.getAttribute('aria-valuenow'),'0');
    await thumb.scrollIntoViewIfNeeded();const r=await thumb.boundingBox();const cdp=await context.newCDPSession(page);
    await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:r.x+22,y:r.y+22}]});
    await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:r.x+100,y:r.y+22}]});
    await cdp.send('Input.dispatchTouchEvent',{type:'touchCancel',touchPoints:[]}); await cdp.detach();
    assert.equal(await thumb.getAttribute('aria-valuenow'),'0');
    await thumb.focus();await page.keyboard.press('End');await page.keyboard.press('Enter');assert.match(await s.locator('output').textContent(),/已确认/);await s.locator('[data-reset-confirm]').click();
  });
  await check('MP-003 cord drag elasticity, ambient transition and Kelvin reading',async()=>{
    const s=stage('MP-003'),b=s.locator('.stage-cord');await b.scrollIntoViewIfNeeded();const r=await b.boundingBox();
    await page.mouse.move(r.x+r.width/2,r.y+10);await page.mouse.down();await page.mouse.move(r.x+r.width/2,r.y+35,{steps:6});
    assert.match(await s.locator('path').getAttribute('d'),/71/);await page.mouse.up();assert.match(await s.locator('output').textContent(),/2700 K/);
    assert.ok(await s.evaluate(n=>n.classList.contains('is-lit')));await page.waitForTimeout(520);await b.click();assert.match(await s.locator('output').textContent(),/5600 K/);
  });
  await check('MP-004 real continuous cosine dock and six accessible named tools',async()=>{
    const s=stage('MP-004'),buttons=s.locator('.stage-tools button');await buttons.nth(2).click();await page.waitForTimeout(150);
    const scales=await buttons.evaluateAll(nodes=>nodes.map(n=>new DOMMatrix(getComputedStyle(n.querySelector('span')).transform).a));assert.ok(scales[2]>1.4&&scales[1]>1.19&&scales[3]>1.19);assert.match(await s.locator('output').textContent(),/统计/);
    const r=await buttons.nth(2).boundingBox();await page.mouse.move(r.x+r.width*.8,r.y+r.height/2);await page.waitForTimeout(120);
    const intermediate=await buttons.nth(2).locator('span').evaluate(n=>new DOMMatrix(getComputedStyle(n).transform).a);assert.ok(intermediate>1.3&&intermediate<1.45);
    await buttons.nth(5).focus();assert.match(await s.locator('output').textContent(),/设置/);await page.mouse.move(0,0);
  });
  await check('MP-005 five real reactions, long press, no count on open, Escape',async()=>{
    const s=stage('MP-005'),bubble=s.locator('.stage-bubble');await bubble.click();assert.equal(await bubble.locator('b').textContent(),'0');
    assert.equal(await s.locator('.stage-reactions button:visible').count(),5);await s.locator('.stage-reactions button').nth(1).click();assert.equal(await bubble.locator('b').textContent(),'1');
    await bubble.scrollIntoViewIfNeeded();const r=await bubble.boundingBox();await page.mouse.move(r.x+20,r.y+20);await page.mouse.down();await page.waitForTimeout(500);await page.mouse.up();assert.equal(await bubble.getAttribute('aria-expanded'),'true');
    await page.keyboard.press('Escape');assert.equal(await bubble.getAttribute('aria-expanded'),'false');assert.equal(await bubble.locator('b').textContent(),'1');
  });
  await check('MP-006 actual native file drag/drop, touch pointer path, cancel, reset',async()=>{
    const s=stage('MP-006'),file=s.locator('.stage-file'),folder=s.locator('.stage-folder');
    await file.dragTo(folder);assert.equal(await folder.locator('b').textContent(),'1');
    await s.locator('[data-reset-folder]').click();await file.scrollIntoViewIfNeeded();const a=await file.boundingBox(),b=await folder.boundingBox();const cdp=await context.newCDPSession(page);
    await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:a.x+a.width/2,y:a.y+22}]});
    await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:b.x+b.width/2,y:b.y+22}]});
    assert.ok(await folder.evaluate(n=>n.classList.contains('is-open')));
    await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});assert.equal(await folder.locator('b').textContent(),'1');
    await s.locator('[data-reset-folder]').click();await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:a.x+a.width/2,y:a.y+22}]});await cdp.send('Input.dispatchTouchEvent',{type:'touchCancel',touchPoints:[]});await cdp.detach();assert.equal(await folder.locator('b').textContent(),'0');
  });
  await check('MP-007 deterministic saved consequence',async()=>{const s=stage('MP-007');await s.locator('button').click();assert.match(await s.locator('output').textContent(),/已保存.*每周一 09:00/);const text=await s.locator('output').textContent();await s.locator('button').click();assert.equal(await s.locator('output').textContent(),text);});
  await check('MP-008 organic warp range changes actual animation and pause/resume',async()=>{
    const s=stage('MP-008'),range=s.locator('input');await range.focus();await page.keyboard.press('End');
    assert.equal(await s.locator('.stage-fluid').evaluate(n=>n.style.getPropertyValue('--warp')),'50px');assert.notEqual(await s.locator('.stage-fluid i').first().evaluate(n=>getComputedStyle(n).animationName),'none');
    await s.locator('.stage-play').click();assert.equal(await s.locator('.stage-fluid i').first().evaluate(n=>getComputedStyle(n).animationPlayState),'paused');await s.locator('.stage-play').click();assert.equal(await s.locator('.stage-fluid i').first().evaluate(n=>getComputedStyle(n).animationPlayState),'running');
  });
  await check('MP-009 pickup/fan, invalid bounce, real legal reorder and pointer path',async()=>{
    const s=stage('MP-009'),stack=s.locator('.stage-stack'),before=await stack.locator('span').allTextContents();
    await s.locator('[data-stack=pickup]').click();assert.ok(await stack.evaluate(n=>n.classList.contains('is-fanned')));
    await s.locator('[data-stack=invalid]').click();assert.match(await s.locator('output').textContent(),/非法.*回弹/);assert.ok(await stack.evaluate(n=>n.classList.contains('is-bounce')));
    await s.locator('[data-stack=legal]').click();assert.notDeepEqual(await stack.locator('span').allTextContents(),before);
    await stack.scrollIntoViewIfNeeded();const r=await stack.boundingBox();await page.mouse.move(r.x+50,r.y+20);await page.mouse.down();await page.mouse.move(r.x+90,r.y+20,{steps:8});await page.mouse.up();assert.match(await s.locator('output').textContent(),/合法重排/);
  });
  await check('IP-001 real segment cross-filter, KPI and repeat reset',async()=>{const s=stage('IP-001');assert.equal((await visibleRows(s)).length,3);await s.locator('[data-segment="力量"]').click();assert.deepEqual(await visibleRows(s),['力量 · 24 分钟']);assert.match(await s.locator('output').textContent(),/1 项 · 24 分钟/);await s.locator('[data-segment="力量"]').click();assert.equal((await visibleRows(s)).length,3);assert.match(await s.locator('output').textContent(),/74 分钟/);});
  await check('IP-002 orthogonal filter and numeric sorting preserve both choices',async()=>{const s=stage('IP-002');assert.deepEqual(await visibleRows(s),['复盘 · 8m','写作 · 12m','测试 · 20m']);await s.locator('[data-filter=doing]').click();await s.locator('[data-sort]').click();assert.deepEqual(await visibleRows(s),['测试 · 20m','写作 · 12m']);await s.locator('[data-filter=all]').click();assert.deepEqual(await visibleRows(s),['测试 · 20m','写作 · 12m','复盘 · 8m']);await s.locator('[data-sort]').click();assert.deepEqual(await visibleRows(s),['复盘 · 8m','写作 · 12m','测试 · 20m']);});
  await check('IP-003 stable master order and actual inspector selection/parameters',async()=>{const s=stage('IP-003'),list=s.locator('ol'),before=await list.textContent();await s.locator('[data-detail="提醒规则"]').click();assert.match(await s.locator('.stage-inspector').textContent(),/提醒规则.*18 分钟.*每周一/);await s.locator('[data-detail="周报摘要"]').click();assert.match(await s.locator('.stage-inspector').textContent(),/周报摘要.*12 分钟.*最近 7 天/);assert.equal(await list.textContent(),before);assert.equal(await s.locator('[data-detail][aria-pressed=true]').count(),1);});
  await check('IP-004 empty/relax restores real contextual rows without clearing other filter',async()=>{const s=stage('IP-004');await s.locator('select').selectOption('cardio');assert.deepEqual(await visibleRows(s),['慢跑 · 强度 2']);await s.locator('[data-empty]').click();assert.deepEqual(await visibleRows(s),[]);assert.match(await s.locator('output').textContent(),/没有匹配结果.*有氧训练/);await s.locator('[data-relax]').click();assert.equal(await s.locator('select').inputValue(),'cardio');assert.deepEqual(await visibleRows(s),['慢跑 · 强度 2']);});
  await check('IP-005 real checkbox hit labels update SVG ring and numbers both directions',async()=>{const s=stage('IP-005');await s.locator('label').nth(0).click();assert.match(await s.locator('output').textContent(),/1\/3.*33%/);await page.waitForTimeout(450);assert.ok(Math.abs(Number(await s.locator('.ring-value').evaluate(n=>getComputedStyle(n).strokeDashoffset.replace('px','')))-66.6667)<.01);await s.locator('label').nth(0).click();assert.match(await s.locator('output').textContent(),/0\/3.*0%/);await page.waitForTimeout(450);assert.equal(await s.locator('svg').getAttribute('aria-label'),'完成 0%');});
  await check('IP-006 accessible jargon/plain language comparison',async()=>{const s=stage('IP-006'),b=s.locator('button');await b.click();assert.match(await s.locator('.stage-copy').textContent(),/每周一上午 9:00/);assert.equal(await b.getAttribute('aria-pressed'),'true');await b.click();assert.match(await s.locator('.stage-copy').textContent(),/CRON/);});
  await check('IP-007 independent reminder, disclosed quiet time/repeat controls and instance IDs',async()=>{const s=stage('IP-007');await s.locator('.stage-switch').click();await s.locator('[data-advanced]').click();assert.equal(await s.locator('[role=switch]').isChecked(),true);await s.locator('input[type=time]').fill('23:30');await s.locator('select').selectOption({label:'工作日'});assert.match(await s.locator('output').textContent(),/已开启.*工作日.*23:30/);await s.locator('[data-advanced]').click();assert.equal(await s.locator('[role=switch]').isChecked(),true);await s.locator('[data-advanced]').click();await geometry(page,'geometry-mobile-disclosed.json');await s.locator('[data-advanced]').click();});
  await check('IP-008 actual edge anchoring independent of font size',async()=>{const s=stage('IP-008'),badge=s.locator('.stage-badge b');const initial=await badge.evaluate(n=>({top:getComputedStyle(n).top,right:getComputedStyle(n).right,size:getComputedStyle(n).fontSize}));await s.locator('[data-flip]').click();assert.equal(await badge.evaluate(n=>getComputedStyle(n).left),'0px');await s.locator('input').focus();await page.keyboard.press('End');const after=await badge.evaluate(n=>({left:getComputedStyle(n).left,bottom:getComputedStyle(n).bottom,size:getComputedStyle(n).fontSize}));assert.equal(after.left,'0px');assert.equal(after.bottom,'0px');assert.notEqual(after.size,initial.size);await s.locator('[data-flip]').click();});
  await check('Duplicate design and pattern instances stay isolated with no duplicated IDs',async()=>{
    for (const id of ['MP-005','IP-002','IP-007']) {const designs=page.locator(`.vault-design [data-stage-id="${id}"]`),design=designs.first(),pattern=stage(id);assert.ok(await designs.count()>=1);
      if(id==='MP-005') {const before=await pattern.locator('b').textContent();await design.locator('.stage-bubble').click();await design.locator('.stage-reactions button').first().click();assert.equal(await pattern.locator('b').textContent(),before);}
      if(id==='IP-002') {const before=await visibleRows(pattern);await design.locator('[data-filter=done]').click();assert.deepEqual(await visibleRows(design),['复盘 · 8m']);assert.deepEqual(await visibleRows(pattern),before);}
      if(id==='IP-007') {await design.locator('[data-advanced]').click();assert.equal(await pattern.locator('[data-advanced]').getAttribute('aria-expanded'),'false');await design.locator('[data-advanced]').click();}
    }
    const duplicates=await page.evaluate(()=>{const ids=[...document.querySelectorAll('[id]')].map(n=>n.id);return ids.filter((id,i)=>ids.indexOf(id)!==i);});assert.deepEqual(duplicates,[]);
  });
  await check('11 GM/VS family previews have distinct actual DOM and surfaces',async()=>{
    const values=await page.locator('.vault-material-preview').evaluateAll(nodes=>nodes.map(n=>({id:n.dataset.previewId,dom:n.innerHTML,bg:getComputedStyle(n).background,color:getComputedStyle(n).color})));assert.equal(values.length,11);assert.equal(new Set(values.map(v=>v.dom)).size,11);assert.equal(new Set(values.map(v=>v.bg)).size,11);await evidence('material-previews.json',values);
  });
  await check('390px stage budgets, actual 44px hit regions and no overflow',async()=>{await geometry(page,'geometry-mobile.json');const heights=await page.locator('.vault-live-stage').evaluateAll(nodes=>nodes.map(n=>n.getBoundingClientRect().height));assert.ok(heights.every(h=>h>=180&&h<=200));});
  const remote=process.env.DEMO_BASELINE || 'origin/master';
  for (const goal of ['aidash-cards-redesign','voxpocket-holistic-redesign']) await check(`${goal} remote content preserved; SELECT STAR NOTES filter copy reload and Strata isolation`,async()=>{
    const path=`demos/${goal}/index.html`,upstream=execFileSync('git',['show',`${remote}:${path}`],{cwd:root,encoding:'utf8'});
    await page.goto(base+`/demos/${goal}/`);const comparison=await page.evaluate(source=>{const baseline=new DOMParser().parseFromString(source,'text/html');const read=doc=>({summaries:[...doc.querySelectorAll('.variant-summary')].map(n=>n.outerHTML),iframes:[...doc.querySelectorAll('#portal-grid iframe')].map(n=>n.getAttribute('src')),config:JSON.parse(doc.querySelector('#gallery-config').textContent)});return {baseline:read(baseline),current:read(document)};},upstream);
    assert.deepEqual(comparison.current,comparison.baseline);assert.equal(await page.locator('html').getAttribute('data-strata-brand'),'yellow');
    const current=page.locator('#portal-grid .variant-card:visible').first();await current.locator('[data-select]').check();await current.locator('[data-star]').check();const note=`恢复验收 ${goal}\n完整多行笔记，不截断`;await current.locator('[data-note]').fill(note);
    const data=await current.evaluate(n=>({...n.__galleryCard}));const state=await page.evaluate(goal=>localStorage.getItem('design-gallery:'+goal),goal);assert.ok(JSON.parse(state));
    await page.locator('[data-group-filter=all]').click();assert.equal(await page.locator('#portal-grid .variant-card:visible').count(),comparison.current.config.cards.length);
    await page.locator('#copy-summary').click();const copied=await page.evaluate(()=>navigator.clipboard.readText());assert.ok(copied.includes(note));assert.match(copied,/SELECT:.*r\d+\//);assert.match(copied,/STAR:.*r\d+\//);
    await page.reload();const restored=page.locator(`#portal-grid .variant-card[data-group="${data.category}"][data-round="${data.round}"][data-variant="${data.id}"]`);assert.equal(await restored.locator('[data-note]').inputValue(),note);assert.equal(await restored.locator('[data-select]').isChecked(),true);assert.equal(await restored.locator('[data-star]').isChecked(),true);
    await page.locator('[data-theme-choice=dark]').click();assert.equal(await page.locator('html').getAttribute('data-lp-theme'),'dark');const header=await page.locator('.site-header__bar').evaluate(n=>({background:getComputedStyle(n).backgroundColor,borderRadius:getComputedStyle(n).borderRadius,font:getComputedStyle(n).fontFamily}));assert.notEqual(header.background,'rgba(0, 0, 0, 0)');
    await page.locator('[data-portal-theme=light]').click();assert.equal(await page.locator('html').getAttribute('data-lp-theme'),'dark');
    storageEvidence.push({goal,candidates:comparison.current.config.cards.length,summaries:comparison.current.summaries.length,iframeSources:comparison.current.iframes,stored:state,copied,header});await screenshot(page,`${goal}-390-dark.png`);await page.locator('[data-theme-choice=light]').click();
  });
  await check('Demos hub dynamic remote counts, all compatibility aliases and read-only complete storage copy',async()=>{
    await page.evaluate(()=>{localStorage.setItem('aidash-cards-r2:note:scheduled-pulse:v01','旧版完整观察\n第二行');localStorage.setItem('aidash-cards-r2:star:scheduled-pulse:v01','1');localStorage.setItem('aidash-cards-r2:selection:select-scheduled-pulse','v01');});
    const before=await page.evaluate(()=>({...localStorage}));await page.goto(base+'/demos/');
    for(const goal of ['aidash-cards-redesign','voxpocket-holistic-redesign']) {const card=page.locator(`[data-demo-goal="${goal}"]`);assert.equal(await card.count(),1);const remoteCount=storageEvidence.find(s=>s.goal===goal).candidates;assert.match(await card.textContent(),new RegExp(`${remoteCount} 套候选`));assert.equal(await page.locator(`[data-goal-telemetry="${goal}"]`).count(),1);await page.locator(`[data-copy-goal="${goal}"]`).click();assert.ok((await page.evaluate(()=>navigator.clipboard.readText())).includes(`恢复验收 ${goal}`));}
    await page.locator('#copy-all-demos-summary').click();const copied=await page.evaluate(()=>navigator.clipboard.readText());assert.match(copied,/旧版完整观察\n第二行/);assert.equal(await page.locator('.summary-preview').inputValue(),copied);assert.deepEqual(await page.evaluate(()=>({...localStorage})),before);
    await screenshot(page,'demos-390-light.png');
  });
  await check('Malformed and denied storage plus clipboard fallback do not break hub',async()=>{
    const blocked=await browser.newContext({viewport:{width:390,height:844}});await blocked.addInitScript(()=>{Object.defineProperty(window,'localStorage',{get(){throw new Error('denied');}});Object.defineProperty(navigator,'clipboard',{value:{writeText(){return Promise.reject(new Error('denied'));}}});});
    const p=await blocked.newPage();p.on('pageerror',e=>errors.push(e.message));await p.goto(base+'/demos/');await p.locator('#copy-all-demos-summary').click();assert.match(await p.locator('#copy-result').textContent(),/手动复制/);assert.match(await p.locator('.summary-preview').inputValue(),/Goal:/);await blocked.close();
    await page.evaluate(()=>localStorage.setItem('design-gallery:aidash-cards-redesign','{invalid'));await page.reload();assert.match(await page.locator('[data-goal-telemetry="aidash-cards-redesign"]').textContent(),/已记录/);
  });
  for (const width of [390,1280]) for (const appearance of ['light','dark']) for (const motion of ['no-preference','reduce']) await check(`Real viewport/section evidence ${width} ${appearance} ${motion}`,async()=>{
    await page.setViewportSize({width,height:width===390?844:900});await page.emulateMedia({colorScheme:appearance,reducedMotion:motion});await page.evaluate(mode=>localStorage.setItem('lp-theme',mode),appearance);await page.goto(base+'/vault/');await screenshot(page,`vault-${width}-${appearance}-${motion}.png`);
    for(const id of ['MP-001','MP-002','MP-003','MP-004','MP-005','MP-006','MP-007','MP-008','MP-009','IP-001','IP-002','IP-003','IP-004','IP-005','IP-006','IP-007','IP-008']) await screenshot(page,`${id}-${width}-${appearance}-${motion}.png`,stage(id));
    await geometry(page,`geometry-${width}-${appearance}-${motion}.json`);
    if(motion==='reduce') {const s=stage('MP-008');assert.equal(await s.locator('.stage-play').textContent(),'播放流体');assert.equal(await s.locator('.stage-fluid i').first().evaluate(n=>getComputedStyle(n).animationName),'none');}
    await page.goto(base+'/demos/');assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));await screenshot(page,`demos-${width}-${appearance}-${motion}.png`);
  });
  await check('No browser errors',async()=>assert.deepEqual(errors,[]));
  await evidence('contrast.json',contrasts);await evidence('storage.json',storageEvidence);await evidence('geometry-index.json',geometryEvidence);
  const result={baseline:execFileSync('git',['rev-parse',remote],{cwd:root,encoding:'utf8'}).trim(),candidate:execFileSync('git',['rev-parse','HEAD'],{cwd:root,encoding:'utf8'}).trim(),checks,passed:checks.filter(c=>c.status==='PASS').length,failed:checks.filter(c=>c.status==='FAIL').length};await evidence('results.json',result);console.log(JSON.stringify({passed:result.passed,failed:result.failed,output}));if(result.failed)process.exitCode=1;
} finally {clearTimeout(deadline);await browser?.close();await new Promise(r=>server.close(r));}
