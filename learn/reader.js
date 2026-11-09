(() => {
  // 1. Strata Theme Management (Auto / Light / Dark)
  const root = document.documentElement;
  const STORAGE_KEY = 'lp-learn-theme';
  const darkQuery = matchMedia('(prefers-color-scheme: dark)');

  const resolveTheme = pref => {
    if (pref === 'light' || pref === 'dark') return pref;
    return darkQuery.matches ? 'dark' : 'light';
  };

  const applyTheme = pref => {
    const active = resolveTheme(pref);
    root.setAttribute('data-lp-theme', active);
    const metaTheme = document.querySelector('meta[name="theme-color"]');
    if (metaTheme) {
      metaTheme.setAttribute('content', active === 'dark' ? '#201E17' : '#EEECE5');
    }
    document.querySelectorAll('[data-theme-toggle]').forEach(btn => {
      const label = active === 'dark' ? '☀️ 浅色' : '🌙 深色';
      btn.textContent = label;
      btn.setAttribute('aria-label', active === 'dark' ? '切换为浅色外观' : '切换为深色外观');
    });
  };

  let currentPref = localStorage.getItem(STORAGE_KEY) || 'auto';
  applyTheme(currentPref);

  darkQuery.addEventListener('change', () => {
    if (currentPref === 'auto') applyTheme('auto');
  });

  document.querySelectorAll('[data-theme-toggle]').forEach(btn => {
    btn.addEventListener('click', () => {
      const active = root.getAttribute('data-lp-theme');
      currentPref = active === 'dark' ? 'light' : 'dark';
      localStorage.setItem(STORAGE_KEY, currentPref);
      applyTheme(currentPref);
    });
  });

  // 2. Mobile Drawer Sheet
  const sheet = document.querySelector('.series-sheet');
  const opener = document.querySelector('.open-series');
  const closeBtn = document.querySelector('.close-sheet');
  const close = () => { if (sheet && sheet.open) sheet.close(); };

  if (opener && sheet) {
    opener.addEventListener('click', () => {
      sheet.showModal();
      document.body.classList.add('sheet-open');
      opener.setAttribute('aria-expanded', 'true');
    });
    if (closeBtn) closeBtn.addEventListener('click', close);
    sheet.addEventListener('close', () => {
      document.body.classList.remove('sheet-open');
      opener.setAttribute('aria-expanded', 'false');
    });
    sheet.addEventListener('click', event => {
      const bounds = sheet.getBoundingClientRect();
      if (
        event.target === sheet &&
        (event.clientY < bounds.top || event.clientX < bounds.left || event.clientX > bounds.right)
      ) {
        close();
      }
    });
  }

  const desktop = matchMedia('(min-width: 1024px)');
  desktop.addEventListener('change', event => { if (event.matches) close(); });

  // 3. Reading Progress & Section Outline Highlighting
  const article = document.querySelector('[data-reading-body]');
  if (!article) return;

  const sections = [...article.querySelectorAll('h2[id]')];
  const outlineLinks = [...document.querySelectorAll('.outline a')];
  const setActive = id => {
    outlineLinks.forEach(link => {
      if (link.hash === '#' + id) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  };

  let activeId;
  const updateSection = () => {
    const threshold = desktop.matches ? 96 : 120;
    let active = sections[0];
    for (const heading of sections) {
      if (heading.getBoundingClientRect().top <= threshold) active = heading;
      else break;
    }
    if (active && active.id !== activeId) {
      activeId = active.id;
      setActive(active.id);
    }
  };

  const observer = new IntersectionObserver(updateSection, {
    rootMargin: '-80px 0px -65% 0px',
    threshold: 0,
  });
  sections.forEach(heading => observer.observe(heading));

  outlineLinks.forEach(link => link.addEventListener('click', event => {
    event.preventDefault();
    close();
    const target = document.getElementById(link.hash.slice(1));
    if (!target) return;
    history.replaceState(null, '', link.hash);
    requestAnimationFrame(() => {
      target.scrollIntoView({
        behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth'
      });
      target.focus({ preventScroll: true });
    });
  }));

  const fills = document.querySelectorAll('[data-progress-fill]');
  const labels = document.querySelectorAll('[data-progress-label]');
  const meters = document.querySelectorAll('[role="progressbar"]');

  const update = () => {
    const rect = article.getBoundingClientRect();
    const offset = desktop.matches ? 32 : 80;
    const distance = Math.max(1, rect.height - innerHeight + offset + 32);
    const progress = Math.max(0, Math.min(1, (offset - rect.top) / distance));
    const percent = Math.round(progress * 100);
    fills.forEach(fill => { fill.style.width = `${progress * 100}%`; });
    labels.forEach(label => { label.textContent = `${percent}%`; });
    meters.forEach(meter => meter.setAttribute('aria-valuenow', String(percent)));
    updateSection();
  };

  let pending = false;
  addEventListener('scroll', () => {
    if (pending) return;
    pending = true;
    requestAnimationFrame(() => { update(); pending = false; });
  }, { passive: true });
  addEventListener('resize', update);
  addEventListener('hashchange', update);
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(update);
  }
  update();
})();
