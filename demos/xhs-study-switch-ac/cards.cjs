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
  const add = (style, n, topology, body) => cards.push({
    id: `${style}-${String(n).padStart(2, '0')}`, style, number: n, topology,
    html: shell(style, topology, body),
  });

  add('a', 1, 'asymmetric-three-modules',
    group('heading', title('空调遥控器丢了之后，\n我做了一个\n最爽的决定', 68, 84, 252)
      + text('subtitle', '少一个遥控器，\n多一次顺手的肌肉记忆', 72, 380, 936, 120, 40, 60, { color: '#566056' }))
    + group('wireless-button', panel('button-paper', 72, 536, 352, 608, '#FFFCF6')
      + art('A-button', 132, 616, 232, 264, '0 0 240 280', aButton)
      + text('button-caption', '手边已有的\n无线按键', 104, 960, 288, 120))
    + group('air-illustration', panel('air-wash', 448, 536, 560, 352, '#E5EADC')
      + art('A-air', 496, 592, 208, 120, '0 0 280 180', aAir)
      + text('illustrative-temperature', '24℃', 736, 680, 224, 96, 72, 88, { weight: 700, color: '#355E3B' })
      + text('temperature-qualifier', '温度示意，不是作者配置', 496, 800, 464, 42, 28, 42, { color: '#566056' }))
    + group('on-only', panel('on-paper', 448, 912, 560, 232, '#FFFCF6')
      + art('A-on-accent', 464, 956, 6, 120, '0 0 6 120', '<path d="M3 3 V117"/>')
      + text('on-copy', '长按一下\n只负责打开空调', 480, 956, 496, 120))
    + group('footer', text('series', '书房里的减法设计', 72, 1304, 760, 42, 28, 42, { color: '#566056' }) + pageNumber(1, 5, 1304)));

  const searchScenes = [
    '<path d="M20 80 H220 V160"/>',
    '<rect x="20" y="80" width="94" height="80" rx="20"/><rect x="126" y="80" width="94" height="80" rx="20"/>',
    '<path d="M20 80 H220 M40 80 V160 M200 80 V160"/>',
  ];
  add('a', 2, 'unequal-pain-columns',
    title('只是想吹个风，\n前戏为什么这么长？', 64, 80, 160)
    + group('search-column', panel('search-paper', 72, 344, 352, 736, '#FFFCF6')
      + text('search-heading', '找遥控器', 104, 384, 288, 60)
      + searchScenes.map((scene, i) => art(`A-search-${i + 1}`, 128, 472 + i * 180, 240, 96, '0 0 240 180',
        `${scene}<rect x="82" y="30" width="76" height="132" rx="14" stroke-dasharray="8 10"/>`)
        + text(`search-place-${i + 1}`, ['桌面', '沙发缝', '床头'][i], 104, 584 + i * 180, 288, 60)).join(''))
    + group('phone-journey', panel('phone-paper', 448, 344, 560, 736, '#FFFCF6')
      + text('phone-heading', '拿手机也要绕一下', 480, 384, 496, 60)
      + art('A-step-thread', 480, 468, 18, 488, '0 0 18 488', '<path stroke-width="3" opacity=".35" d="M9 8 V480"/>')
      + ['拿手机', '解锁', '进 App', '找书房', '点开机'].map((step, i) => text(`step-${i + 1}`, `${i + 1}  ${step}`, 512, 460 + i * 112, 464, 84)).join(''))
    + text('closing', '明明只想开空调，\n注意力却先跑去找东西。', 72, 1160, 936, 120)
    + pageNumber(2, 5, 1304));

  add('a', 3, 'single-open-editorial',
    title('为什么不做单击调温、\n双击切模式？', 64, 80, 160)
    + group('single-intent', panel('open-wash', 72, 368, 936, 592, '#E5EADC')
      + text('open-hero', '开', 136, 456, 304, 248, 192, 208, { weight: 700, color: '#355E3B' })
      + text('intent', '每次坐进书房，\n我其实只需要\n把空调打开。', 520, 448, 420, 240))
    + text('on-semantics', '常用温度和模式，不必每次重调。\n不猜当前状态，也不做组合选择。\n长按 = 开空调，不是开关切换。', 72, 1016, 936, 180)
    + text('rhetorical-qualifier', '原文用「99%」形容高频意图。\n这是修辞，不是测量数据。', 72, 1232, 816, 84, 28, 42, { color: '#566056' })
    + pageNumber(3, 5, 1312));

  add('a', 4, 'backstage-and-fingertip',
    title('复杂度在背后\n确定性在指尖')
    + group('backstage', art('A-backstage-folds', 104, 360, 872, 152, '0 0 872 152',
      `<path stroke-width="3" d="M0 146 H872"/><g transform="translate(72 0) scale(.35)">${aFold}</g><g transform="translate(396 0) scale(.35)">${aFold}</g><g transform="translate(728 0) scale(.35)">${aFold}</g>`)
      + text('tool-nas', '绿联 NAS', 104, 456, 248, 60)
      + text('tool-ha', 'Home Assistant', 376, 456, 336, 60)
      + text('tool-node-red', 'Node-RED', 752, 456, 224, 60)
      + text('conceptual-tools', '原文提到的幕后工具', 104, 536, 872, 60))
    + group('fingertip', panel('fingertip-wash', 72, 708, 936, 452, '#E5EADC')
      + art('A-button', 128, 772, 232, 264, '0 0 240 280', aButton)
      + art('A-finger', 104, 784, 192, 232, '0 0 192 232', '<path d="M8 220 L78 132 Q88 119 103 125 L135 138 Q153 142 163 132 Q171 120 155 110 L105 79 Q83 68 68 82 L8 134" fill="#F5F0E6"/>')
      + text('press-result', '长按 → 开空调\n「滴」一声出风', 424, 812, 520, 144, 48, 72, { weight: 600, color: '#355E3B' }))
    + text('household-scope', '关停由原文中的离开书房、睡眠／离家场景收尾。\n这里只解释作者的使用方式，不提供自动化配置。', 72, 1216, 936, 84, 28, 42, { color: '#566056' })
    + pageNumber(4, 5, 1312));

  const principles = [
    ['痛点长在生活裂缝里', '遥控器少了一个，\n但我现在就想开空调。'],
    ['最高频的动作，砍掉分支', '想打开时，\n就不必先做一道选择题。'],
    ['复杂留在背后，确定留在指尖', '不用低头看屏幕，\n长按，听见「滴」，就结束。'],
  ];
  add('a', 5, 'open-three-principles',
    title('好工具\n先替我做减法')
    + principles.map(([heading, body], i) => {
      const y = 360 + 288 * i;
      return group(`principle-${i + 1}`, art(`A-principle-dash-${i + 1}`, 72, y, 120, 6, '0 0 120 6', '<path d="M3 3 H117"/>')
        + text(`principle-number-${i + 1}`, `0${i + 1}`, 72, y + 24, 120, 112, 80, 96, { weight: 700, color: '#355E3B' })
        + text(`principle-heading-${i + 1}`, heading, 232, y + 24, 744, 60, 40, 60, { weight: 600 })
        + text(`principle-body-${i + 1}`, body, 232, y + 88, 744, 120));
    }).join('')
    + group('footer', text('series', '少一个遥控器，多一次顺手的肌肉记忆', 72, 1280, 760, 42, 28, 42, { color: '#566056' }) + pageNumber(5, 5, 1280)));

  add('b', 1, 'full-ai-cover',
    image('study-room.png', bg1, 0, 0, 1080, 1440, 'cover', '0')
    + '<div class="mask" style="left:0;top:0;width:1080px;height:480px;background:linear-gradient(to bottom,#FFF7EC 0px,#FFF7EC 328px,transparent 480px)"></div>'
    + '<div class="mask" style="left:0;top:1040px;width:1080px;height:400px;background:linear-gradient(to bottom,transparent 0px,#FFF7EC 128px,#FFF7EC 400px)"></div>'
    + title('遥控器不见了\n书房多了个长按')
    + text('closing', '长按手边的按键。\n空调打开，听到「滴」。', 72, 1176, 936, 120)
    + pageNumber(1, 4));

  add('b', 2, 'left-journey-right-ai',
    title('只是想吹个风\n却先分了心')
    + group('phone-journey', text('phone-heading', '找不到遥控器时', 72, 384, 396, 60)
      + art('B-path', 72, 484, 32, 496, '0 0 96 496', '<path stroke-width="3" d="M48 40 C16 76 80 108 48 144 S16 212 48 248 S80 316 48 352 S16 420 48 456"/><g fill="currentColor"><circle cx="48" cy="40" r="7"/><circle cx="48" cy="144" r="7"/><circle cx="48" cy="248" r="7"/><circle cx="48" cy="352" r="7"/><circle cx="48" cy="456" r="7"/></g>', '#80512E')
      + ['拿手机', '解锁', '进 App', '找书房', '点开机'].map((step, i) => text(`step-${i + 1}`, step, 120, 488 + i * 104, 348, 80)).join(''))
    + image('press-button.png', bg2, 516, 376, 492, 724, 'contain')
    + text('closing', '手机当然能开。\n我只是想让这件事更顺手。', 72, 1168, 936, 120)
    + pageNumber(2, 4));

  add('b', 3, 'left-prose-right-oval-ai',
    title('每次坐下\n其实只需要开')
    + group('intent-prose', text('fixed-settings', '常用温度和模式，\n不必每次再调。', 72, 432, 456, 126, 42, 63)
      + text('on-only-prose', '不做单击调温、\n双击切模式的组合。\n长按，只负责打开。', 72, 582, 456, 189, 42, 63))
    + image('press-button.png', bg2, 600, 376, 408, 696, 'contain', '50%')
    + group('press-symbol', art('B-press', 600, 1088, 80, 80, '0 0 240 240', bPress, '#34271D')
      + text('press-label', '长按 → 开', 704, 1108, 304, 60))
    + text('closing', '不用猜当前状态，再做一道选择题。', 72, 1184, 936, 84)
    + pageNumber(3, 4));

  add('b', 4, 'wide-ai-scene-closing-prose',
    image('study-room.png', bg1, 72, 80, 936, 664, 'contain')
    + art('B-breeze', 72, 352, 360, 180, '0 0 360 180', bBreeze, '#80512E')
    + '<div class="mask" style="left:72px;top:632px;width:936px;height:160px;background:linear-gradient(to bottom,transparent,#FFF7EC)"></div>'
    + title('好工具\n不是让我选更多\n而是少找一次', 72, 88, 264, sans, 832)
    + text('closing', '复杂度藏在背后。\n确定性留在指尖。', 72, 1144, 936, 120)
    + pageNumber(4, 4));

  add('c', 1, 'staggered-search-comic',
    title('我只是想开空调\n却先找起了东西', 80, 96, 192, serif)
    + group('search-panel', art('C-search-frame', 72, 360, 600, 416, '0 0 600 416', '<path d="M3 3 L597 9 L593 413 L5 409 Z" fill="#FFFAEE"/>', '#493C32')
      + text('search-copy', '桌面上找找，\n沙发缝里再看看。', 104, 400, 528, 126, 42, 63)
      + art('C-search-sofa', 104, 556, 528, 184, '0 0 528 184', cSofa, '#493C32'))
    + art('C-gaze-connector', 104, 784, 264, 248, '0 0 264 248', '<path d="M160 6 C20 48 28 194 256 224"/>', '#C17460')
    + group('phone-panel', art('C-phone-frame', 384, 808, 624, 356, '0 0 624 356', '<path d="M3 7 L621 3 L616 353 L8 349 Z" fill="#FFFAEE"/>', '#493C32')
      + text('phone-copy', '找不到的话，\n就拿起手机。', 416, 840, 560, 126, 42, 63)
      + art('C-phone', 536, 992, 280, 140, '0 0 240 180', cPhone, '#493C32'))
    + text('closing', '麻烦不大，分心很真。', 72, 1232, 816, 84, 42, 63)
    + pageNumber(1, 4, 1312));

  const nodes = [[252, 440], [804, 440], [804, 664], [252, 664], [252, 888]];
  add('c', 2, 'connected-serpentine-five-steps',
    title('想吹个风\n还要先走一小圈', 80, 96, 192, serif)
    + art('C-serpentine-path', 72, 352, 936, 744, '0 0 936 744',
      `<path stroke="#C17460" d="M180 88 C324 76 568 100 732 88 C918 80 918 318 732 312 C556 318 352 300 180 312 C6 306 6 536 180 536 C372 524 528 552 732 536"/>
      <path stroke="#789080" d="M716 520 Q754 496 780 522 M726 540 Q762 516 794 540 M730 558 Q768 536 788 558"/>
      <g fill="#FFF4DE"><circle cx="180" cy="88" r="28"/><circle cx="732" cy="88" r="28"/><circle cx="732" cy="312" r="28"/><circle cx="180" cy="312" r="28"/><circle cx="180" cy="536" r="28"/></g>`, '#493C32')
    + nodes.map(([x, y], i) => group(`step-node-${i + 1}`,
      text(`step-number-${i + 1}`, `${i + 1}`, x - 20, y - 21, 40, 42, 28, 42, { align: 'center' })
      + text(`step-${i + 1}`, ['拿手机', '解锁', '进 App', '找书房', '点开机'][i], x - 148, y + 36, 296, 63, 42, 63, { align: 'center' }))).join('')
    + text('closing', '手机没做错。\n我只是想少走几步。', 72, 1152, 936, 126, 42, 63)
    + pageNumber(2, 4, 1312));

  add('c', 3, 'quiet-hand-press-and-breeze',
    title('长按，滴——', 88, 106, 106, serif, 112)
    + text('subtitle', '空调开了，事情就结束了。', 72, 264, 936, 84, 42, 63)
    + group('single-press-scene', art('C-button', 320, 616, 300, 264, '0 0 300 264', cButton, '#493C32')
      + art('C-pressing-hand', 128, 680, 352, 272, '0 0 352 272', '<path d="M6 208 L84 124 C98 109 116 100 140 94 L292 30 Q312 20 331 22 Q348 23 348 35 Q350 46 332 52 L236 89 Q244 96 252 105 Q262 122 246 139 Q256 159 235 174 Q241 198 216 213 L163 246 Q145 258 112 258 L6 264" fill="#FFFAEE"/><path stroke-width="3" d="M152 176 L216 124 M176 200 L238 150"/>', '#493C32')
      + art('C-contact-arcs', 432, 650, 80, 44, '0 0 80 44', '<path d="M8 30 Q26 6 42 12 M54 10 L62 2 M66 28 L78 24"/>', '#C17460')
      + art('C-wind', 720, 480, 240, 176, '0 0 240 176', cWind, '#493C32')
      + art('C-sound-highlight', 732, 704, 128, 36, '0 0 128 36', '<path stroke="#EBC778" opacity=".3" stroke-width="32" d="M18 18 L110 16"/>', '#493C32')
      + text('sound-note', '滴——', 736, 696, 224, 60, 28, 42))
    + text('on-semantics', '不是开关切换，也不加调温组合。\n这一下，只负责把空调打开。', 72, 1144, 936, 126, 42, 63)
    + pageNumber(3, 4, 1312));

  add('c', 4, 'tangled-thread-open-marginalia',
    title('好工具\n替我少做一道选择', 80, 96, 192, serif)
    + group('thread-to-button', art('C-thread', 72, 400, 936, 460, '0 0 936 460', '<path d="M48 204 C154 18 358 402 164 338 C12 292 296 70 332 238 C374 386 100 330 164 138 C242 4 408 324 456 234 C524 134 580 252 642 196"/>', '#493C32')
      + art('C-button', 648, 520, 280, 200, '0 0 300 264', cButton, '#493C32'))
    + group('marginalia', text('note-pain', '从丢一个遥控器的痛点开始。', 72, 928, 936, 84, 42, 63)
      + text('note-subtraction', '为最常用的动作，做一点减法。', 72, 1028, 936, 84, 42, 63)
      + art('C-note-highlight', 72, 1144, 714, 44, '0 0 714 44', '<path stroke="#EBC778" opacity=".25" stroke-width="38" d="M22 22 L692 20"/>', '#493C32')
      + text('note-certainty', '复杂留在后面，顺手留在眼前。', 72, 1128, 936, 84, 42, 63))
    + text('series', '少一个遥控器，多一次顺手的肌肉记忆', 72, 1272, 816, 42, 28, 42)
    + pageNumber(4, 4, 1312));

  return cards;
}

module.exports = { buildCards, text, shell };
