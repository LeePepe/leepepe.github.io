const fs = require('node:fs');
const path = require('node:path');

const sans = '"PingFang SC","Noto Sans CJK SC","Microsoft YaHei",sans-serif';
const serif = '"Songti SC","Noto Serif CJK SC","PingFang SC",serif';
const escape = value => String(value).replace(/[&<>"']/g, c => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
}[c]));

function text(id, copy, x, y, width, height, size = 40, lineHeight = 60, options = {}) {
  if (![x, y, width, height, size, lineHeight].every(Number.isFinite)) {
    throw new Error(`Explicit text geometry required: ${id}`);
  }
  const { weight = 400, face = sans, color = 'inherit', align = 'left' } = options;
  return `<div class="t" data-text="${escape(id)}" style="left:${x}px;top:${y}px;width:${width}px;height:${height}px;font-size:${size}px;line-height:${lineHeight}px;font-family:${escape(face)};font-weight:${weight};color:${color};text-align:${align}">${escape(copy)}</div>`;
}

function art(id, x, y, width, height, viewBox, body, color = '#355E3B') {
  return `<svg data-art="${id}" aria-hidden="true" style="left:${x}px;top:${y}px;width:${width}px;height:${height}px;color:${color}" viewBox="${viewBox}" fill="none" stroke="currentColor" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">${body}</svg>`;
}
const panel = (id, x, y, width, height, fill) => `<div data-surface="${id}" style="left:${x}px;top:${y}px;width:${width}px;height:${height}px;background:${fill};border-radius:40px"></div>`;
const group = (id, body) => `<section data-group="${id}">${body}</section>`;
const pageNumber = (n, total, y = 1308) => text('page-number', `${n} / ${total}`, 928, y, 80, 42, 28, 42, { align: 'right' });
const title = (copy, size = 80, lineHeight = 96, height = 192, face = sans, y = 96) => text('title', copy, 72, y, 936, height + 16, size, lineHeight, { weight: 700, face });

const aButton = `<rect x="36" y="56" width="168" height="152" rx="44"/><path d="M36 168 Q36 226 120 234 Q204 226 204 168"/><circle cx="120" cy="122" r="38"/><path d="M60 40 Q120 14 180 40 M78 28 Q120 10 162 28"/>`;
const aAir = `<rect x="20" y="20" width="240" height="64" rx="16"/><path d="M44 54 H236 M64 100 C54 124 78 142 62 164 M140 100 C130 124 154 142 138 164 M216 100 C206 124 230 142 214 164"/>`;
const aFold = `<path d="M16 16 H180 L224 60 V156 H16 Z M180 16 V60 H224"/>`;
const bPress = `<ellipse cx="120" cy="130" rx="68" ry="54" fill="#FFFCF5"/><path d="M42 86 C76 30 174 30 206 92 M60 72 C96 30 160 34 184 66 M94 120 Q120 106 146 120"/>`;
const bBreeze = `<path opacity=".18" d="M20 104 C104 24 212 170 340 74 M46 136 C138 76 230 176 318 116 M84 66 C146 16 224 84 278 42"/>`;
const cSofa = `<path d="M28 128 Q20 64 80 64 L448 64 Q506 64 500 128 L500 156 L28 156 Z M264 70 Q254 114 264 148 M70 158 L62 178 M452 158 L460 178"/><rect x="410" y="8" width="48" height="84" rx="10" stroke-dasharray="7 9"/>`;
const cPhone = `<path d="M88 16 Q80 16 80 28 L80 148 Q80 160 92 160 L154 156 Q166 156 164 142 L160 24 Q160 12 148 14 Z" fill="#FFF4DE"/><path d="M24 174 C30 136 62 142 76 126 L82 92 Q94 76 106 96 L104 124 M94 32 L146 30 M104 142 L134 142"/>`;
const cButton = `<path d="M52 92 C44 28 248 26 252 90 C254 160 50 164 52 92 Z" fill="#FFFAEE"/><path d="M52 100 C34 210 270 212 252 100"/><ellipse cx="150" cy="90" rx="58" ry="40"/><path d="M76 30 Q150 2 226 30"/>`;
const cWind = `<path d="M20 24 Q120 16 220 24 L218 76 Q120 84 22 76 Z M44 54 Q120 58 196 54"/><path stroke="#789080" d="M60 100 Q40 124 64 156 M122 100 Q102 128 130 164 M184 100 Q164 128 190 154"/>`;

function image(asset, data, x, y, width, height, fit = 'cover', radius = '64px') {
  return `<img class="ai" data-asset="${asset}" src="${data}" alt="" style="left:${x}px;top:${y}px;width:${width}px;height:${height}px;object-fit:${fit};object-position:50% 50%;border-radius:${radius};background:#FFF7EC">`;
}

function shell(style, topology, body) {
  return `<!doctype html><html lang="zh-Hans"><head><meta charset="utf-8"><style>
*{box-sizing:border-box}html,body{margin:0}body{background:#fff}
.slide{position:relative;width:1080px;height:1440px;font-family:${sans}}
.a{background:#F5F0E6;color:#202A23}.b{background:#FFF7EC;color:#34271D}.c{background:#FFF4DE;color:#493C32}
section{position:static}.t{position:absolute;z-index:3;white-space:pre-wrap;overflow:visible;letter-spacing:0;margin:0;padding:0}
svg,[data-surface],.mask,.ai{position:absolute}svg,[data-surface],.mask{z-index:1}svg{overflow:visible}.ai{z-index:0}
</style></head><body><article class="slide ${style}" data-topology="${topology}">${body}</article></body></html>`;
}

function buildCards(root = __dirname) {
  const bg = name => `data:image/png;base64,${fs.readFileSync(path.join(root, 'assets/raw-bg', name)).toString('base64')}`;
  const bg1 = bg('study-room.png');
  const bg2 = bg('press-button.png');
  const cards = [];
  const add = (style, n, topology, body) => cards.push({ id: `${style}-${String(n).padStart(2, '0')}`, style, number: n, topology, html: shell(style, topology, body) });
  const steps = ['掏手机', '解锁', '打开米家 App', '找到书房', '点开空调'];
  const moonCurtain = `<path d="M72 20 C24 40 30 116 92 122 C52 98 42 62 72 20 Z M180 20 H316 M188 26 V136 Q208 126 224 136 V26 M308 26 V136 Q286 126 270 136 V26 M224 32 Q246 54 270 32"/><path d="M122 70 Q136 48 150 70 V90 H122 Z M136 92 V128 M118 132 H154"/>`;
  const deskButton = `<path d="M16 132 H360 M40 134 V206 M336 134 V206"/><g transform="translate(104 -4) scale(.58)">${aButton}</g>`;
  const nasBox = `<rect x="28" y="18" width="120" height="112" rx="12"/><path d="M44 50 H132 M44 76 H132 M44 102 H104 M174 130 V88 H206 V50 H236 V18"/>`;
  const wrench = `<path d="M34 176 L142 68 Q134 30 164 12 L166 46 L194 54 L214 26 Q230 74 188 94 L80 202 Z M56 182 L68 194"/><path d="M10 202 C16 166 20 146 40 140 L64 142 M94 172 Q114 182 110 200"/>`;
  const hand = `<path d="M6 208 L84 124 C98 109 116 100 140 94 L292 30 Q312 20 331 22 Q348 23 348 35 Q350 46 332 52 L236 89 Q244 96 252 105 Q262 122 246 139 Q256 159 235 174 Q241 198 216 213 L163 246 Q145 258 112 258 L6 264" fill="#FFFAEE"/><path stroke-width="3" d="M152 176 L216 124 M176 200 L238 150"/>`;

  add('a', 1, 'spare-button-asymmetric-cover',
    title('买多了的无线开关，\n随手放书房当测试键')
    + text('subtitle', '闲置长按 → 盲开空调，少一个遥控器', 72, 336, 936, 60)
    + group('spare-button', panel('button-paper', 72, 416, 352, 704, '#FFFCF6')
      + art('A-button', 132, 500, 232, 264, '0 0 240 280', aButton)
      + text('button-caption', '睡觉一键入眠\n不小心买多了', 104, 920, 288, 120))
    + group('testing-past', panel('test-paper', 448, 416, 560, 304, '#FFFCF6')
      + text('test-caption', '随手放书房桌边\n连 Node-RED 当测试键', 480, 456, 496, 120)
      + art('A-fold', 848, 600, 96, 72, '0 0 240 180', aFold))
    + group('on-present', panel('air-wash', 448, 744, 560, 376, '#E5EADC')
      + art('A-air', 496, 792, 280, 180, '0 0 280 180', aAir)
      + text('on-copy', '闲置长按 -> 盲开空调\n听见「滴」声出风', 480, 984, 496, 120))
    + text('closing', '买多了的无线开关：随手放书房当测试键。\n每次坐进书房只需要「开」就行，零心智负担。', 72, 1184, 936, 84, 28, 42)
    + pageNumber(1, 5, 1312));

  add('a', 2, 'shelved-plan-and-ai-year',
    title('这七七八八的东西，\n也太多了')
    + group('shelved-plan', panel('before-paper', 72, 416, 352, 704, '#FFFCF6')
      + text('before-heading', '装修那会儿搁置', 104, 448, 288, 60)
      + text('renovation', '想装 NAS，\n玩智能家居。\nHA、\nNode-RED，\n门槛高，搁置。', 104, 560, 288, 300)
      + art('A-plan-fold', 144, 920, 192, 128, '0 0 240 180', aFold))
    + group('ai-start', panel('after-paper', 448, 416, 560, 704, '#E5EADC')
      + text('year', '25 年', 480, 448, 496, 128, 96, 112, { weight: 700, color: '#355E3B' })
      + text('ai-skeleton', 'AI 帮写 YAML 配置、\n搭初步 Node-RED 流程。', 480, 632, 496, 120)
      + text('manual-testing', '实机测试、延迟调节\n和排障还得自己动手。', 480, 864, 496, 120))
    + text('closing', '装修搁置：这七七八八的东西也太多了。\n25 年 AI 破局：搭好骨架，实测自己抠。', 72, 1184, 936, 84, 28, 42)
    + pageNumber(2, 5, 1312));

  add('a', 3, 'bedtime-to-desk-journey',
    title('买多了的无线开关：\n随手放书房当测试键')
    + art('A-moon-light-curtain', 232, 416, 616, 200, '0 0 336 160', moonCurtain)
    + text('bedtime', '睡觉时想一键入眠（顺手关灯、关窗帘），\n结果买开关的时候不小心买多了。', 72, 640, 936, 120)
    + art('A-surplus-connector', 72, 432, 936, 624, '0 0 936 624', '<path stroke-width="3" d="M864 160 C920 256 912 376 384 376 C344 376 324 416 312 432"/>')
    + group('study-test', art('A-desk-test-button', 104, 872, 304, 176, '0 0 376 224', deskButton)
      + text('test-origin', '多出来的一个没处安放，\n随手放在书房桌边，\n连 Node-RED 当测试键。', 480, 848, 496, 180))
    + text('idle-action', '从 Node-RED 里随便连了一条流当平时调试用的测试键，\n「长按」动作刚好闲置。', 72, 1184, 936, 84, 28, 42)
    + pageNumber(3, 5, 1312));

  add('a', 4, 'mijia-five-steps-versus-long-press',
    title('夏天的神来之笔：\n闲置长按 → 盲开空调')
    + group('remote-and-phone', art('A-shared-remote', 104, 448, 96, 128, '0 0 96 128', '<rect x="22" y="4" width="52" height="116" rx="14" stroke-dasharray="8 10"/><path d="M38 38 H58 M38 58 H58 M38 78 H58"/>')
      + text('shared-remote', '只剩一个\n空调遥控器', 232, 448, 280, 120)
      + art('A-phone-thread', 80, 652, 8, 416, '0 0 8 416', '<path stroke-width="3" opacity=".35" d="M4 4 V412"/>')
      + steps.map((step, i) => text(`step-${i + 1}`, `${i + 1}  ${step}`, 104, 640 + i * 96, 408, 60)).join(''))
    + group('idle-action-on', art('A-node-red-fold', 704, 456, 96, 80, '0 0 240 180', aFold)
      + text('binding', '在 Node-RED 里\n把闲置「长按」\n接上书房空调。', 608, 592, 368, 180)
      + art('A-button', 608, 816, 136, 160, '0 0 240 280', aButton)
      + art('A-air', 792, 816, 176, 144, '0 0 280 180', aAir)
      + text('press-result', '长按 → 盲开空调', 608, 1008, 368, 60))
    + text('on-semantics', '掏手机 → 解锁 → 打开米家 App → 找到书房 → 点开空调，实在太麻烦。\n长按一下听见「滴」声出风，零心智负担。', 72, 1184, 936, 84, 28, 42)
    + pageNumber(4, 5, 1312));

  const principles = [
    ['搭好骨架，实测自己抠', 'AI 帮写 YAML、搭初步 Node-RED 流；\n实机测试、延迟调节和排障自己动手。'],
    ['买多了的无线开关当测试键', '睡前一键入眠开关买多了，\n随手放书房当测试键。'],
    ['每次坐进书房，其实只需要「开」', '把闲置「长按」接上书房空调，\n听见「滴」声出风，零心智负担。'],
  ];
  add('a', 5, 'open-causal-principles',
    title('搭好骨架实测自己抠，\n长按一下零心智负担')
    + principles.map(([heading, body], i) => {
      const y = 416 + 248 * i;
      return group(`principle-${i + 1}`, art(`A-principle-dash-${i + 1}`, 72, y, 120, 6, '0 0 120 6', '<path d="M3 3 H117"/>')
        + text(`principle-number-${i + 1}`, `0${i + 1}`, 72, y + 24, 120, 112, 80, 96, { weight: 700, color: '#355E3B' })
        + text(`principle-heading-${i + 1}`, heading, 232, y + 24, 744, 60, 40, 60, { weight: 600 })
        + text(`principle-body-${i + 1}`, body, 232, y + 96, 744, 120));
    }).join('')
    + text('household-scope', '常用温度、模式固定；睡眠／离家场景收尾关停。\n这里只讲真实生活记录，不提供自动化配置。', 72, 1184, 936, 84, 28, 42)
    + pageNumber(5, 5, 1312));

  add('b', 1, 'full-room-spare-switch-cover',
    image('study-room.png', bg1, 0, 0, 1080, 1440, 'cover', '0')
    + '<div class="mask" style="left:0;top:0;width:1080px;height:480px;background:linear-gradient(to bottom,#FFF7EC 0px,#FFF7EC 328px,transparent 480px)"></div>'
    + '<div class="mask" style="left:0;top:1040px;width:1080px;height:400px;background:linear-gradient(to bottom,transparent 0px,#FFF7EC 128px,#FFF7EC 400px)"></div>'
    + title('买多了的无线开关，\n随手放书房当测试键')
    + text('closing', '夏天的神来之笔：闲置长按 → 盲开空调，\n长按一下听见「滴」声出风，零心智负担。', 72, 1176, 936, 120)
    + pageNumber(1, 5, 1312));

  add('b', 2, 'paper-origin-tall-ai-scene',
    title('25 年 AI 破局：\n搭好骨架，实测自己抠')
    + group('origin-prose', text('renovation', '装修想装 NAS，\nHA / Node-RED\n门槛高，就先搁置。', 72, 432, 456, 180)
      + text('year', '25 年，有了 AI。', 72, 656, 456, 60)
      + text('ai-skeleton', '25 年 AI 帮写 YAML，\n搭初步 Node-RED 流，\n终于把骨架先搭好。', 72, 748, 456, 180)
      + text('manual-testing', '实机测试、延迟调节\n和排障还得自己抠。', 72, 992, 456, 120))
    + image('study-room.png', bg1, 600, 416, 408, 704, 'contain')
    + text('closing', '装修搁置：这七七八八的东西也太多了。\n25 年 AI 破局：搭好骨架，实测自己抠。', 72, 1184, 936, 84, 28, 42)
    + pageNumber(2, 5, 1312));

  add('b', 3, 'ai-hand-bedtime-desk-timeline',
    title('买多了的无线开关：\n随手放书房当测试键')
    + image('press-button.png', bg2, 72, 416, 480, 696, 'contain')
    + art('B-bedtime-moon-curtain', 616, 416, 376, 160, '0 0 336 160', moonCurtain, '#34271D')
    + text('bedtime', '睡觉想一键入眠：\n顺手关灯、关窗帘，\n无线开关买多了。', 600, 624, 408, 180)
    + art('B-desk-test-button', 616, 840, 368, 112, '0 0 376 224', deskButton, '#34271D')
    + text('test-origin', '随手放书房桌边，\nNode-RED 测试键。', 600, 992, 408, 120)
    + text('idle-action', '买多了的无线开关：随手放书房当测试键。\n从 Node-RED 连条流当调试键，「长按」动作刚好闲置。', 72, 1184, 936, 84, 28, 42)
    + pageNumber(3, 5, 1312));

  add('b', 4, 'mijia-trail-opposed-oval-press',
    title('夏天的神来之笔：\n闲置长按 → 盲开空调')
    + group('summer-trail', text('shared-remote', '夏天书房要开空调，\n只剩一个空调遥控器。', 72, 416, 456, 120)
      + art('B-path', 72, 612, 24, 432, '0 0 24 432', '<path stroke-width="3" d="M12 8 C2 38 22 70 12 100 S2 162 12 192 S22 254 12 284 S2 346 12 376"/>', '#80512E')
      + steps.map((step, i) => text(`step-${i + 1}`, step, 120, 608 + i * 92, 408, 60)).join('')
      + text('binding', '在 Node-RED 里绑定闲置长按', 72, 1080, 456, 42, 28, 42))
    + image('press-button.png', bg2, 600, 416, 408, 696, 'contain', '50%')
    + group('press-symbol', art('B-press', 600, 1152, 80, 80, '0 0 240 240', bPress, '#34271D')
      + text('press-label', '长按 → 盲开', 704, 1172, 304, 60))
    + text('on-semantics', '每次坐进书房只需要「开」，\n听见「滴」声出风，零心智负担。', 72, 1184, 456, 84, 28, 42)
    + pageNumber(4, 5, 1312));

  add('b', 5, 'wide-room-subtraction-closing',
    image('study-room.png', bg1, 72, 96, 936, 624, 'contain')
    + art('B-breeze', 72, 352, 360, 180, '0 0 360 180', bBreeze, '#80512E')
    + '<div class="mask" style="left:72px;top:608px;width:936px;height:160px;background:linear-gradient(to bottom,transparent,#FFF7EC)"></div>'
    + title('每次坐进书房，\n其实只需要「开」就行', 80, 96, 192, sans, 832)
    + text('on-only', '闲置长按 -> 盲开空调，听见「滴」声出风。', 72, 1088, 936, 60)
    + text('household-scope', '掏手机 → 解锁 → 打开米家 App → 找到书房 → 点开空调，实在太麻烦。\n常用温度、模式固定，睡眠／离家场景收尾关停，不附部署配置。', 72, 1184, 936, 84, 28, 42)
    + pageNumber(5, 5, 1312));

  add('c', 1, 'renovation-ai-human-three-comics',
    title('装修时想玩全屋智能，\n这七七八八也太多了', 80, 96, 192, serif)
    + group('renovation-panel', art('C-nas-frame', 72, 416, 400, 416, '0 0 400 416', '<path d="M3 3 L397 9 L393 413 L5 409 Z" fill="#FFFAEE"/>', '#493C32')
      + text('renovation', '装修想装 NAS，\nHA / Node-RED\n门槛高，搁置。', 104, 448, 336, 189, 42, 63)
      + art('C-nas-high-step', 144, 672, 240, 112, '0 0 256 144', nasBox, '#493C32'))
    + group('ai-panel', art('C-ai-frame', 504, 464, 504, 368, '0 0 504 368', '<path d="M3 7 L501 3 L496 365 L8 361 Z" fill="#FFFAEE"/>', '#493C32')
      + text('ai-skeleton', '25 年，有了 AI。\n帮写 YAML 配置，\n搭初步流程骨架。', 536, 496, 440, 189, 42, 63)
      + text('skeleton-label', '初步 Node-RED 流', 536, 744, 304, 42, 28, 42)
      + art('C-ai-document-skeleton', 856, 720, 104, 80, '0 0 240 180', `${aFold}<path stroke-width="3" d="M48 48 H132 M48 84 H168 M48 120 H132"/>`, '#493C32'))
    + group('human-panel', art('C-human-frame', 72, 864, 936, 256, '0 0 936 256', '<path d="M3 5 L933 3 L929 253 L7 249 Z" fill="#FFFAEE"/>', '#493C32')
      + text('manual-testing', '实机测试、延迟调节\n和排障还得自己动手。', 104, 896, 528, 126, 42, 63)
      + text('human-caption', '25 年 AI 破局：搭好骨架，实测自己抠', 104, 1056, 528, 42, 28, 42)
      + art('C-human-wrench', 720, 880, 232, 184, '0 0 240 224', wrench, '#493C32'))
    + text('closing', '装修搁置：这七七八八的东西也太多了。\n25 年 AI 破局：搭好骨架，实测自己抠。', 72, 1184, 936, 84, 28, 42)
    + pageNumber(1, 5, 1312));

  add('c', 2, 'bedtime-surplus-desk-fork',
    title('买多了的无线开关：\n随手放书房当测试键', 80, 96, 192, serif)
    + art('C-moon-light-curtain', 72, 432, 400, 176, '0 0 336 160', moonCurtain, '#493C32')
    + text('bedtime', '睡觉一键入眠，\n顺手关灯、关窗帘。\n无线开关买多了。', 72, 656, 408, 189, 42, 63)
    + art('C-desk-test-button', 568, 432, 440, 264, '0 0 376 224', deskButton, '#493C32')
    + art('C-testing-fork', 496, 464, 48, 520, '0 0 48 520', '<path stroke-dasharray="8 10" d="M4 12 Q40 100 24 256 Q8 384 40 508"/>', '#C17460')
    + text('test-origin', '随手放书房桌边，\n连进 Node-RED，\n当平时调试的测试键。', 568, 752, 440, 189, 42, 63)
    + text('test-label', '买多了的无线开关：随手放书房当测试键。', 72, 1040, 936, 42, 28, 42)
    + text('closing', '从 Node-RED 连了一条流当测试键，「长按」动作刚好闲置。', 72, 1184, 936, 84, 28, 42)
    + pageNumber(2, 5, 1312));

  const nodes = [[252, 624], [804, 624], [804, 808], [252, 808], [252, 992]];
  add('c', 3, 'shared-remote-connected-mijia-maze',
    title('米家 App 开空调，\n每次都要走完五步', 80, 96, 192, serif)
    + text('shared-remote', '到了夏天书房需要开空调，家里偏偏只剩一个空调遥控器了。', 72, 336, 936, 42, 28, 42)
    + art('C-search-sofa', 72, 416, 360, 126, '0 0 528 184', cSofa, '#493C32')
    + art('C-phone', 720, 416, 160, 126, '0 0 240 180', cPhone, '#493C32')
    + art('C-serpentine-path', 72, 552, 936, 568, '0 0 936 568',
      '<path stroke="#C17460" d="M180 72 C324 60 568 84 732 72 C918 64 918 262 732 256 C556 262 352 244 180 256 C6 250 6 440 180 440 C372 428 528 456 732 440"/><path stroke="#789080" d="M716 424 Q754 400 780 426 M726 444 Q762 420 794 444"/><g fill="#FFF4DE"><circle cx="180" cy="72" r="28"/><circle cx="732" cy="72" r="28"/><circle cx="732" cy="256" r="28"/><circle cx="180" cy="256" r="28"/><circle cx="180" cy="440" r="28"/></g>', '#493C32')
    + nodes.map(([x, y], i) => group(`step-node-${i + 1}`, text(`step-number-${i + 1}`, `${i + 1}`, x - 20, y - 21, 40, 42, 28, 42, { align: 'center' })
      + text(`step-${i + 1}`, steps[i], x - 148, y + 36, 296, 63, 42, 63, { align: 'center' }))).join('')
    + text('closing', '掏手机 → 解锁 → 打开米家 App → 找到书房 → 点开空调，\n每次都要走完这一串，实在太麻烦了。', 72, 1184, 936, 84, 28, 42)
    + pageNumber(3, 5, 1312));

  add('c', 4, 'idle-long-press-quiet-on-scene',
    title('夏天的神来之笔：\n闲置长按 → 盲开空调', 80, 96, 192, serif)
    + text('binding', '在 Node-RED 里把闲置「长按」\n接上书房空调（闲置长按 -> 盲开空调）。', 72, 336, 936, 126, 42, 63)
    + group('single-press-scene', art('C-node-red-fold', 632, 560, 96, 64, '0 0 240 180', aFold, '#493C32')
      + art('C-button', 320, 680, 300, 264, '0 0 300 264', cButton, '#493C32')
      + art('C-pressing-hand', 128, 744, 352, 272, '0 0 352 272', hand, '#493C32')
      + art('C-contact-arcs', 432, 714, 80, 44, '0 0 80 44', '<path d="M8 30 Q26 6 42 12 M54 10 L62 2 M66 28 L78 24"/>', '#C17460')
      + art('C-wind', 720, 528, 240, 176, '0 0 240 176', cWind, '#493C32')
      + art('C-sound-highlight', 732, 752, 128, 36, '0 0 128 36', '<path stroke="#EBC778" opacity=".3" stroke-width="32" d="M18 18 L110 16"/>', '#493C32')
      + text('sound-note', '「滴」声出风', 736, 744, 224, 60, 28, 42))
    + text('on-semantics', '每次坐进书房只需要「开」，不是开关切换。', 72, 1184, 936, 63, 42, 63)
    + pageNumber(4, 5, 1312));

  add('c', 5, 'thread-to-causal-marginalia',
    title('搭好骨架实测自己抠，\n长按一下零心智负担', 80, 96, 192, serif)
    + group('thread-to-button', art('C-thread', 72, 416, 936, 460, '0 0 936 460', '<path d="M48 204 C154 18 358 402 164 338 C12 292 296 70 332 238 C374 386 100 330 164 138 C242 4 408 324 456 234 C524 134 580 252 642 196"/>', '#493C32')
      + art('C-button', 648, 536, 280, 200, '0 0 300 264', cButton, '#493C32'))
    + group('marginalia', text('note-ai', '25 年 AI 破局：搭好骨架，实测自己抠。', 72, 920, 936, 63, 42, 63)
      + text('note-surplus', '买多了的无线开关：随手放书房当测试键。', 72, 1016, 936, 63, 42, 63)
      + text('note-on', '听见「滴」声出风，零心智负担。', 72, 1112, 936, 63, 42, 63))
    + text('household-scope', '温度、模式固定，睡眠／离家收尾关停。', 72, 1208, 936, 42, 28, 42)
    + pageNumber(5, 5, 1312));
  return cards;
}

module.exports = { buildCards, text, shell };
