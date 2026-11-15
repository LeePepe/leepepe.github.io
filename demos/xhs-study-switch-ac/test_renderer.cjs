const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { assertFullStory } = require('./story_checks.cjs');
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
    assert.equal(results.size, 15);
    for (const style of ['a', 'b', 'c']) {
      const visible = [...results.values()].filter(g => g.style === style);
      assert.equal(visible.length, 5);
      assertFullStory(visible.flatMap(g => g.children.map(t => t.text)).join('\n'), `visible suite ${style}`);
    }
    const blog = fs.readFileSync(path.resolve(__dirname, '../../thoughts/study-switch-long-press-ac/index.html'), 'utf8').replace(/<[^>]+>/g, '');
    assertFullStory(blog, 'generated Blog');
    if (process.env.STORY_SOURCE_PATH) {
      const source = fs.readFileSync(process.env.STORY_SOURCE_PATH, 'utf8');
      assertFullStory(source, 'canonical source');
      assert.match(source, /24℃[\s\S]*只是举例/);
      assert.match(source, /99%[\s\S]*修辞，不是测量数据/);
      if (process.env.STORY_INDEX_PATH) {
        const rows = fs.readFileSync(process.env.STORY_INDEX_PATH, 'utf8').split('\n').filter(line => line.includes('](thoughts/study-switch-long-press-ac.md)'));
        assert.equal(rows.length, 1);
        assertFullStory(rows[0] + source, 'canonical index and source');
        for (const phrase of ['装修', 'NAS', '搁置', '2025', 'AI', 'YAML', '初步骨架', '实机测试', '微调', '睡前', '关灯', '拉窗帘', '买多', '测试键', '夏天', '共用遥控器', '米家', '闲置长按', '开', '2026-11-15']) {
          assert.ok(rows[0].includes(phrase), `index insight missing ${phrase}`);
        }
      }
    }
    assert.throws(() => assertFullStory('遥控器丢了，长按开空调。', 'T1 old gist'), /missing renovation/);
    const baselineStory = [...results.values()].filter(g => g.style === 'a').flatMap(g => g.children.map(t => t.text)).join('\n');
    assert.throws(() => assertFullStory(baselineStory.replace(/实机测试/g, ''), 'missing manual work'), /manual testing/);
    assert.throws(() => assertFullStory(baselineStory.replace(/测试键/g, ''), 'missing spare origin'), /study test key/);
    for (const id of ['a-04', 'b-04', 'c-03']) {
      const measured = results.get(id);
      assert.deepEqual([1, 2, 3, 4, 5].map(n => measured.children.find(t => t.id === `step-${n}`).text.replace(/^\d+\s+/, '')), ['掏手机', '解锁', '打开米家', '找书房', '点开机']);
    }
    const principles = results.get('a-05').children;
    assert.deepEqual(principles.filter(t => t.id.startsWith('principle-number')).map(t => t.text), ['01', '02', '03']);
    assert.deepEqual(principles.filter(t => t.id.startsWith('principle-heading')).map(t => t.text), ['AI 让我能开始', '多余的东西，接住真实痛点', '最高频的意图，砍掉选择']);
    const copy = id => results.get(id).children.map(t => t.text).join('\n');
    assert.match(copy('a-05'), /睡眠／离家[\s\S]*不提供自动化配置/);
    assert.match(copy('c-04'), /不是开关切换/);
    for (const g of results.values()) {
      assert.doesNotMatch(copy(g.id), /等反馈|等待反馈|\d+℃|\d+%/);
      if (g.style === 'b') {
        assert.equal(g.images.length, 1);
        assert.ok(g.images[0].visibleAreaLowerBound >= 10000);
        assert.equal(g.images[0].naturalWidth, 1024);
        assert.equal(g.images[0].naturalHeight, 1536);
        const { paintedFrame: p, visibleFrame: v, visibleAreaLowerBound: area } = g.images[0];
        assert.ok(v.x >= p.x && v.y >= p.y && v.x + v.width <= p.x + p.width + .01 && v.y + v.height <= p.y + p.height + .01, 'visibility cells must not include contain gutters or mask boundary pixels');
        assert.ok(area <= p.width * p.height);
      }
      if (g.style === 'c') {
        assert.equal(g.images.length, 0);
        assert.ok(g.children.find(t => t.id === 'title').platformFonts.some(f => f.familyName.includes('Songti') && f.glyphCount > 0), 'C headings must really render in Songti');
      }
    }
    const points = [[252, 624], [804, 624], [804, 808], [252, 808], [252, 992]];
    points.forEach(([x, y], i) => {
      const label = results.get('c-03').children.find(t => t.id === `step-${i + 1}`);
      assert.deepEqual(label.frame, { x: x - 148, y: y + 36, width: 296, height: 63 });
    });
    const motifs = { 'c-01': ['C-nas-high-step', 'C-ai-document-skeleton', 'C-human-wrench'], 'c-02': ['C-moon-light-curtain', 'C-desk-test-button'], 'c-03': ['C-search-sofa', 'C-phone', 'C-serpentine-path'], 'c-04': ['C-pressing-hand', 'C-button', 'C-node-red-fold', 'C-wind'], 'c-05': ['C-thread', 'C-button'] };
    for (const [id, required] of Object.entries(motifs)) {
      for (const motif of required) assert.ok(results.get(id).decorations.some(d => d.id === motif && d.pathCount > 0));
    }
    const signatures = [...results.values()].map(g => JSON.stringify({
      textFrames: g.children.map(t => t.frame),
      imageFrames: g.images.map(i => [i.frame, i.borderRadius]),
      artFrames: g.decorations.map(d => [d.frame, d.pathCount]),
    }));
    assert.equal(new Set(signatures).size, 15, 'independent real compositions, not merely different topology labels');

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
    for (const [card, role, size, lineHeight] of [['a-01', 'title', 80, 96], ['a-02', 'year', 96, 112], ['b-02', 'manual-testing', 40, 60], ['c-04', 'binding', 42, 63]]) {
      const t = results.get(card).children.find(t => t.id === role);
      assert.deepEqual([t.fontSize, t.lineHeight], [size, lineHeight], 'broad theme rules must not override role metrics');
    }
    const paragraph = results.get('b-02').children.find(t => t.id === 'ai-skeleton');
    assert.ok(paragraph.lines.length >= 3 && paragraph.glyphs.length > 30);
    assertCard(results.get('b-02')); // Same-paragraph ranges and decorative backgrounds are not separate blocks.
    console.log('All 15 real card compositions/full-story/source/font/image checks and 12 failing regression mutations passed.');
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
