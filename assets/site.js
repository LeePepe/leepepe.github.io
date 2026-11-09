(() => {
  // 1. Strata 3-State Theme Management (Light / Dark / Auto) — synced across all site routes
  const root = document.documentElement;
  const PRIMARY_KEY = 'lp-theme';
  const LEGACY_KEY = 'lp-learn-theme';
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
      metaTheme.setAttribute('content', active === 'dark' ? '#201E17' : '#EEECE5');
    }
    document.querySelectorAll('[data-theme-val]').forEach(btn => {
      const isSelected = btn.getAttribute('data-theme-val') === validPref;
      btn.setAttribute('aria-pressed', isSelected ? 'true' : 'false');
    });
  };

  let currentPref = localStorage.getItem(PRIMARY_KEY) || localStorage.getItem(LEGACY_KEY) || 'auto';
  localStorage.setItem(PRIMARY_KEY, currentPref);
  localStorage.setItem(LEGACY_KEY, currentPref);
  applyTheme(currentPref);

  darkQuery.addEventListener('change', () => {
    if (currentPref === 'auto') applyTheme('auto');
  });

  document.querySelectorAll('[data-theme-val]').forEach(btn => {
    btn.addEventListener('click', () => {
      currentPref = btn.getAttribute('data-theme-val') || 'auto';
      localStorage.setItem(PRIMARY_KEY, currentPref);
      localStorage.setItem(LEGACY_KEY, currentPref);
      applyTheme(currentPref);
      announce(`已切换外观模式为 ${currentPref}`);
    });
  });

  // 2. Global Search Modal & Inline 404 Search
  const searchIndex = Array.isArray(window.SITE_SEARCH_INDEX) ? window.SITE_SEARCH_INDEX : [];
  const escapeHtml = s => String(s).replace(/[&<>"']/g, c => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[c]));

  const computeHits = rawQuery => {
    const q = rawQuery.trim().toLowerCase();
    if (!q) return [];
    const hits = [];
    for (const item of searchIndex) {
      const hay = `${item.title} ${item.short_title || ''} ${item.teaser || ''} ${item.series_label || ''} ${(item.tags || []).join(' ')}`.toLowerCase();
      if (hay.includes(q)) {
        hits.push({
          url: item.url,
          badge: item.series_badge || item.series_label || '文章',
          title: item.title,
          sub: item.teaser || '',
        });
      }
      for (const qa of (item.questions || [])) {
        if (`${qa.badge} ${qa.q}`.toLowerCase().includes(q)) {
          hits.push({
            url: `${item.url}#${qa.id}`,
            badge: `痛点 ${qa.badge}`,
            title: qa.q,
            sub: item.title,
          });
        }
      }
      for (const sec of (item.sections || [])) {
        if ((sec.title || '').toLowerCase().includes(q)) {
          hits.push({
            url: `${item.url}#${sec.id}`,
            badge: `${item.series_badge || '小节'}`,
            title: sec.title,
            sub: item.title,
          });
        }
      }
    }
    return hits.slice(0, 10);
  };

  const renderHitList = (box, rawQuery, onSelect) => {
    if (!box) return;
    const q = rawQuery.trim();
    if (!q) {
      box.innerHTML = `<p class="search-empty">输入关键词搜索全站 ${searchIndex.length} 篇求知笔记、痛点 Q&amp;A 与随笔感悟…</p>`;
      return;
    }
    const hits = computeHits(q);
    if (!hits.length) {
      box.innerHTML = `<p class="search-empty">未找到包含「${escapeHtml(q)}」的文章或痛点问答</p>`;
      return;
    }
    box.innerHTML = hits.map((h, idx) => (
      `<a class="search-hit${idx === 0 ? ' is-active' : ''}" role="option" href="${escapeHtml(h.url)}">` +
      `<span class="search-hit-top"><span class="search-hit-badge">${escapeHtml(h.badge)}</span>` +
      `<span>${escapeHtml(h.title)}</span></span>` +
      `<span class="search-hit-sub">${escapeHtml(h.sub)}</span></a>`
    )).join('');

    box.querySelectorAll('.search-hit').forEach(link => {
      link.addEventListener('click', () => {
        if (onSelect) onSelect();
      });
    });
  };

  const searchDialog = document.getElementById('site-search-dialog');
  const searchInput = searchDialog ? searchDialog.querySelector('[data-site-search-input]') : null;
  const searchResults = searchDialog ? searchDialog.querySelector('[data-site-search-results]') : null;
  const openSearchBtns = document.querySelectorAll('[data-open-search]');
  const closeSearchBtns = document.querySelectorAll('[data-close-search]');

  const openSearch = () => {
    if (!searchDialog) return;
    if (!searchDialog.open) searchDialog.showModal();
    if (searchInput) {
      renderHitList(searchResults, searchInput.value, () => searchDialog.close());
      searchInput.focus();
      searchInput.select();
    }
  };

  const closeSearch = () => {
    if (searchDialog && searchDialog.open) searchDialog.close();
  };

  openSearchBtns.forEach(btn => btn.addEventListener('click', openSearch));
  closeSearchBtns.forEach(btn => btn.addEventListener('click', closeSearch));

  if (searchDialog) {
    searchDialog.addEventListener('click', e => {
      const r = searchDialog.getBoundingClientRect();
      if (e.target === searchDialog && (e.clientY < r.top || e.clientY > r.bottom || e.clientX < r.left || e.clientX > r.right)) {
        closeSearch();
      }
    });
  }

  if (searchInput && searchResults) {
    renderHitList(searchResults, '', closeSearch);
    searchInput.addEventListener('input', () => renderHitList(searchResults, searchInput.value, closeSearch));
    searchInput.addEventListener('keydown', e => {
      if (e.key === 'Enter') {
        const first = searchResults.querySelector('.search-hit');
        if (first) {
          e.preventDefault();
          first.click();
        }
      }
    });
  }

  // Inline 404 search box if present
  document.querySelectorAll('[data-inline-search-wrap]').forEach(wrap => {
    const inp = wrap.querySelector('[data-inline-search-input]');
    const box = wrap.querySelector('[data-inline-search-results]');
    if (!inp || !box) return;
    inp.addEventListener('input', () => {
      const q = inp.value.trim();
      box.hidden = !q;
      if (q) renderHitList(box, q, () => { box.hidden = true; });
    });
    inp.addEventListener('keydown', e => {
      if (e.key === 'Enter') {
        const first = box.querySelector('.search-hit');
        if (first && !box.hidden) {
          e.preventDefault();
          first.click();
        }
      }
    });
  });

  // Keyboard shortcut: / or Cmd+K
  document.addEventListener('keydown', e => {
    const tag = (e.target && e.target.tagName) || '';
    const isInput = tag === 'INPUT' || tag === 'TEXTAREA' || (e.target && e.target.isContentEditable);
    if ((e.key === '/' && !isInput && !e.metaKey && !e.ctrlKey) || ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k')) {
      e.preventDefault();
      openSearch();
    }
  });

  // 3. Mobile Navigation Drawer
  const navDialog = document.getElementById('site-nav-dialog');
  const openNavBtn = document.querySelector('[data-open-nav]');
  const closeNavBtn = document.querySelector('[data-close-nav]');

  if (navDialog && openNavBtn) {
    openNavBtn.addEventListener('click', () => {
      if (!navDialog.open) navDialog.showModal();
      openNavBtn.setAttribute('aria-expanded', 'true');
    });
    if (closeNavBtn) {
      closeNavBtn.addEventListener('click', () => navDialog.close());
    }
    navDialog.addEventListener('close', () => {
      openNavBtn.setAttribute('aria-expanded', 'false');
    });
    navDialog.addEventListener('click', e => {
      const r = navDialog.getBoundingClientRect();
      if (e.target === navDialog && (e.clientY < r.top || e.clientY > r.bottom || e.clientX < r.left || e.clientX > r.right)) {
        navDialog.close();
      }
    });
  }

  // 4. Series Filter Tabs on / (Home Stream) and /archive/ (Timeline Archive)
  const seriesFilterBar = document.querySelector('[data-series-filter-bar]');
  if (seriesFilterBar) {
    const tabs = [...seriesFilterBar.querySelectorAll('[data-series-filter]')];
    const items = [...document.querySelectorAll('[data-item-series]')];
    const yearBlocks = [...document.querySelectorAll('[data-archive-year]')];

    const applySeries = seriesKey => {
      const activeKey = seriesKey || 'all';
      tabs.forEach(t => {
        const isCurr = t.getAttribute('data-series-filter') === activeKey;
        t.classList.toggle('is-active', isCurr);
        t.setAttribute('aria-pressed', isCurr ? 'true' : 'false');
      });
      items.forEach(el => {
        const itemSeries = el.getAttribute('data-item-series');
        el.hidden = !(activeKey === 'all' || itemSeries === activeKey);
      });
      yearBlocks.forEach(block => {
        const visibleRows = [...block.querySelectorAll('[data-item-series]')].filter(r => !r.hidden).length;
        block.hidden = visibleRows === 0;
        const cnt = block.querySelector('[data-year-count]');
        if (cnt) cnt.textContent = `共 ${visibleRows} 篇`;
      });
    };

    tabs.forEach(t => {
      t.addEventListener('click', () => applySeries(t.getAttribute('data-series-filter') || 'all'));
    });

    const urlSeries = new URLSearchParams(location.search).get('series');
    if (urlSeries) applySeries(urlSeries);
  }

  // 5. Interactive Tag Filtering on /tags/
  const tagAtlasBar = document.querySelector('[data-tag-atlas-bar]');
  if (tagAtlasBar) {
    const chips = [...tagAtlasBar.querySelectorAll('[data-atlas-tag]')];
    const groups = [...document.querySelectorAll('[data-tag-group]')];
    const statusEl = document.querySelector('[data-tag-atlas-status]');
    let currentTag = 'all';

    const applyAtlasTag = rawTag => {
      const nextTag = (!rawTag || (rawTag === currentTag && rawTag !== 'all')) ? 'all' : rawTag;
      currentTag = nextTag;
      let visibleCount = 0;

      groups.forEach(g => {
        const gTag = g.getAttribute('data-tag-group');
        const show = currentTag === 'all' || gTag === currentTag;
        g.hidden = !show;
        if (show) visibleCount += 1;
      });

      chips.forEach(c => {
        const active = c.getAttribute('data-atlas-tag') === currentTag;
        c.classList.toggle('is-active', active);
        c.setAttribute('aria-pressed', active ? 'true' : 'false');
      });

      if (statusEl) {
        if (currentTag === 'all') {
          statusEl.hidden = true;
          statusEl.textContent = '';
        } else {
          statusEl.hidden = false;
          statusEl.textContent = `当前筛选标签：「${currentTag}」（再次点击该标签显示全部 ${groups.length} 个标签）`;
        }
      }
    };

    chips.forEach(c => {
      c.addEventListener('click', () => applyAtlasTag(c.getAttribute('data-atlas-tag') || 'all'));
    });

    const urlTag = new URLSearchParams(location.search).get('tag');
    if (urlTag) applyAtlasTag(urlTag);
  }
})();
