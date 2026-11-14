(() => {
  const all = (s, root = document) => [...root.querySelectorAll(s)];
  const q = (s, root = document) => root.querySelector(s);
  const page = document.body.dataset.page;
  const sendTheme = () => all('iframe').forEach(f => f.contentWindow?.postMessage({type:'rich-theme', theme:document.body.dataset.theme}, location.protocol === 'file:' ? '*' : location.origin));
  all('[data-theme-toggle]').forEach(b => b.onclick = () => {document.body.dataset.theme = document.body.dataset.theme === 'dark' ? 'light' : 'dark'; sendTheme();});
  all('iframe').forEach(f => f.addEventListener('load', sendTheme));
  let rating = {};
  // One stable sibling URL owns storage even where file:// isolates each document.
  const broker = document.createElement('iframe');
  broker.hidden = true; broker.title = 'Offline rating persistence';
  broker.src = new URL('rating-store-r3.html', document.currentScript.src).href;
  let saveSerial=0, deferredNavigation;
  const storeStatus=document.createElement('output');storeStatus.className='store-status';storeStatus.setAttribute('aria-live','polite');
  if(q('.gallery-index'))q('.gallery-index').prepend(storeStatus);
  function sendRatings(type, entries) {broker.contentWindow.postMessage({type,entries,serial:saveSerial},location.protocol==='file:'?'*':location.origin);}
  broker.onload = () => sendRatings('ratings-read');
  addEventListener('message', e => {
    if(e.source!==broker.contentWindow||e.origin!==(location.protocol==='file:'?'null':location.origin)||e.data?.type!=='ratings-data')return;
    if(!document.body.dataset.ratingsReady){rating=e.data.entries;redraw();document.body.dataset.ratingsReady='true';}
    if(e.data.serial===saveSerial){document.body.dataset.ratingsSaved='true';storeStatus.textContent='Saved locally';if(deferredNavigation){location.href=deferredNavigation;deferredNavigation=null;}}
  });
  document.body.append(broker);
  function save() { saveSerial++;document.body.dataset.ratingsSaved='false';storeStatus.textContent='Saving…';sendRatings('ratings-write',rating); }
  document.addEventListener('click',e=>{
    const link=e.target.closest('a[href]');
    if(link&&document.body.dataset.ratingsSaved==='false'&&!e.metaKey&&!e.ctrlKey&&!e.shiftKey){e.preventDefault();deferredNavigation=link.href;}
  },true);
  function redraw() {
    all('[data-rate]').forEach(b => {
      const r = rating[b.dataset.rate] || {};
      b.setAttribute('aria-pressed', String(!!r[b.dataset.value]));
      if (b.dataset.value === 'star') b.textContent = r.star ? '★ Starred' : '☆ Star';
    });
    all('[data-note]').forEach(x => x.value = rating[x.dataset.note]?.notes || '');
    all('[data-rating]').forEach(x => {
      const r = rating[x.dataset.rating] || {};
      x.textContent = `${r.select ? 'Selected' : 'No selection'}${r.star ? ' · Starred' : ''}`;
    });
  }
  all('[data-rate]').forEach(b => b.onclick = () => {
    const id = b.dataset.rate, field = b.dataset.value;
    rating[id] ||= {}; rating[id][field] = !rating[id][field]; rating[id].at = new Date().toISOString(); save(); redraw();
  });
  all('[data-note]').forEach(x => x.oninput = () => { rating[x.dataset.note] ||= {}; rating[x.dataset.note].notes = x.value; rating[x.dataset.note].at = new Date().toISOString(); save(); });
  all('[data-export]').forEach(b => b.onclick = () => {
    const entries = ['A','B','C'].flatMap(g => Array.from({length:g === 'A' ? 4 : 10}, (_, i) => {
      const id = `${g}-${String(i+1).padStart(2,'0')}`;
      return {id, star:false, select:false, notes:'', ...rating[id]};
    }));
    const blob = new Blob([JSON.stringify({revision:3, ratings:entries},null,2)],{type:'application/json'}), url = URL.createObjectURL(blob), a = document.createElement('a');
    a.href = url; a.download = 'voxpocket-rich-r3.json'; a.click(); setTimeout(() => URL.revokeObjectURL(url),1000);
  });
  redraw();
  function toggle(button, target) { all(button).forEach(b => b.onclick = () => {const t=q(target,b.closest('[data-stage]')); t.hidden=!t.hidden; b.setAttribute('aria-expanded', String(!t.hidden)); if(!t.hidden)RichOptics.refresh();}); }
  toggle('[data-reveal]','[data-reveal-target]'); toggle('[data-popover]','[data-popover-target]'); toggle('[data-prompter]','[data-prompter-target]');
  all('[data-recent]').forEach(b => b.onclick = () => q('[data-pasted]', b.closest('[data-stage]')).textContent = `已贴入：${b.dataset.recent}`);
  let simulatedActive = true, actualActive = true;
  function focusPaint() {
    document.body.classList.toggle('inactive', !(simulatedActive && actualActive));
    all('[data-focus-state]').forEach(x => x.textContent = simulatedActive && actualActive ? 'Active' : 'Matte');
  }
  all('[data-focus]').forEach(b => b.onclick = () => {simulatedActive=!simulatedActive;focusPaint();});
  addEventListener('blur', () => {actualActive=false;focusPaint();}); addEventListener('focus', () => {actualActive=true;focusPaint();});
  all('[data-ruler]').forEach(b => b.onclick = () => { const r=q('[data-ruler-overlay]'); r.hidden=!r.hidden; b.setAttribute('aria-pressed',String(!r.hidden)); });
  function setPlatform(mode) {
    all('[data-device]').forEach(x => { x.hidden = x.dataset.device !== mode; });
    all('[data-platform]').forEach(x=>x.setAttribute('aria-pressed',String(x.dataset.platform===mode)));
    RichOptics.refresh();
  }
  if (page.startsWith('C-') && !page.endsWith('index') && !page.endsWith('current')) setPlatform(innerWidth <= 760 ? 'phone' : 'desktop');
  all('[data-platform]').forEach(b => b.onclick = () => setPlatform(b.dataset.platform));
  all('.device[data-device]').forEach(device => {
    if (!device.className.includes('c-')) return;
    let filter='all', runnerTimer;
    function applyFilter(next=filter) {
      filter=next;
      all('[data-task]',device).forEach(t => t.hidden = filter !== 'all' && t.dataset.status !== filter);
      all('[data-filter]',device).forEach(b => b.setAttribute('aria-pressed',String(b.dataset.filter===filter)));
    }
    all('[data-filter]',device).forEach(b=>b.onclick=()=>applyFilter(b.dataset.filter));
    all('[data-check]',device).forEach(check=>check.onchange=()=>{const t=check.closest('[data-task]');t.dataset.status=check.checked?'done':'todo';applyFilter();});
    function decompose() {
      const list=q('[data-subtasks]',device);list.replaceChildren();
      ['确认输入','复核摘要','留下回执'].forEach(text=>{
        const li=document.createElement('li'), label=document.createElement('label'), check=document.createElement('input');check.type='checkbox';label.append(check,document.createTextNode(text));li.append(label);list.append(li);
      });
      list.hidden=false;const preview=q('.tree-preview',device);if(preview)preview.hidden=true;
      list.scrollIntoView({block:'nearest'});
    }
    all('[data-decompose]',device).forEach(b=>b.onclick=decompose);
    q('[data-recorder]',device).addEventListener('recordstate',e=>{if(e.detail.state==='Done')decompose();});
    all('[data-details]',device).forEach(b=>b.onclick=()=>{
      const inspector=q('[data-inspector]',device), t=b.closest('[data-task]');
      q('[data-detail-title]',inspector).textContent=q('label span',t).textContent;
      q('[data-detail-status]',inspector).textContent=t.dataset.status;
      inspector.hidden=false;
    });
    all('[data-close-details]',device).forEach(b=>b.onclick=()=>{q('[data-inspector]',device).hidden=true;});
    all('[data-runner]',device).forEach(b=>b.onclick=()=>{
      clearTimeout(runnerTimer);decompose();const out=q('[data-runner-state]',device);out.textContent='queued';
      const p0=q('[data-p0]',device);p0.dataset.status='running';applyFilter();
      runnerTimer=setTimeout(()=>{out.textContent='running';runnerTimer=setTimeout(()=>{out.textContent='complete';p0.dataset.status='done';q('[data-check]',p0).checked=true;all('[data-subtasks] input',device).forEach(c=>c.checked=true);applyFilter();},280);},160);
    });
    all('[data-inbox]',device).forEach(b=>b.onclick=()=>{const t=q('[data-inbox-target]',device);t.hidden=!t.hidden;b.setAttribute('aria-expanded',String(!t.hidden));});
    all('[data-unfold]',device).forEach(b=>b.onclick=()=>{q('[data-content]',device).classList.toggle('unfolded');b.setAttribute('aria-expanded',String(q('[data-content]',device).classList.contains('unfolded')));});
    all('[data-horizon]',device).forEach(b=>b.onclick=()=>{const t=q('[data-horizon-target]',b.parentElement);t.hidden=!t.hidden;b.setAttribute('aria-expanded',String(!t.hidden));});
    all('[data-fold-return]',device).forEach(b=>b.onclick=()=>{q('[data-recorder]',device).recorder?.cancel();q('[data-return-recorder]',device).hidden=false;});
    all('[data-return-todo]',device).forEach(b=>b.onclick=()=>q('[data-return-recorder]',device).hidden=true);
  });
  const mac=q('[data-a-mac]'), phone=q('[data-a-phone]');
  if(mac) {
    const history=['quick'];
    function go(route,push=true) {
      if(push&&history.at(-1)!==route)history.push(route);
      q('[data-a-stage]',mac).textContent=route;
      q('[data-a-quick]',mac).hidden=route!=='quick';
      all('[data-a-destination]',mac).forEach(x=>x.hidden=x.dataset.aDestination!==route);
      RichOptics.refresh(mac);
    }
    all('[data-a-nav]',mac).forEach(b=>b.onclick=()=>go(b.dataset.aNav));
    all('[data-work-check]',mac).forEach(check=>check.onchange=()=>{q('[data-work-status]',mac).textContent=check.checked?'complete':'pending';});
    all('[data-work-search]',mac).forEach(input=>input.oninput=()=>all('.command-entry',mac).forEach(row=>row.hidden=!row.textContent.toLowerCase().includes(input.value.toLowerCase())));
    all('[data-work-expand]',mac).forEach(b=>b.onclick=()=>{const list=q('[data-work-steps]',mac);list.hidden=!list.hidden;b.setAttribute('aria-expanded',String(!list.hidden));});
    let workRunner;
    all('[data-work-runner]',mac).forEach(b=>b.onclick=()=>{clearTimeout(workRunner);const out=q('[data-work-runner-state]',mac);out.textContent='queued';workRunner=setTimeout(()=>{out.textContent='running';workRunner=setTimeout(()=>{out.textContent='complete';q('[data-work-check]',mac).checked=true;q('[data-work-status]',mac).textContent='complete';},280);},160);});
    all('[data-a-back]',mac).forEach(b=>b.onclick=()=>{if(history.length>1)history.pop();go(history.at(-1),false);});
    all('[data-details]',mac).forEach(b=>b.onclick=()=>{q('[data-a-todo-detail]',mac).hidden=false;});
    all('[data-a-close-detail]',mac).forEach(b=>b.onclick=()=>{q('[data-a-todo-detail]',mac).hidden=true;});
    all('[data-check]',mac).forEach(check=>check.onchange=()=>{check.closest('[data-task]').dataset.status=check.checked?'done':'todo';});
    all('[data-a-decompose]',mac).forEach(b=>b.onclick=()=>{const list=q('[data-subtasks]',mac);list.innerHTML=['确认输入','复核结果','留下回执'].map(t=>`<li><label><input type="checkbox">${t}</label></li>`).join('');list.hidden=false;});
    function platform(mode){phone.hidden=mode!=='phone';mac.hidden=mode!=='desktop';all('[data-a-platform]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.aPlatform===mode)));RichOptics.refresh();}
    all('[data-a-platform]').forEach(b=>b.onclick=()=>platform(b.dataset.aPlatform));
    platform('phone');
    const iframe=q('iframe',phone);
    addEventListener('message',e=>{
      const expected=location.protocol==='file:'?'null':location.origin;
      if(e.source!==iframe.contentWindow||e.origin!==expected||e.data?.type!=='rich-nav')return;
      phone.dataset.route=e.data.route;
    });
  }
})();
