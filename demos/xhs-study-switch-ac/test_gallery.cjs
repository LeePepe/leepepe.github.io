const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const base = process.argv[2] || process.env.GALLERY_URL || 'http://127.0.0.1:8769/demos/xhs-study-switch-ac/';
const receiptDirectory = process.env.GALLERY_RECEIPT_DIR || __dirname;

async function ready(page) {
  const sizes = await page.evaluate(async () => {
    await document.fonts.ready;
    const images = [...document.querySelectorAll('.thumb img')];
    images.forEach(image => { image.loading = 'eager'; });
    await Promise.all(images.map(image => image.decode()));
    return images.map(image => [image.naturalWidth, image.naturalHeight]);
  });
  assert.equal(sizes.length, 13);
  assert.ok(sizes.every(([width, height]) => width === 1080 && height === 1440));
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, 'horizontal body overflow');
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    fs.mkdirSync(receiptDirectory, { recursive: true });
    const context = await browser.newContext({ viewport: { width: 375, height: 844 }, deviceScaleFactor: 1 });
    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    await page.goto(base);
    await ready(page);
    await page.screenshot({ path: path.join(receiptDirectory, 'receipt-mobile.png'), fullPage: true });
    const notes = { 'style-a': 'A note <script> & 保留', 'style-b': 'B note 完整保留\n第二行' };
    for (const [id, note] of Object.entries(notes)) {
      await page.locator(`[data-notes="${id}"]`).fill(note);
      await page.locator(`[data-star="${id}"]`).click();
      await page.locator(`[data-select="${id}"]`).click();
    }
    assert.equal(await page.locator('[data-select="style-a"]').getAttribute('aria-pressed'), 'false');
    assert.equal(await page.locator('[data-select="style-b"]').getAttribute('aria-pressed'), 'true');
    await page.reload();
    for (const [id, note] of Object.entries(notes)) {
      assert.equal(await page.locator(`[data-notes="${id}"]`).inputValue(), note);
      assert.equal(await page.locator(`[data-star="${id}"]`).getAttribute('aria-pressed'), 'true');
    }
    assert.equal(await page.locator('.copy-area script').count(), 0);
    const state = await page.evaluate(() => JSON.parse(localStorage.getItem('design-gallery:xhs-study-switch-ac')));
    const entries = Object.values(state);
    assert.equal(entries.filter(e => e.selected).length, 1);
    assert.equal(entries.filter(e => e.starred).length, 2);
    for (const [id, note] of Object.entries(notes)) {
      assert.deepEqual(state[JSON.stringify(['xhs', 1, id])], { category: 'xhs', round: 1, id, selected: id === 'style-b', starred: true, notes: note });
    }

    const hub = await context.newPage();
    await hub.goto(new URL('../', base).href);
    const telemetry = await hub.locator('[data-goal-telemetry="xhs-study-switch-ac"]').textContent();
    assert.match(telemetry, /已记录 2 条观察/);
    assert.match(telemetry, /2 个收藏/);
    assert.match(telemetry, /(?:已选 1 项|1 个选择)/);
    await hub.evaluate(() => Object.defineProperty(navigator, 'clipboard', { configurable: true, value: { writeText: async text => { window.copiedText = text; } } }));
    await hub.locator('[data-copy-goal="xhs-study-switch-ac"]').click();
    await hub.waitForFunction(() => typeof window.copiedText === 'string');
    const summary = await hub.evaluate(() => window.copiedText);
    assert.match(summary, /(?:SELECT:|选择：)\s*r1\/style-b/);
    assert.match(summary, /(?:STAR:|收藏：)\s*r1\/style-a(?:, |、)r1\/style-b/);
    for (const note of Object.values(notes)) assert.ok(summary.includes(note));

    for (const corrupt of ['{bad', '[]', 'null']) {
      await page.evaluate(value => localStorage.setItem('design-gallery:xhs-study-switch-ac', value), corrupt);
      await page.reload();
      assert.equal(await page.locator('.suite').count(), 3);
      assert.equal(await page.locator('[data-select][aria-pressed="true"]').count(), 0);
    }
    const opener = page.locator('[data-lightbox]').first();
    const close = page.locator('[data-close]');
    await opener.click();
    await page.locator('#lightbox-image').evaluate(image => image.decode());
    await page.keyboard.press('Tab');
    assert.equal(await close.evaluate(e => document.activeElement === e), true);
    await page.keyboard.press('Shift+Tab');
    assert.equal(await close.evaluate(e => document.activeElement === e), true);
    await page.keyboard.press('Escape');
    assert.equal(await page.locator('#lightbox').isHidden(), true);
    assert.equal(await opener.evaluate(e => document.activeElement === e), true);
    await opener.click();
    await page.mouse.click(10, 10);
    assert.equal(await page.locator('#lightbox').isHidden(), true);
    assert.equal(await opener.evaluate(e => document.activeElement === e), true);
    await opener.click();
    await close.click();
    assert.equal(await opener.evaluate(e => document.activeElement === e), true);

    await page.evaluate(() => Object.defineProperty(navigator, 'clipboard', { configurable: true, value: { writeText: async text => { window.copiedText = text; } } }));
    await page.locator('[data-copy-title="style-b"]').click();
    await page.waitForFunction(() => document.querySelector('[data-status="style-b"]').textContent.includes('已复制到剪贴板'));
    assert.equal(await page.evaluate(() => window.copiedText), await page.locator('[data-suite="style-b"] .copy-area strong').textContent());
    await page.locator('[data-copy-body="style-c"]').click();
    await page.waitForFunction(() => document.querySelector('[data-status="style-c"]').textContent.includes('已复制到剪贴板'));
    assert.equal(await page.evaluate(() => window.copiedText), await page.locator('[data-suite="style-c"] pre').textContent());

    const fallback = await context.newPage();
    await fallback.addInitScript(() => {
      Object.defineProperty(navigator, 'clipboard', { configurable: true, value: { writeText: () => Promise.reject(new Error('forced denial')) } });
      document.execCommand = () => false;
    });
    await fallback.goto(base);
    await fallback.locator('[data-copy-body="style-a"]').click();
    await fallback.waitForFunction(() => document.querySelector('[data-status="style-a"]').textContent.includes('手动复制'));
    const manual = fallback.locator('[data-copy-fallback]');
    assert.equal(await manual.isVisible(), true);
    assert.equal(await manual.inputValue(), await fallback.locator('[data-suite="style-a"] pre').textContent());
    assert.equal(await manual.evaluate(e => document.activeElement === e && e.selectionStart === 0 && e.selectionEnd === e.value.length), true);

    const deniedStorage = await browser.newPage({ viewport: { width: 375, height: 844 } });
    deniedStorage.on('pageerror', e => errors.push(e.message));
    await deniedStorage.addInitScript(() => Object.defineProperty(window, 'localStorage', { get() { throw new Error('storage unavailable'); } }));
    await deniedStorage.goto(base);
    await deniedStorage.locator('[data-select="style-a"]').click();
    assert.equal(await deniedStorage.locator('.suite').count(), 3);

    const desktop = await browser.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 });
    await desktop.goto(base);
    await ready(desktop);
    await desktop.screenshot({ path: path.join(receiptDirectory, 'receipt-desktop.png') });
    assert.deepEqual(errors, []);
    console.log('Gallery: 375/1280px, decoded 13 PNGs, canonical hub/select/stars/notes, corrupt/denied storage, both copy paths, modal Tab/Escape/backdrop/focus passed.');
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
