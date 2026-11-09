(() => {
  // 1. 3-State Theme Management (Light / Dark / Auto)
  const root = document.documentElement;
  const STORAGE_KEY = 'lp-learn-theme';
  const darkQuery = matchMedia('(prefers-color-scheme: dark)');
  const liveRegion = document.querySelector('[data-copy-live]');

  const announce = msg => {
    if (liveRegion) liveRegion.textContent = msg;
  };

  const resolveTheme = pref => {
    if (pref === 'light' || pref === 'dark') return pref;
    return darkQuery.matches ? 'dark' : 'light';
  };

  const applyTheme = pref => {
    const validPref = ['light', 'dark', 'auto'].includes(pref) ? pref : 'auto';
    const active = resolveTheme(validPref);
    root.setAttribute('data-lp-theme', active);
    root.setAttribute('data-lp-theme-pref', validPref);
    const metaTheme = document.querySelector('meta[name="theme-color"]');
    if (metaTheme) {
      metaTheme.setAttribute('content', active === 'dark' ? '#1E1B17' : '#F4EFE7');
    }
    document.querySelectorAll('[data-theme-val]').forEach(btn => {
      const isSelected = btn.getAttribute('data-theme-val') === validPref;
      btn.setAttribute('aria-pressed', isSelected ? 'true' : 'false');
    });
  };

  let currentPref = localStorage.getItem(STORAGE_KEY) || 'auto';
  applyTheme(currentPref);

  darkQuery.addEventListener('change', () => {
    if (currentPref === 'auto') applyTheme('auto');
  });

  document.querySelectorAll('[data-theme-val]').forEach(btn => {
    btn.addEventListener('click', () => {
      currentPref = btn.getAttribute('data-theme-val') || 'auto';
      localStorage.setItem(STORAGE_KEY, currentPref);
      applyTheme(currentPref);
    });
  });

  // 2. Mobile Bottom-Sheet Drawer
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

  // 3. Copy Code & Copy Section Anchor Permalink
  const copyText = async text => {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      await navigator.clipboard.writeText(text);
      return;
    }
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    ta.remove();
  };

  document.querySelectorAll('[data-copy-code]').forEach(btn => {
    btn.addEventListener('click', async () => {
      const fig = btn.closest('.code-figure');
      const pre = fig ? fig.querySelector('pre') : null;
      if (!pre) return;
      try {
        await copyText(pre.textContent || '');
        const orig = btn.textContent;
        btn.textContent = '✓ 已复制代码';
        btn.setAttribute('data-copied', 'true');
        announce('已复制代码到剪贴板');
        setTimeout(() => {
          btn.textContent = orig;
          btn.removeAttribute('data-copied');
        }, 1800);
      } catch (_) {}
    });
  });

  document.querySelectorAll('[data-copy-anchor]').forEach(btn => {
    btn.addEventListener('click', async () => {
      const hash = btn.getAttribute('data-copy-anchor') || '';
      if (!hash) return;
      const url = `${location.origin}${location.pathname}${hash}`;
      history.replaceState(null, '', hash);
      try {
        await copyText(url);
        btn.textContent = '✓ 已复制链接';
        btn.setAttribute('data-copied', 'true');
        announce('已复制小节直达链接');
        setTimeout(() => {
          btn.textContent = '#';
          btn.removeAttribute('data-copied');
        }, 1800);
      } catch (_) {}
    });
  });

  // 4. Instant Search (Press / or Cmd+K) across Essays & Sections
  const searchIndex = Array.isArray(window.THOUGHTS_INDEX)
    ? window.THOUGHTS_INDEX
    : (Array.isArray(window.LEARN_INDEX) ? window.LEARN_INDEX : []);
  const escapeHtml = s => String(s).replace(/[&<>"']/g, c => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[c]));

  const searchWraps = [...document.querySelectorAll('.rail-search-wrap')];
  searchWraps.forEach(wrap => {
    const input = wrap.querySelector('[data-learn-search]');
    const box = wrap.querySelector('[data-search-results]');
    if (!input || !box) return;

    const renderHits = rawQuery => {
      const q = rawQuery.trim().toLowerCase();
      if (!q) {
        box.hidden = true;
        box.innerHTML = '';
        return;
      }
      const hits = [];
      for (const art of searchIndex) {
        const hayArt = `${art.title} ${art.subtitle || ''} ${art.insight || ''} ${(art.tags || []).join(' ')}`.toLowerCase();
        if (hayArt.includes(q)) {
          hits.push({
            url: art.url,
            badge: `第 ${art.num} 篇`,
            title: art.title,
            sub: art.insight || art.subtitle || '',
          });
        }
        for (const sec of (art.sections || [])) {
          if (sec.title.toLowerCase().includes(q)) {
            hits.push({
              url: `${art.url}#${sec.id}`,
              badge: `${art.num} · 小节`,
              title: sec.title,
              sub: art.title,
            });
          }
        }
      }

      box.hidden = false;
      if (!hits.length) {
        box.innerHTML = `<p class="search-empty">未找到包含「${escapeHtml(rawQuery.trim())}」的感悟随笔</p>`;
        return;
      }
      box.innerHTML = hits.slice(0, 8).map((h, idx) => (
        `<a class="search-hit${idx === 0 ? ' is-active' : ''}" role="option" href="${escapeHtml(h.url)}">` +
        `<span class="search-hit-top"><span class="search-hit-badge">${escapeHtml(h.badge)}</span>` +
        `<span>${escapeHtml(h.title)}</span></span>` +
        `<span class="search-hit-sub">${escapeHtml(h.sub)}</span></a>`
      )).join('');

      box.querySelectorAll('.search-hit').forEach(link => {
        link.addEventListener('click', () => {
          box.hidden = true;
          close();
        });
      });
    };

    input.addEventListener('input', () => renderHits(input.value));
    input.addEventListener('focus', () => { if (input.value.trim()) renderHits(input.value); });
    input.addEventListener('keydown', e => {
      if (e.key === 'Escape') {
        box.hidden = true;
        input.blur();
      } else if (e.key === 'Enter') {
        const first = box.querySelector('.search-hit');
        if (first && !box.hidden) {
          e.preventDefault();
          first.click();
        }
      }
    });
  });

  document.addEventListener('click', e => {
    searchWraps.forEach(wrap => {
      if (!wrap.contains(e.target)) {
        const box = wrap.querySelector('[data-search-results]');
        if (box) box.hidden = true;
      }
    });
  });

  document.addEventListener('keydown', e => {
    const tag = (e.target && e.target.tagName) || '';
    const isInput = tag === 'INPUT' || tag === 'TEXTAREA' || (e.target && e.target.isContentEditable);
    if ((e.key === '/' && !isInput && !e.metaKey && !e.ctrlKey) || ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k')) {
      e.preventDefault();
      const targetInput = desktop.matches
        ? document.querySelector('.rail [data-learn-search]')
        : (sheet && sheet.open ? sheet.querySelector('[data-learn-search]') : null);
      if (targetInput) {
        targetInput.focus();
        targetInput.select();
      } else if (!desktop.matches && opener && sheet) {
        opener.click();
        requestAnimationFrame(() => {
          const mInput = sheet.querySelector('[data-learn-search]');
          if (mInput) mInput.focus();
        });
      }
    }
  });

  // 5. Interactive Tag Filtering on /thoughts/ Index
  const tagBar = document.querySelector('[data-tag-bar]');
  if (tagBar) {
    const filterStatus = document.querySelector('[data-filter-status]');
    const storyItems = [...document.querySelectorAll('.story-item[data-story-tags]')];
    const catSections = [...document.querySelectorAll('[data-category-section]')];
    const allTagBtns = [...document.querySelectorAll('[data-filter-tag]')];
    let currentTag = 'all';

    const applyTagFilter = tag => {
      const nextTag = (!tag || (tag === currentTag && tag !== 'all')) ? 'all' : tag;
      currentTag = nextTag;
      let visibleTotal = 0;

      storyItems.forEach(item => {
        const tags = (item.getAttribute('data-story-tags') || '').split('|');
        const show = currentTag === 'all' || tags.includes(currentTag);
        item.hidden = !show;
        if (show) visibleTotal += 1;
      });

      catSections.forEach(sec => {
        const visibleInCat = [...sec.querySelectorAll('.story-item')].filter(li => !li.hidden).length;
        sec.hidden = visibleInCat === 0;
        const cntEl = sec.querySelector('[data-category-count]');
        if (cntEl) cntEl.textContent = `${visibleInCat} 篇`;
      });

      allTagBtns.forEach(el => {
        const t = el.getAttribute('data-filter-tag');
        const active = t === currentTag;
        el.classList.toggle('is-active', active);
        if (el.hasAttribute('aria-pressed')) {
          el.setAttribute('aria-pressed', active ? 'true' : 'false');
        }
      });

      if (filterStatus) {
        if (currentTag === 'all') {
          filterStatus.hidden = true;
          filterStatus.textContent = '';
        } else {
          filterStatus.hidden = false;
          filterStatus.textContent = `已筛选标签「${currentTag}」· 共 ${visibleTotal} 篇（再次点击标签恢复全部）`;
        }
      }
    };

    allTagBtns.forEach(el => {
      el.addEventListener('click', e => {
        if (el.classList.contains('tag-pill') && el.closest('a.story-card')) {
          e.preventDefault();
          e.stopPropagation();
        }
        applyTagFilter(el.getAttribute('data-filter-tag') || 'all');
      });
      if (el.getAttribute('role') === 'button') {
        el.addEventListener('keydown', e => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            e.stopPropagation();
            applyTagFilter(el.getAttribute('data-filter-tag') || 'all');
          }
        });
      }
    });

    const urlTag = new URLSearchParams(location.search).get('tag');
    if (urlTag) applyTagFilter(urlTag);
  }

  // 6. Reading Progress & Section Outline Scroll-Spy
  const article = document.querySelector('[data-reading-body]');
  if (!article) return;

  const spyTargets = [...article.querySelectorAll('h2[id]')];
  const outlineLinks = [...document.querySelectorAll('.outline a')];
  const setActive = id => {
    outlineLinks.forEach(link => {
      if (link.hash === '#' + id) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  };

  let activeId;
  const updateSection = () => {
    const threshold = desktop.matches ? 110 : 130;
    let active = spyTargets[0];
    for (const el of spyTargets) {
      if (el.getBoundingClientRect().top <= threshold) active = el;
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
  spyTargets.forEach(el => observer.observe(el));

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
