(() => {
  window.bindRecorder = root => {
    if (root.recorder) return root.recorder;
    let state = 'Idle', intent = root.dataset.kind === 'todo' || root.dataset.kind === 'hybrid' ? 'todo' : 'text';
    let timer, keyHeld = false, pointerHeld = false, suppressClick = false;
    const fields = selector => root.querySelectorAll(selector);
    const write = (selector, value) => fields(selector).forEach(x => x.textContent = value);
    function render(next) {
      state = next;
      root.dataset.state = next;
      write('[data-state]', next);
      fields('[data-hold]').forEach(b => b.setAttribute('aria-pressed', String(next === 'Listening')));
      root.dispatchEvent(new CustomEvent('recordstate', {detail: {state, intent}}));
    }
    function cancel() {
      clearTimeout(timer); keyHeld = pointerHeld = false;
      write('[data-raw]', '口述会出现在这里。');
      write('[data-refined]', '润色结果将在松手后生成。');
      fields('[data-generated]').forEach(x => x.replaceChildren());
      render('Idle');
    }
    function start(kind = intent) {
      if (state === 'Listening' || state === 'Refining') return;
      clearTimeout(timer); intent = kind; root.dataset.intent = intent;
      write('[data-raw]', intent === 'todo' ? '合成口述：准备提纲，复核摘要，留下回执。' : '合成口述：把发布决定整理成清晰的下一步。');
      write('[data-refined]', '等待松手润色…');
      render('Listening');
    }
    function release() {
      if (state !== 'Listening') return;
      render('Refining');
      timer = setTimeout(() => {
        write('[data-refined]', intent === 'todo' ? 'Todo 已拆解：确认输入 → 复核摘要 → 留下回执。' : '已润色：整理发布决定，确认下一步行动。');
        fields('[data-generated]').forEach(x => {
          x.replaceChildren();
          if (intent !== 'todo') return;
          ['确认输入', '复核摘要', '留下回执'].forEach(text => {
            const article = document.createElement('article'), label = document.createElement('label'), check = document.createElement('input');
            check.type = 'checkbox'; label.append(check, document.createTextNode(text)); article.append(label); x.append(article);
          });
        });
        render('Done');
      }, Number(root.dataset.refineDelay) || 420);
    }
    fields('[data-hold]').forEach(b => {
      b.addEventListener('pointerdown', e => {
        if (e.button !== 0) return;
        b.setPointerCapture(e.pointerId); pointerHeld = true; suppressClick = true; start();
      });
      b.addEventListener('pointerup', () => { if (pointerHeld) { pointerHeld = false; release(); } });
      b.addEventListener('pointercancel', cancel);
      b.addEventListener('lostpointercapture', () => { if (pointerHeld) cancel(); });
      b.addEventListener('click', e => {
        if (suppressClick && e.detail !== 0) { suppressClick = false; return; }
        suppressClick = false;
        if (state === 'Listening') release(); else start();
      });
    });
    fields('[data-intent]').forEach(b => b.addEventListener('click', () => {
      intent = b.dataset.intent; root.dataset.intent = intent;
      fields('[data-intent]').forEach(x => x.setAttribute('aria-pressed', String(x === b)));
      write('[data-refined]', intent === 'todo' ? 'Todo intent ready · 按住 ⌥⇧Space' : 'Text intent ready · 按住 ⌥Space');
    }));
    fields('[data-cancel]').forEach(b => b.addEventListener('click', cancel));
    const visible = () => !!root.getBoundingClientRect().width && !root.closest('[hidden]');
    addEventListener('keydown', e => {
      if (!visible() || /INPUT|TEXTAREA|SELECT/.test(e.target.tagName)) return;
      if (e.key === 'Escape') { cancel(); return; }
      if (e.code === 'Space' && e.altKey) {
        e.preventDefault(); if (e.repeat || keyHeld) return;
        keyHeld = true; start(e.shiftKey ? 'todo' : 'text');
      }
    });
    addEventListener('keyup', e => {
      if (keyHeld && (e.code === 'Space' || e.key === 'Alt')) { e.preventDefault(); keyHeld = false; release(); }
    });
    addEventListener('blur', cancel);
    root.addEventListener('recordstate', e => {
      const ribbon = root.querySelector('[data-ribbon]');
      if (ribbon) ribbon.hidden = e.detail.state === 'Idle';
      const reveal = root.querySelector('[data-reveal-target]');
      if (reveal && e.detail.state === 'Listening') reveal.hidden = false;
    });
    render('Idle');
    return root.recorder = {start, release, cancel, get state() {return state;}};
  };
  addEventListener('DOMContentLoaded', () => document.querySelectorAll('[data-recorder]').forEach(bindRecorder));
})();
