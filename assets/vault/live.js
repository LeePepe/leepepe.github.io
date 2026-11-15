/* Each mounted stage owns its state and event listeners, including repeated design cards. */
(() => {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const clamp = (v, min, max) => Math.max(min, Math.min(max, v));
  function drag(node, {start = () => {}, move, end, cancel}) {
    let active = null;
    node.addEventListener('pointerdown', e => {
      if (e.button !== 0) return;
      active = {x: e.clientX, y: e.clientY, id: e.pointerId};
      node.setPointerCapture(e.pointerId); start(e, active);
    });
    node.addEventListener('pointermove', e => {if (active) move(e, active);});
    node.addEventListener('pointerup', e => {
      if (!active) return;
      const origin = active; active = null; end(e, origin);
      if (node.hasPointerCapture(e.pointerId)) node.releasePointerCapture(e.pointerId);
    });
    const abort = e => {if (active) {active = null; cancel(e);}};
    node.addEventListener('pointercancel', abort);
    node.addEventListener('lostpointercapture', abort);
  }
  const handlers = {
    'MP-001'(stage, say) {
      const button = stage.querySelector('.stage-peel');
      const peel = open => {stage.classList.toggle('is-peeled', open); button.setAttribute('aria-pressed', open); say(open ? '元信息已揭示' : '隐藏元信息层 · 弹簧回落');};
      let pinned = false;
      button.addEventListener('pointerenter', () => peel(true));
      button.addEventListener('pointerleave', () => {pinned = false; peel(false);});
      button.addEventListener('click', () => {pinned = !pinned; peel(pinned);});
      button.addEventListener('blur', () => {pinned = false; peel(false);});
      peel(false);
    },
    'MP-002'(stage, say) {
      const track = stage.querySelector('.stage-track'), thumb = stage.querySelector('.stage-thumb'), range = stage.querySelector('.stage-range');
      let progress = 0, locked = false;
      const render = v => {progress = clamp(Math.round(v), 0, 100); thumb.style.setProperty('--progress', progress / 100); thumb.setAttribute('aria-valuenow', progress); range.value = progress;};
      const reset = () => {locked = false; range.disabled = false; stage.classList.remove('is-confirmed', 'is-dragging'); render(0); say('拖动到 85% 确认');};
      const settle = () => {
        if (locked) return;
        stage.classList.remove('is-dragging');
        if (progress >= 85) {locked = true; range.disabled = true; render(100); stage.classList.add('is-confirmed'); say('✓ 已确认执行');}
        else {render(0); say('已取消 · 回弹归位');}
      };
      const at = e => {const r = track.getBoundingClientRect(); render((e.clientX - r.left - 22) / (r.width - 44) * 100);};
      drag(thumb, {start: () => {if (!locked) stage.classList.add('is-dragging');}, move: e => {if (!locked) at(e);}, end: settle, cancel: () => {if (!locked) {render(0); settle();}}});
      track.addEventListener('click', e => {if (e.target === track && !locked) {at(e); settle();}});
      range.addEventListener('input', () => {if (!locked) render(Number(range.value));});
      range.addEventListener('change', settle);
      thumb.addEventListener('keydown', e => {
        if (locked) return;
        if (['ArrowRight', 'ArrowLeft', 'Home', 'End', 'Enter', ' '].includes(e.key)) e.preventDefault();
        if (e.key === 'ArrowRight') render(progress + 10);
        if (e.key === 'ArrowLeft') render(progress - 10);
        if (e.key === 'Home') render(0);
        if (e.key === 'End') render(100);
        if (e.key === 'Enter' || e.key === ' ') settle();
      });
      stage.querySelector('[data-reset-confirm]').addEventListener('click', reset); reset();
    },
    'MP-003'(stage, say) {
      const cord = stage.querySelector('.stage-cord'), path = stage.querySelector('.cord-path');
      let lit = false, pulled = 0, suppressClick = false;
      const stretch = amount => {pulled = amount; path.setAttribute('d', `M130 0 Q${130 + amount / 4} 20 130 ${46 + amount}`); cord.style.transform = `translateY(${amount}px)`;};
      const toggle = () => {lit = !lit; stage.classList.toggle('is-lit', lit); cord.setAttribute('aria-pressed', lit); say(lit ? '暖光 · 2700 K' : '冷光 · 5600 K');};
      drag(cord, {move: (e, o) => stretch(clamp(e.clientY - o.y, 0, 28)), end: () => {if (pulled >= 10) {toggle(); suppressClick = true; setTimeout(() => suppressClick = false, 0);} stretch(0);}, cancel: () => stretch(0)});
      cord.addEventListener('click', () => {if (!suppressClick) {stretch(20); toggle(); setTimeout(() => stretch(0), reduced.matches ? 0 : 180);}});
      say('冷光 · 5600 K');
    },
    'MP-004'(stage, say) {
      const bar = stage.querySelector('.stage-tools'), tools = [...bar.children];
      const magnify = index => {tools.forEach((b, i) => {const d = Math.abs(i - index); b.querySelector('span').style.transform = `scale(${1 + (d <= 2 ? .225 * (1 + Math.cos(Math.PI * d / 2)) : 0)})`;}); say(tools[Math.round(index)]?.dataset.tool || '选择工具');};
      bar.addEventListener('pointermove', e => {const centers = tools.map(b => {const r = b.getBoundingClientRect(); return r.left + r.width / 2;}); const step = (centers.at(-1) - centers[0]) / 5; magnify(clamp((e.clientX - centers[0]) / step, 0, 5));});
      tools.forEach((b, i) => {b.addEventListener('focus', () => magnify(i)); b.addEventListener('click', () => magnify(i));});
      bar.addEventListener('pointerleave', () => {tools.forEach(b => b.querySelector('span').style.transform = 'scale(1)'); say('选择工具查看名称');});
      say('选择工具查看名称');
    },
    'MP-005'(stage, say) {
      const bubble = stage.querySelector('.stage-bubble'), tray = stage.querySelector('.stage-reactions');
      let timer, longPressed = false;
      const open = yes => {tray.hidden = !yes; bubble.setAttribute('aria-expanded', yes); say(yes ? '选择一个表情回应' : '点击或长按消息');};
      bubble.addEventListener('click', () => {if (!longPressed) open(tray.hidden); longPressed = false;});
      bubble.addEventListener('pointerdown', () => {longPressed = false; timer = setTimeout(() => {longPressed = true; open(true);}, 450);});
      ['pointerup', 'pointercancel', 'pointerleave'].forEach(event => bubble.addEventListener(event, () => clearTimeout(timer)));
      tray.querySelectorAll('button').forEach(b => b.addEventListener('click', () => {const badge = bubble.querySelector('b'); badge.textContent = Number(badge.textContent) + 1; open(false); say(`${b.textContent} 已回应 · ${badge.textContent} 次`); bubble.focus();}));
      stage.addEventListener('keydown', e => {if (e.key === 'Escape') {open(false); bubble.focus();}}); open(false);
    },
    'MP-006'(stage, say) {
      const file = stage.querySelector('.stage-file'), folder = stage.querySelector('.stage-folder'), count = folder.querySelector('b');
      let suppressClick = false;
      const intent = open => folder.classList.toggle('is-open', open);
      const inside = e => {const r = folder.getBoundingClientRect(); return e.clientX >= r.left && e.clientX <= r.right && e.clientY >= r.top && e.clientY <= r.bottom;};
      const ingest = () => {intent(false); count.textContent = Number(count.textContent) + 1; stage.classList.remove('is-dropped'); void stage.offsetWidth; stage.classList.add('is-dropped'); say('文件已吸入 · +1');};
      drag(file, {start: () => stage.classList.add('is-dragging'), move: (e, o) => {file.style.transform = `translate(${e.clientX - o.x}px,${e.clientY - o.y}px)`; intent(inside(e));}, end: (e, o) => {const moved = Math.hypot(e.clientX - o.x, e.clientY - o.y) > 5; if (moved && inside(e)) ingest(); file.style.transform = ''; intent(false); stage.classList.remove('is-dragging'); if (moved) {suppressClick = true; setTimeout(() => suppressClick = false, 0);}}, cancel: () => {file.style.transform = ''; intent(false); stage.classList.remove('is-dragging');}});
      file.addEventListener('dragstart', e => {e.dataTransfer.setData('text/plain', 'vault-report'); stage.classList.add('is-dragging');});
      file.addEventListener('dragend', () => {intent(false); file.style.transform = ''; stage.classList.remove('is-dragging');});
      folder.addEventListener('dragenter', e => {e.preventDefault(); intent(true);});
      folder.addEventListener('dragover', e => {e.preventDefault(); e.dataTransfer.dropEffect = 'move'; intent(true);});
      folder.addEventListener('dragleave', () => intent(false));
      folder.addEventListener('drop', e => {e.preventDefault(); if (e.dataTransfer.getData('text/plain') === 'vault-report') ingest();});
      file.addEventListener('click', () => {if (!suppressClick) ingest();});
      folder.addEventListener('click', ingest);
      stage.querySelector('[data-reset-folder]').addEventListener('click', () => {count.textContent = '0'; stage.classList.remove('is-dropped'); intent(false); say('拖动报告进入文件夹');}); say('拖动报告进入文件夹');
    },
    'MP-007'(stage, say) {
      stage.querySelector('.stage-save').addEventListener('click', e => {e.currentTarget.textContent = '✓ 已保存'; stage.classList.add('is-saved'); say('✓ 已保存 · 下次提醒：每周一 09:00');}); say('保存后立即给出下次提醒');
    },
    'MP-008'(stage, say) {
      const fluid = stage.querySelector('.stage-fluid'), button = stage.querySelector('.stage-play'), control = stage.querySelector('[data-fluid-control]');
      let paused = reduced.matches;
      const render = () => {stage.classList.toggle('is-paused', paused); button.textContent = paused ? '播放流体' : '暂停流体'; button.setAttribute('aria-pressed', !paused); say(`湍流 ${control.value}% · ${paused ? '已暂停' : '播放中'}`);};
      control.addEventListener('input', () => {fluid.style.setProperty('--warp', `${Number(control.value) / 2}px`); fluid.style.setProperty('--speed', `${8 - Number(control.value) / 20}s`); fluid.style.filter = `saturate(${1 + Number(control.value) / 100})`; render();});
      button.addEventListener('click', () => {paused = !paused; render();}); reduced.addEventListener('change', () => {if (reduced.matches) {paused = true; render();}}); render();
    },
    'MP-009'(stage, say) {
      const stack = stage.querySelector('.stage-stack');
      const pickup = () => {stack.classList.add('is-fanned'); say('成摞抓起 · 扇形展开');};
      const invalid = () => {stack.classList.remove('is-fanned', 'is-bounce'); void stack.offsetWidth; stack.classList.add('is-bounce'); say('非法落点 · 回弹归位');};
      const legal = () => {stack.append(stack.firstElementChild); stack.classList.remove('is-fanned'); say('合法重排 · ' + [...stack.children].map(c => c.dataset.card).join(' → '));};
      stage.querySelectorAll('[data-stack]').forEach(b => b.addEventListener('click', {pickup, invalid, legal}[b.dataset.stack]));
      drag(stack, {start: pickup, move: (e, o) => stack.style.setProperty('--drag-x', `${clamp(e.clientX - o.x, -35, 35)}px`), end: (e, o) => {stack.style.setProperty('--drag-x', '0px'); e.clientX - o.x > 25 ? legal() : invalid();}, cancel: () => {stack.style.setProperty('--drag-x', '0px'); invalid();}});
      stack.addEventListener('animationend', () => stack.classList.remove('is-bounce')); say('三张训练卡 · 待抽拉');
    },
    'IP-001'(stage, say) {
      const buttons = [...stage.querySelectorAll('[data-segment]')], rows = [...stage.querySelectorAll('li')]; let selected = null;
      const render = () => {buttons.forEach(b => b.setAttribute('aria-pressed', b.dataset.segment === selected)); rows.forEach(r => r.hidden = selected !== null && r.dataset.segmentRow !== selected); const visible = rows.filter(r => !r.hidden); say(`${selected || '全部'} · ${visible.length} 项 · ${visible.reduce((sum, r) => sum + Number(r.dataset.minutes), 0)} 分钟`);};
      buttons.forEach(b => b.addEventListener('click', () => {selected = selected === b.dataset.segment ? null : b.dataset.segment; render();})); render();
    },
    'IP-002'(stage, say) {
      const list = stage.querySelector('ol'), buttons = [...stage.querySelectorAll('[data-filter]')], sort = stage.querySelector('[data-sort]'); let filter = 'all', desc = false;
      const render = () => {const rows = [...list.children].sort((a, b) => (Number(a.dataset.minutes) - Number(b.dataset.minutes)) * (desc ? -1 : 1)); rows.forEach(r => {list.append(r); r.hidden = filter !== 'all' && r.dataset.status !== filter;}); buttons.forEach(b => b.setAttribute('aria-pressed', b.dataset.filter === filter)); sort.textContent = `耗时 ${desc ? '↓' : '↑'}`; say(`${rows.filter(r => !r.hidden).length} 项 · ${desc ? '降序' : '升序'}`);};
      buttons.forEach(b => b.addEventListener('click', () => {filter = b.dataset.filter; render();})); sort.addEventListener('click', () => {desc = !desc; render();}); render();
    },
    'IP-003'(stage, say) {
      const buttons = [...stage.querySelectorAll('[data-detail]')], inspector = stage.querySelector('.stage-inspector');
      buttons.forEach(b => b.addEventListener('click', () => {buttons.forEach(x => x.setAttribute('aria-pressed', x === b)); inspector.querySelector('strong').textContent = b.dataset.detail; inspector.querySelector('span').textContent = `${b.dataset.duration} 分钟 · 参数：${b.dataset.parameters}`; inspector.classList.remove('is-updated'); void inspector.offsetWidth; inspector.classList.add('is-updated'); say('详情已就地更新');}));
    },
    'IP-004'(stage, say) {
      const context = stage.querySelector('[data-context]'), rows = [...stage.querySelectorAll('li')]; let strict = false;
      const render = () => {rows.forEach(r => r.hidden = strict || r.dataset.contextRow !== context.value); stage.classList.toggle('is-empty', strict); say(`${strict ? '没有匹配结果' : rows.filter(r => !r.hidden).length + ' 项结果'} · 保留 ${context.selectedOptions[0].textContent}`);};
      context.addEventListener('change', render); stage.querySelector('[data-empty]').addEventListener('click', () => {strict = true; render();}); stage.querySelector('[data-relax]').addEventListener('click', () => {strict = false; render();}); render();
    },
    'IP-005'(stage, say) {
      const checks = [...stage.querySelectorAll('input')], circle = stage.querySelector('.ring-value'), ring = stage.querySelector('svg');
      const render = () => {const n = checks.filter(i => i.checked).length, percent = Math.round(n / 3 * 100); circle.style.strokeDashoffset = 100 - n / 3 * 100; ring.setAttribute('aria-label', `完成 ${percent}%`); say(`已完成 ${n}/3 · 达成率 ${percent}%`);};
      checks.forEach(i => i.addEventListener('change', render)); render();
    },
    'IP-006'(stage) {
      const button = stage.querySelector('[data-plain]'), copy = stage.querySelector('.stage-copy');
      button.addEventListener('click', () => {const plain = button.getAttribute('aria-pressed') !== 'true'; button.setAttribute('aria-pressed', plain); copy.textContent = plain ? '✅ 人话态：每周一上午 9:00 提醒我' : '❌ 术语态：CRON 0 9 * * 1 · RRule FREQ=WEEKLY';});
    },
    'IP-007'(stage, say, index) {
      const button = stage.querySelector('[data-advanced]'), panel = stage.querySelector('.stage-advanced'), reminder = stage.querySelector('[role=switch]');
      panel.id = `vault-advanced-${index}`; button.setAttribute('aria-controls', panel.id);
      button.addEventListener('click', () => {panel.hidden = !panel.hidden; button.setAttribute('aria-expanded', !panel.hidden);});
      const render = () => say(`${reminder.checked ? '提醒已开启' : '提醒已关闭'} · ${panel.querySelector('select').value} · ${panel.querySelector('input').value} 静音`);
      stage.querySelectorAll('input,select').forEach(i => i.addEventListener('change', render)); render();
    },
    'IP-008'(stage, say) {
      const flip = stage.querySelector('[data-flip]'), scale = stage.querySelector('[data-scale]'), card = stage.querySelector('.stage-badge');
      flip.addEventListener('click', () => {const flipped = flip.getAttribute('aria-pressed') !== 'true'; flip.setAttribute('aria-pressed', flipped); stage.classList.toggle('is-flipped', flipped); flip.textContent = flipped ? 'Leading + Bottom 孔位反转' : 'Trailing + Top 正贴'; say('角标孔位已切换');});
      scale.addEventListener('input', () => {card.style.setProperty('--badge-font', `${12 * Number(scale.value) / 100}px`); say(`字号 ${scale.value}% · 孔位保持锚定`);});
    }
  };
  document.querySelectorAll('.vault-live-stage').forEach((stage, index) => {
    const say = text => {stage.querySelector('output').textContent = text; stage.dataset.state = text;};
    handlers[stage.dataset.stageId]?.(stage, say, index);
  });
  document.querySelectorAll('.vault-mini-specimen').forEach(specimen => {
    const toggle = specimen.querySelector('[data-specimen-theme-toggle]'), cta = specimen.querySelector('[data-specimen-cta]');
    toggle.addEventListener('click', () => {
      const dark = toggle.getAttribute('aria-pressed') !== 'true'; toggle.setAttribute('aria-pressed', dark);
      specimen.setAttribute('style', dark ? specimen.dataset.darkStyle : specimen.dataset.lightStyle);
      const tokens = Object.fromEntries(specimen.getAttribute('style').split(';').map(pair => pair.split(':')));
      specimen.querySelectorAll('[data-role]').forEach(node => {const color = tokens['--spec-' + node.dataset.role]; node.style.setProperty('--swatch', color); if (node.matches('button')) {node.dataset.copy = `${color} | ${node.dataset.role}`; node.querySelector('span').textContent = color;}});
    });
    cta.addEventListener('click', () => {const done = cta.getAttribute('aria-pressed') !== 'true'; cta.setAttribute('aria-pressed', done); cta.textContent = done ? '趋势已展开 ✓' : '查看本周趋势'; specimen.querySelector('.specimen-status').textContent = done ? '● 趋势已就绪' : '● 状态稳定';});
  });
  document.querySelectorAll('[data-copy]').forEach(button => button.addEventListener('click', async () => {
    const status = document.querySelector('#vault-result');
    try {await navigator.clipboard.writeText(button.dataset.copy); status.textContent = '已复制 ' + button.dataset.copy;}
    catch (_) {status.textContent = '剪贴板不可用，请手动复制：' + button.dataset.copy;}
  }));
  const cards = [...document.querySelectorAll('.vault-card')], search = document.querySelector('#vault-search'), result = document.querySelector('#vault-result');
  let category = 'all', platform = 'all', dimension = 'all';
  const apply = () => {
    const query = search.value.toLowerCase().trim(); let visible = 0;
    cards.forEach(card => {card.hidden = !((category === 'all' || card.dataset.type === category) && (platform === 'all' || (card.dataset.platform || '').toLowerCase().includes(platform)) && (dimension === 'all' || (card.dataset.dimension || '').toLowerCase().includes(dimension.toLowerCase())) && (!query || card.dataset.search.toLowerCase().includes(query))); if (!card.hidden) visible++;});
    document.querySelectorAll('.vault-section').forEach(section => section.hidden = !section.querySelector('.vault-card:not([hidden])'));
    result.textContent = `${visible} 项可见${visible ? '' : '，没有匹配素材'}`;
  };
  const bind = (selector, update) => {const buttons = [...document.querySelectorAll(selector)]; buttons.forEach(b => b.addEventListener('click', () => {const wasActive = b.classList.contains('is-active'); buttons.forEach(x => x.classList.remove('is-active')); update(b, wasActive); b.classList.toggle('is-active', !(selector.includes('dimension') && wasActive)); apply();}));};
  bind('.vault-filter', b => category = b.dataset.filter);
  bind('button.vault-axis[data-platform]', b => platform = b.dataset.platform);
  bind('button.vault-axis[data-dimension]', (b, active) => dimension = active ? 'all' : b.dataset.dimension);
  search.addEventListener('input', apply);
  const dialog = document.querySelector('#vault-lightbox');
  document.querySelectorAll('[data-lightbox]').forEach(b => b.addEventListener('click', () => {dialog.querySelector('img').src = b.dataset.lightbox; dialog.showModal();}));
  dialog?.addEventListener('click', e => {if (e.target === dialog || e.target.closest('.vault-lightbox__close')) dialog.close();});
  apply();
})();
