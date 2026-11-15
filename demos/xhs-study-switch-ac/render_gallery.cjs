const fs = require('node:fs');
const path = require('node:path');
const { createHash } = require('node:crypto');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const { buildCards } = require('./cards.cjs');
const { prepareCard, platformFonts } = require('./card_geometry.cjs');

async function render() {
  const browser = await chromium.launch({ headless: true });
  const output = process.env.CARD_OUTPUT_DIR || path.join(__dirname, 'assets');
  const receipt = process.env.CARD_GEOMETRY_PATH || path.join(__dirname, 'card-geometry.json');
  const cards = buildCards();
  const pages = [];
  const geometry = [];
  try {
    // Validate the whole batch before overwriting any of the thirteen published exports.
    for (const card of cards) {
      const page = await browser.newPage({ viewport: { width: 1080, height: 1440 }, deviceScaleFactor: 1 });
      pages.push(page);
      const measured = await prepareCard(page, card);
      await platformFonts(page, measured);
      geometry.push(measured);
    }
    for (let i = 0; i < cards.length; i++) {
      const card = cards[i];
      const directory = path.join(output, `style-${card.style}`);
      fs.mkdirSync(directory, { recursive: true });
      const exportFile = path.join(directory, `slide-${String(card.number).padStart(2, '0')}.png`);
      await pages[i].locator('.slide').screenshot({ path: exportFile });
      geometry[i].exportPath = `assets/style-${card.style}/slide-${String(card.number).padStart(2, '0')}.png`;
      geometry[i].exportSha256 = createHash('sha256').update(fs.readFileSync(exportFile)).digest('hex');
      for (const image of geometry[i].images) {
        image.sourceSha256 = createHash('sha256').update(fs.readFileSync(path.join(__dirname, 'assets/raw-bg', image.asset))).digest('hex');
      }
    }
    const document = {
      viewportWidth: 1080, viewportHeight: 1440, cardCount: cards.length,
      overlapPolicy: 'Every pair of separate text blocks, across all parent groups, is checked using actual glyph Range rectangles AND DOM frames. Ranges within one paragraph are not separate blocks. Decorative SVG/image backgrounds are recorded as metadata, not sibling text.',
      children: geometry.map(card => ({
        id: card.id, topology: card.topology,
        children: [card],
      })),
    };
    fs.mkdirSync(path.dirname(receipt), { recursive: true });
    fs.writeFileSync(receipt, `${JSON.stringify(document, null, 2)}\n`);
    console.log(`Rendered ${cards.length} cards; real text/image geometry and platform fonts recorded.`);
  } finally {
    await browser.close();
  }
}

if (require.main === module) render().catch(error => { console.error(error); process.exitCode = 1; });
module.exports = { render };
