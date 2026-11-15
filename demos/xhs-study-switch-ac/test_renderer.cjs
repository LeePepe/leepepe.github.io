const assert = require('node:assert/strict');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const { buildCards, text, shell } = require('./cards.cjs');
const { assertMarkup, prepareCard, measureCard, assertCard, platformFonts } = require('./card_geometry.cjs');

(async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1080, height: 1440 }, deviceScaleFactor: 1 });
    const cards = buildCards();
    const results = new Map();
    for (const card of cards) {
      const measured = await prepareCard(page, card);
      await platformFonts(page, measured);
      results.set(card.id, measured);
    }
    assert.equal(results.size, 13);
    for (const id of ['a-02', 'b-02', 'c-02']) {
      const measured = results.get(id);
      assert.deepEqual([1, 2, 3, 4, 5].map(n => measured.children.find(t => t.id === `step-${n}`).text.replace(/^\d+\s+/, '')), ['拿手机', '解锁', '进 App', '找书房', '点开机']);
    }
    const principles = results.get('a-05').children;
    assert.deepEqual(principles.filter(t => t.id.startsWith('principle-number')).map(t => t.text), ['01', '02', '03']);
    assert.deepEqual(principles.filter(t => t.id.startsWith('principle-heading')).map(t => t.text), ['痛点长在生活裂缝里', '最高频的动作，砍掉分支', '复杂留在背后，确定留在指尖']);
    const copy = id => results.get(id).children.map(t => t.text).join('\n');
    assert.match(copy('a-01'), /温度示意，不是作者配置/);
    assert.match(copy('a-03'), /99%[\s\S]*修辞，不是测量数据/);
    assert.match(copy('a-04'), /离开书房、睡眠／离家[\s\S]*不提供自动化配置/);
    assert.match(copy('c-03'), /不是开关切换/);
    for (const g of results.values()) {
      assert.doesNotMatch(copy(g.id), /等反馈|等待反馈/);
      if (g.style === 'b') {
        assert.equal(g.images.length, 1);
        assert.ok(g.images[0].visibleAreaLowerBound >= 10000);
        assert.equal(g.images[0].naturalWidth, 1024);
        assert.equal(g.images[0].naturalHeight, 1536);
      }
      if (g.style === 'c') {
        assert.equal(g.images.length, 0);
        assert.ok(g.children.find(t => t.id === 'title').platformFonts.some(f => f.familyName.includes('Songti') && f.glyphCount > 0), 'C headings must really render in Songti');
      }
    }
    const points = [[252, 440], [804, 440], [804, 664], [252, 664], [252, 888]];
    points.forEach(([x, y], i) => {
      const label = results.get('c-02').children.find(t => t.id === `step-${i + 1}`);
      assert.deepEqual(label.frame, { x: x - 148, y: y + 36, width: 296, height: 63 });
    });
    const motifs = { 'c-01': ['C-search-sofa', 'C-phone'], 'c-02': ['C-serpentine-path'], 'c-03': ['C-pressing-hand', 'C-button', 'C-wind'], 'c-04': ['C-thread', 'C-button'] };
    for (const [id, required] of Object.entries(motifs)) {
      for (const motif of required) assert.ok(results.get(id).decorations.some(d => d.id === motif && d.pathCount > 0));
    }
    const signatures = [...results.values()].map(g => JSON.stringify({
      textFrames: g.children.map(t => t.frame),
      imageFrames: g.images.map(i => [i.frame, i.borderRadius]),
      artFrames: g.decorations.map(d => [d.frame, d.pathCount]),
    }));
    assert.equal(new Set(signatures).size, 13, 'independent real compositions, not merely different topology labels');

    const sample = cards.find(c => c.id === 'b-03');
    const mutate = async (change, error) => {
      await prepareCard(page, sample);
      await page.evaluate(change);
      const measured = await measureCard(page, sample);
      assert.throws(() => assertCard(measured), error);
    };
    await mutate(() => { const t = document.querySelector('.t'); t.style.left = ''; t.style.top = ''; }, /MISSING_GEOMETRY/);
    await mutate(() => { document.querySelector('.t').style.left = '1000px'; }, /TEXT_SAFE_AREA/);
    await mutate(() => { document.querySelector('.t').style.fontSize = '27px'; }, /MIN_FONT/);
    await mutate(() => { document.querySelector('.t').style.width = '80px'; }, /TEXT_SCROLL_CLIPPING/);
    await mutate(() => { document.querySelector('.t').style.overflow = 'hidden'; }, /TEXT_CROPPING_STYLE/);
    await mutate(() => {
      const original = document.querySelector('.t');
      const duplicate = original.cloneNode(true);
      duplicate.dataset.text = 'collision';
      const section = document.createElement('section');
      section.dataset.group = 'different-parent';
      section.append(duplicate);
      document.querySelector('.slide').append(section);
    }, /GLYPH_OVERLAP/);
    await mutate(() => { document.querySelector('img').remove(); }, /B_IMAGE_REQUIRED/);
    await mutate(() => { document.querySelector('img').style.opacity = '0'; }, /IMAGE_INVISIBLE/);
    await mutate(() => {
      const overlay = document.createElement('div');
      overlay.style.cssText = 'position:absolute;inset:0;background:white;z-index:2';
      document.querySelector('.slide').append(overlay);
    }, /IMAGE_INVISIBLE/);
    await assert.rejects(() => prepareCard(page, { ...sample, html: sample.html.replace(/src="data:image\/png;base64,[^"]+"/, 'src="data:image/png;base64,broken"') }), /decode|source image/i);
    assert.throws(() => assertMarkup({ ...sample, html: sample.html.replace('class="t"', 'class="t" style="left:0"') }), /DUPLICATE_OR_MISSING_STYLE/);
    const glyphOnly = { id: 'glyph-only', style: 'a', topology: 'regression-fixture', html: shell('a', 'regression-fixture',
      text('first', '开', 72, 400, 200, 104, 80, 96) + text('second', '开', 72, 504, 200, 104, 80, 96)) };
    await page.setContent(glyphOnly.html);
    await page.evaluate(() => document.fonts.ready);
    const glyphGeometry = await measureCard(page, glyphOnly);
    assert.equal(glyphGeometry.children[0].frame.y + glyphGeometry.children[0].frame.height, glyphGeometry.children[1].frame.y);
    assert.throws(() => assertCard(glyphGeometry), /GLYPH_OVERLAP/, 'real Range overhang collision even when CSS frames do not intersect');
    for (const [card, role, size, lineHeight] of [['a-01', 'title', 68, 84], ['a-03', 'open-hero', 192, 208], ['b-03', 'fixed-settings', 42, 63], ['c-03', 'title', 88, 106]]) {
      const t = results.get(card).children.find(t => t.id === role);
      assert.deepEqual([t.fontSize, t.lineHeight], [size, lineHeight], 'broad theme rules must not override role metrics');
    }
    const paragraph = results.get('a-03').children.find(t => t.id === 'on-semantics');
    assert.ok(paragraph.lines.length >= 3 && paragraph.glyphs.length > 30);
    assertCard(results.get('a-03')); // Same-paragraph ranges and decorative backgrounds are not separate blocks.
    console.log('All 13 real card compositions/source/font/image checks and 12 failing regression mutations passed.');
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
