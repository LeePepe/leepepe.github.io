const assert = require('node:assert/strict');

const checkpoints = [
  ['renovation/NAS', /装修/, /NAS/, /HA|Home Assistant/, /Node-RED/, /这七七八八的东西也太多了/, /搁置/],
  ['25 AI skeleton, manual testing', /25\s*年\s*AI\s*破局：搭好骨架，实测自己抠/, /AI/, /YAML/, /初步[\s\S]{0,24}Node-RED\s*流/, /实机测试/, /延迟调节/, /排障/, /自己/],
  ['bedtime surplus study test key', /买多了的无线开关：随手放书房当测试键/, /一键入眠/, /关灯/, /关窗帘/, /买多/, /书房/, /测试键/],
  ['summer Mijia idle long press', /夏天/, /只剩一个/, /空调遥控器/, /掏手机\s*→\s*解锁\s*→\s*打开米家\s*App\s*→\s*找到书房\s*→\s*点开空调/, /闲置长按\s*(?:->|→)\s*盲开空调/, /Node-RED[\s\S]{0,40}长按/, /空调/],
  ['ON lesson and zero mental burden', /只需要「开」/, /听见「滴」声出风/, /零心智负担/],
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
