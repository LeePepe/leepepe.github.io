(() => {
  const scheme = new URLSearchParams(location.search).get('scheme');
  const allowed = ['hub','deck','lens','stream'];
  document.body.dataset.scheme = allowed.includes(scheme) ? scheme : 'hub';
  const root = document.querySelector('.r3-app'), footer = document.querySelector('.r3-bottom');
  root.dataset.recorder = ''; root.dataset.kind = 'baseline'; root.dataset.refineDelay='900';
  document.querySelector('[data-r3-action]').setAttribute('data-hold', '');
  document.querySelector('.r3-sentence').setAttribute('data-refined', '');
  document.querySelector('.r3-feedback').setAttribute('data-state', '');
  footer.classList.add('lg-surface'); footer.dataset.liquidGlass = '';
  footer.insertAdjacentHTML('afterbegin','<span class="caustic-veil" aria-hidden="true"></span><div class="aura" aria-hidden="true"></div>');
  const fold = document.createElement('button');
  fold.className='adapter-fold';fold.dataset.fold='';fold.textContent='Fold';fold.setAttribute('aria-expanded','false');
  root.append(fold);
  const overlay=document.createElement('section');overlay.className='adapter-navigation';overlay.hidden=true;overlay.dataset.mobileRoute='';
  const routeBody = {
    todo:'<small>P0 / 下一步</small><h2>准备发布提纲</h2><label><input type="checkbox">确认输入</label><label><input type="checkbox">复核摘要</label><label><input type="checkbox">留下回执</label>',
    notes:'<h2>历史速记</h2><ol><li>草拟会议提纲</li><li>复核三项决定</li><li>归档合成摘要</li></ol>',
    settings:'<h2>设置 / 模型</h2><label>本地模型<select><option>Ready · Offline</option><option>Paused</option></select></label><p>全部为离线模拟。</p>'
  };
  const routeTitles={todo:'Todo',notes:'Notes',settings:'Settings'};
  const toolbar='<header><button data-mobile-back>Back</button><button data-detent>半高 / 全高</button><button data-close>关闭</button></header>';
  const nav='<nav>'+Object.entries(routeTitles).map(([v,n])=>`<button data-mobile-nav="${v}">${n}</button>`).join('')+'</nav>';
  const architecture=document.body.dataset.scheme;
  if(architecture==='deck') {
    overlay.innerHTML=toolbar+nav+'<div class="deck-window"><div class="route-content deck-track">'+Object.entries(routeBody).map(([route,html])=>`<article class="deck-page" data-deck-card="${route}">${html}</article>`).join('')+'</div></div><div class="deck-arrows"><button data-deck-prev>←</button><button data-deck-next>→</button></div>';
  } else if(architecture==='lens') {
    overlay.innerHTML=toolbar+'<section class="optical-destination"><small>ONE STAGE / THREE LENSES</small><div class="route-content"></div></section>'+nav;
  } else if(architecture==='stream') {
    overlay.innerHTML=toolbar+'<section class="stream-source"><small>CAPTURE → FOCUS</small><p>把刚刚的决定推进行动。</p></section><div class="route-content action-flow"></div><aside class="stream-routing">'+nav+'</aside>';
  } else {
    overlay.innerHTML='<div class="grabber"></div>'+toolbar+nav+'<div class="route-content detent-content"></div>';
  }
  if(architecture==='lens'){
    const lens=overlay.querySelector('nav');lens.classList.add('lg-surface');lens.dataset.liquidGlass='';
    const controls=document.createElement('div');controls.className='chrome-content';
    while(lens.firstChild)controls.append(lens.firstChild);
    lens.append(controls);lens.insertAdjacentHTML('afterbegin','<span class="caustic-veil" aria-hidden="true"></span>');
  }
  root.append(overlay);
  const stack=[];
  function go(route,push=true){
    if(push&&stack.at(-1)!==route)stack.push(route);
    overlay.hidden=false;overlay.dataset.route=route;
    if(architecture==='deck') {
      overlay.querySelector('.deck-track').style.transform=`translateX(-${Object.keys(routeBody).indexOf(route)*100}%)`;
      overlay.querySelectorAll('[data-deck-card]').forEach(card=>card.inert=card.dataset.deckCard!==route);
    } else overlay.querySelector('.route-content').innerHTML=routeBody[route];
    overlay.querySelectorAll('[data-mobile-nav]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.mobileNav===route)));
    overlay.style.setProperty('--deck-step',Object.keys(routeBody).indexOf(route));
    fold.setAttribute('aria-expanded','true');
    parent.postMessage({type:'rich-nav',route},location.protocol==='file:'?'*':location.origin);
    RichOptics.refresh(overlay);
  }
  function close(){overlay.hidden=true;stack.length=0;fold.setAttribute('aria-expanded','false');parent.postMessage({type:'rich-nav',route:'capture'},location.protocol==='file:'?'*':location.origin);}
  fold.onclick=()=>overlay.hidden?go('todo'):close();
  overlay.querySelectorAll('[data-mobile-nav]').forEach(b=>b.onclick=()=>go(b.dataset.mobileNav));
  overlay.querySelector('[data-mobile-back]').onclick=()=>{stack.pop();stack.length?go(stack.at(-1),false):close();};
  overlay.querySelector('[data-close]').onclick=close;
  overlay.querySelector('[data-detent]').onclick=()=>overlay.classList.toggle('full-detent');
  const step = delta => {const keys=Object.keys(routeBody),i=keys.indexOf(overlay.dataset.route);go(keys[(i+delta+keys.length)%keys.length]);};
  overlay.querySelectorAll('[data-deck-prev]').forEach(b=>b.onclick=()=>step(-1));overlay.querySelectorAll('[data-deck-next]').forEach(b=>b.onclick=()=>step(1));
  root.addEventListener('recordstate',e=>{
    const state=e.detail.state;
    document.body.classList.toggle('r3-recording',state==='Listening');
    document.body.classList.toggle('r3-refined',state==='Done');
    if(state==='Idle')document.querySelector('.r3-sentence').textContent='';
    if(state==='Done'&&document.body.dataset.scheme==='stream'){
      let action=root.querySelector('[data-result-action]');
      if(!action){action=document.createElement('button');action.dataset.resultAction='';action.textContent='上推 → 焦点行动';action.onclick=()=>go('todo');root.append(action);}
    }
  });
  addEventListener('message',e=>{
    if(e.source!==parent||e.origin!==(location.protocol==='file:'?'null':location.origin)||e.data?.type!=='rich-theme')return;
    if(['light','dark'].includes(e.data.theme))document.body.dataset.theme=e.data.theme;
  });
  addEventListener('keydown',e=>{if(e.key==='Escape')close();});
  bindRecorder(root);RichOptics.refresh();
})();