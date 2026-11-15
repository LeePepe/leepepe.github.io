function assertMarkup(card) {
  const tags = card.html.match(/<div\b[^>]*class="t"[^>]*>/g) || [];
  if (!tags.length) throw new Error(`${card.id}: NO_TEXT`);
  for (const tag of tags) {
    if ((tag.match(/\bstyle=/g) || []).length !== 1) {
      throw new Error(`${card.id}: DUPLICATE_OR_MISSING_STYLE`);
    }
  }
}

async function measureCard(page, card) {
  return page.evaluate(({ id, style, topology }) => {
    const slide = document.querySelector('.slide');
    const frame = element => {
      const r = element.getBoundingClientRect();
      return { x: r.x, y: r.y, width: r.width, height: r.height };
    };
    const rect = r => ({ x: r.x, y: r.y, width: r.width, height: r.height });
    const opacity = element => {
      let value = 1;
      for (let e = element; e; e = e.parentElement) {
        const c = getComputedStyle(e);
        if (c.display === 'none' || c.visibility !== 'visible') return 0;
        value *= Number(c.opacity);
      }
      return value;
    };
    const texts = [...slide.querySelectorAll('.t')].map(element => {
      const c = getComputedStyle(element);
      const lines = [];
      const glyphs = [];
      const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT);
      while (walker.nextNode()) {
        const node = walker.currentNode;
        const range = document.createRange();
        range.selectNodeContents(node);
        lines.push(...[...range.getClientRects()].filter(r => r.width > 0 && r.height > 0).map(rect));
        let offset = 0;
        for (const char of node.textContent) {
          range.setStart(node, offset);
          offset += char.length;
          range.setEnd(node, offset);
          if (/\S/.test(char)) glyphs.push(...[...range.getClientRects()].filter(r => r.width > 0 && r.height > 0).map(r => ({ char, ...rect(r) })));
        }
      }
      return {
        id: element.dataset.text, tag: 'div', text: element.textContent,
        parentGroup: element.closest('[data-group]')?.dataset.group || 'canvas',
        frame: frame(element), lines, glyphs,
        fontFamily: c.fontFamily, fontSize: parseFloat(c.fontSize), lineHeight: parseFloat(c.lineHeight),
        fontWeight: c.fontWeight, color: c.color, opacity: opacity(element),
        clientWidth: element.clientWidth, clientHeight: element.clientHeight,
        scrollWidth: element.scrollWidth, scrollHeight: element.scrollHeight,
        overflowX: c.overflowX, overflowY: c.overflowY, textOverflow: c.textOverflow,
        explicit: ['left', 'top', 'width', 'height', 'fontSize', 'lineHeight', 'fontFamily'].every(key => element.style[key] !== ''),
      };
    });
    const images = [...slide.querySelectorAll('img')].map(element => {
      const f = frame(element);
      const c = getComputedStyle(element);
      const nw = element.naturalWidth;
      const nh = element.naturalHeight;
      const scale = c.objectFit === 'contain' ? Math.min(f.width / nw, f.height / nh) : Math.max(f.width / nw, f.height / nh);
      const painted = { x: f.x + (f.width - nw * scale) / 2, y: f.y + (f.height - nh * scale) / 2, width: nw * scale, height: nh * scale };
      const crop = c.objectFit === 'contain' ? { x: 0, y: 0, width: nw, height: nh } : {
        x: (f.x - painted.x) / scale, y: (f.y - painted.y) / scale, width: f.width / scale, height: f.height / scale,
      };
      // Conservative lower-bound visibility: solid overlays and even partially transparent
      // gradient regions count as occluded. Rounded/oval clipping uses browser hit testing.
      const columns = 32;
      const rows = 40;
      const cellWidth = f.width / columns;
      const cellHeight = f.height / rows;
      const points = [];
      const overlays = [...slide.querySelectorAll('*')].filter(e => {
        if (e === element || e.contains(element) || opacity(e) === 0) return false;
        const css = getComputedStyle(e);
        const alpha = css.backgroundColor.match(/rgba\([^,]+,[^,]+,[^,]+,\s*([\d.]+)\)/);
        const opaque = css.backgroundColor !== 'transparent' && (!alpha || Number(alpha[1]) >= .99);
        return opaque || css.backgroundImage !== 'none' || e.matches('.t, img, svg');
      }).map(frame);
      if (opacity(element) > 0) {
        for (let row = 0; row < rows; row++) {
          for (let col = 0; col < columns; col++) {
            const left = f.x + col * cellWidth;
            const top = f.y + row * cellHeight;
            const right = left + cellWidth;
            const bottom = top + cellHeight;
            if (left < painted.x || right > painted.x + painted.width || top < painted.y || bottom > painted.y + painted.height) continue;
            if (overlays.some(r => Math.min(right, r.x + r.width) > Math.max(left, r.x) && Math.min(bottom, r.y + r.height) > Math.max(top, r.y))) continue;
            const probes = [[left + .001, top + .001], [right - .001, top + .001], [left + .001, bottom - .001], [right - .001, bottom - .001], [(left + right) / 2, (top + bottom) / 2]];
            if (probes.every(([x, y]) => document.elementsFromPoint(x, y).includes(element))) {
              points.push({ x: (left + right) / 2, y: (top + bottom) / 2 });
            }
          }
        }
      }
      const visibleFrame = points.length ? {
        x: Math.min(...points.map(p => p.x)) - cellWidth / 2,
        y: Math.min(...points.map(p => p.y)) - cellHeight / 2,
        width: Math.max(...points.map(p => p.x)) - Math.min(...points.map(p => p.x)) + cellWidth,
        height: Math.max(...points.map(p => p.y)) - Math.min(...points.map(p => p.y)) + cellHeight,
      } : null;
      return {
        asset: element.dataset.asset, frame: f, complete: element.complete,
        naturalWidth: nw, naturalHeight: nh, opacity: opacity(element), objectFit: c.objectFit,
        objectPosition: c.objectPosition, borderRadius: c.borderRadius, paintedFrame: painted,
        sourceCrop: crop, visibleFrame, visibleAreaLowerBound: points.length * cellWidth * cellHeight,
        visibilityMethod: '32x40 full cells inside painted image; corner+center hit tests; intersecting overlay/gradient/SVG bounds excluded',
      };
    });
    const decorations = [...slide.querySelectorAll('svg')].map(e => ({
      id: e.dataset.art, frame: frame(e), viewBox: e.getAttribute('viewBox'),
      pathCount: e.querySelectorAll('path,rect,ellipse,circle,line').length,
    }));
    return {
      id, style, topology, viewportWidth: innerWidth, viewportHeight: innerHeight,
      fontsReady: document.fonts.status === 'loaded', frame: frame(slide), children: texts, images, decorations,
      unmeasuredText: [...slide.querySelectorAll('*')].filter(e => !e.closest('.t') && [...e.childNodes].some(n => n.nodeType === Node.TEXT_NODE && n.textContent.trim())).map(e => e.tagName),
    };
  }, { id: card.id, style: card.style, topology: card.topology });
}

function assertCard(geometry) {
  const fail = (code, details = '') => { throw new Error(`${geometry.id}: ${code} ${details}`.trim()); };
  const safe = { x: 72, y: 84, right: 1008, bottom: 1356 };
  const inside = (r, area, tolerance = .5) => r.x >= area.x - tolerance && r.y >= area.y - tolerance
    && r.x + r.width <= area.right + tolerance && r.y + r.height <= area.bottom + tolerance;
  const overlaps = (a, b) => Math.min(a.x + a.width, b.x + b.width) - Math.max(a.x, b.x) > .5
    && Math.min(a.y + a.height, b.y + b.height) - Math.max(a.y, b.y) > .5;
  if (geometry.frame.x !== 0 || geometry.frame.y !== 0 || geometry.frame.width !== 1080 || geometry.frame.height !== 1440) fail('CANVAS_SIZE');
  if (!geometry.fontsReady) fail('FONT_NOT_READY');
  if (geometry.unmeasuredText.length) fail('UNMEASURED_TEXT', geometry.unmeasuredText.join(','));
  if (!geometry.children.length) fail('NO_TEXT');
  const ids = new Set();
  for (const text of geometry.children) {
    if (ids.has(text.id)) fail('DUPLICATE_TEXT_ID', text.id);
    ids.add(text.id);
    if (!text.explicit) fail('MISSING_GEOMETRY', text.id);
    if (!inside(text.frame, safe)) fail('TEXT_SAFE_AREA', text.id);
    if (text.fontSize < 28 || text.lineHeight < text.fontSize) fail('MIN_FONT_OR_LINE_HEIGHT', text.id);
    if (text.opacity !== 1 || !text.glyphs.length) fail('INVISIBLE_TEXT', text.id);
    if (text.scrollWidth > text.clientWidth + 1 || text.scrollHeight > text.clientHeight + 1) fail('TEXT_SCROLL_CLIPPING', text.id);
    if (text.overflowX !== 'visible' || text.overflowY !== 'visible' || text.textOverflow === 'ellipsis') fail('TEXT_CROPPING_STYLE', text.id);
    // CJK Range boxes include ascent/negative leading outside the CSS line box.
    // Neither is clipped: both actual glyph ranges and declared frames must be safe.
    for (const glyph of text.glyphs) {
      if (!inside(glyph, safe)) fail('GLYPH_SAFE_AREA', `${text.id}:${glyph.char}`);
    }
  }
  for (let i = 0; i < geometry.children.length; i++) {
    const a = geometry.children[i];
    for (const b of geometry.children.slice(i + 1)) {
      if (a.glyphs.some(first => b.glyphs.some(second => overlaps(first, second)))) fail('GLYPH_OVERLAP', `${a.id}/${b.id}`);
      if (overlaps(a.frame, b.frame)) fail('TEXT_FRAME_OVERLAP', `${a.id}/${b.id}`);
    }
  }
  if (geometry.style === 'b' && !geometry.images.length) fail('B_IMAGE_REQUIRED');
  for (const image of geometry.images) {
    if (!image.complete || !image.naturalWidth || !image.naturalHeight) fail('IMAGE_NOT_DECODED', image.asset);
    if (image.opacity !== 1 || !image.visibleFrame || image.visibleAreaLowerBound < 10000) fail('IMAGE_INVISIBLE', image.asset);
  }
  return geometry;
}

async function prepareCard(page, card) {
  assertMarkup(card);
  await page.setContent(card.html);
  await page.evaluate(async () => {
    await document.fonts.ready;
    await Promise.all([...document.images].map(image => image.decode()));
    await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
  });
  return assertCard(await measureCard(page, card));
}

async function platformFonts(page, geometry) {
  const session = await page.context().newCDPSession(page);
  try {
    await session.send('DOM.enable');
    await session.send('CSS.enable');
    const { root } = await session.send('DOM.getDocument');
    const { nodeIds } = await session.send('DOM.querySelectorAll', { nodeId: root.nodeId, selector: '.t' });
    for (let i = 0; i < nodeIds.length; i++) {
      const { fonts } = await session.send('CSS.getPlatformFontsForNode', { nodeId: nodeIds[i] });
      geometry.children[i].platformFonts = fonts;
      if (!fonts.some(font => font.glyphCount > 0)) throw new Error(`${geometry.id}: PLATFORM_FONT_MISSING`);
    }
  } finally {
    await session.detach();
  }
}

module.exports = { assertMarkup, measureCard, assertCard, prepareCard, platformFonts };
