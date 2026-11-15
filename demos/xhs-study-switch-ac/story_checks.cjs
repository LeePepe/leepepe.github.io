const assert = require('node:assert/strict');

const checkpoints = [
  ['renovation/NAS', /装修/, /NAS/, /HA|Home Assistant/, /Node-RED/, /搁置/],
  ['2025 AI skeleton, manual testing', /2025/, /AI/, /YAML/, /初步[\s\S]{0,24}骨架/, /实机测试/, /微调/, /我|自己/],
  ['bedtime surplus study test key', /睡前/, /关灯/, /拉窗帘/, /买多|多买/, /书房/, /测试键/],
  ['summer Mijia idle long press', /夏天/, /(?:只剩一个|一个共用)/, /遥控器/, /掏手机/, /解锁/, /打开米家/, /找书房/, /点开机/, /闲置|闲着/, /Node-RED[\s\S]{0,40}长按/, /空调/],
  ['ON lesson and household cleanup', /只负责打开|只负责开|只需要「开」|每次只想开|长按\s*=\s*开空调/, /固定/, /睡眠/, /离家/],
];

function assertFullStory(text, label) {
  for (const [phase, ...patterns] of checkpoints) {
    for (const pattern of patterns) assert.match(text, pattern, `${label}: missing ${phase}: ${pattern}`);
  }
  assert.doesNotMatch(text, /2025\s*年?\s*夏天|等待反馈|等反馈|AI\s*(?:全自动部署|自动完成实机测试)/, `${label}: fabricated fact`);
}

function assertPostCopy(title, body, label) {
  assert.ok([...title].length <= 20, `${label}: title >20 characters`);
  const paragraphs = body.split(/\n\s*\n/);
  assert.ok([...paragraphs[0].replace(/\n/g, '')].length <= 80, `${label}: opening >80 characters`);
  for (const paragraph of paragraphs) {
    assert.ok(paragraph.split('\n').length <= 3, `${label}: paragraph >3 explicit lines`);
    assert.ok(paragraph.split('\n').every(line => !/^\s/.test(line)), `${label}: first-line indentation`);
  }
  assert.match(paragraphs.at(-1), /^#/);
  assertFullStory(body, label);
}

module.exports = { assertFullStory, assertPostCopy };
