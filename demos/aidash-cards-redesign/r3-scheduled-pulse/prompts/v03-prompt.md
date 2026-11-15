# v03 · 檐下脉搏匣 (topology-alcove-tray-console)

## 1. Visual Metaphor & Archetype Lock
以 Alcove 式短檐作入口，下面不是星图，而是一座有纸袋的桌面工作匣。短檐里嵌小环与快慢袋的切换，左列承载任务纸，窄中列显示当前阶段释义，右列是一张横向侧滑的回执票。选 VS-007 Swiss Chrono、CL-008 Alabaster/Navy；CP-002 控制纸袋厚度，DV-003 提供五分段仪表语义，MI-006 管抽取过渡。坐标 X＝单任务就地选择，Y＝fast/slow共享纸列占地并留出另一页纸头，Z＝檐口压住后纸、前纸从中抽出。SWWallet 是叠卡来源、Things 3 是文案留白来源、CleanShot X 是短工具栏来源，Alcove 只供内凹收口观察。候选 R3-AlcoveConsole 不改变 AIDash 其他页面；目标外形为 Native macOS 26。

## 2. Single P0 Focus & Initial Showcase State
首屏檐口选「高频脉搏 3」，左纸列的 PR 自动审查成为唯一选中条，04:10完成、每5分钟；下方慢页纸头仍露晨报与学习的独立标题，五名字没有重复。檐内环中心5/5，caption「晨报阶段 · 04:01」负责解释独立digest记录。中列默认仅写「全部阶段通过」，不摊开五站。右票券收为一条48px纸边，露「执行回执」，未显示问题正文。时间固定11月15日04:15，不能把04:10的PR记录假装刚运行完成；只有用户手动触发后才出现新反馈。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract
檐上的快慢按钮是两页的展示优先级，不是新导航路由。P1为未激活页的可读纸头与五段caption，P2为选中行操作、段释义和侧票。job-pocket-column内两页在初始DOM就有全部5 job rows；ticket-slide-vault中的5阶段记录和3个学习问题同样常驻，SVG五段也不能点击才生成。层叠用 transform/opacity、class 与--page-lift，隐藏正文 inert，保持可点击露出的标题独立不被inert祖先包住。禁止 innerHTML、outerHTML、replaceChildren、insertAdjacentHTML；文本叶和aria状态可以更新。page切换选其已存在的上次任务，卡中只有一个selectedJobId；点击环段把currentStageId绑定到原有dl条目及票上对应行。Esc先收票、再清除段高亮，选择保持，返回原命中按钮。

## 4. Measured Layout & 1280x800 Viewport Geometry
此匣固定1088x608px，位置(96,96)，视口空闲35.40%满足>=22% whitespace。24px padding后content1040x560，alcove-lip-dock高80，间隔24，workspace-split高456。split网格为job-pocket-column 560px、stage-ring-column 168px、ticket-slide-vault 264px，中间两段24px；环在dock用104x104预留重叠，仅向匣内伸24px，不向视口出界。左列顶部64px留页控距离，快页三条48px，选中增为120px，慢页双标题各44px，总不超过400px；选慢页时逆转这两种展开量。票展开占右264px宽，不横跨任务字；5阶段行28px、3题两行40px，标题与留白总420px。stage列只显示一条释义和阶段按钮，不复制完整回执。凹檐半径18px、深12px，纸口r=12px、depth12px，外框r=24px。字阶13/15/20/28px，列内左右padding16px，数值独立最少64px宽；控制32px、环按钮32x32px，底线>=28x28px。票的x位移只能在自身vault内，阴影与focus outline算入安全区；预期所有操作后0px unintended scroll overflow，不能通过缩成11px小字躲避长CJK。

## 5. Dual-Theme Surface Polarity & Liquid Glass / Paper-Pocket Craft
檐匣 Light：canvas #F0F3F8、tray #E7ECF3、sheet #FFFFFF、text #253049、subtext #5A6680、tint #4C59BE、ok #27684D、warn #88580F、focus #086ACC；Dark：#0E131F、#1C273A、#2C3A50、#EFF4FF、#B8C6DC、#B7C2FF、#9DDEBF、#EBC989、#85BFFF。这套CL-008取纸白/海军蓝极性，不让任务内容成为毛玻璃。檐唇前层用真实concave cut-out与一层0.5px inner highlight（Light #FFFFFFE6，Dark #FFFFFF30），下面环境影从0 1px 2px #2234550A、0 7px 16px #22345512 到0 20px 36px #22345518；暗影的alpha为18/28/38 hex。纸头背层错4px与8px，看见厚度但没有装饰条纹。仅dock中的page switch允许玻璃，IOR1.5、bevel8px、blur10px、saturation145%、薄边0.5px；Safari与减弱透明使用tray实底，不叠折射层。tabular-nums锁定时刻、5/5、3/3与14s宽度；深色按钮采用亮tint+深canvas字以维持对比。

## 6. Apple Native Spring Physics & Micro-Interactions
檐口切页以440ms cubic-bezier(0.22, 1.35, 0.36, 1)改变已有纸页的translateY，侧票使用同曲线520ms translateX从216px到0，打开时反射边先亮、票身后移，没有独立加载遮罩。纸头hover peek固定translateY(-6px)，票把手可同样上抬但不自动展开。小环采用120x120 SVG、center60、r40、stroke5；五个circle以pathLength100、stroke-dasharray="16 84"与offset0/-20/-40/-60/-80围成一圈，stroke-linecap="round"，-90°统一起点。环段hover亮起并更新既有释义文本，pointerleave回选中段；click/Enter固定选择并开票。立即运行在对应行的常驻live output依次显示已排队、运行中、刚刚完成 · 耗时14s，运行阶段保留按钮但禁用，离线计时回调按job ID写入内存，不请求宿主服务。prefers-reduced-motion: reduce将这些抽页/抽票变成100ms无位移淡入，关闭peek及环亮度脉动，不丢失状态或恢复入口。

## 7. Production Data Inventory & Exact DOM Topology
檐匣字段如下，两个节律组不可混为五个同频任务：

- 快页① linear-bot-bridge → Linear @bot 桥接 / 每 1 分钟 / 04:14 完成。
- 快页② my-pr-supervisor → 我的 PR / 每 5 分钟 / 04:10 完成。
- 快页③ pr-auto-review → PR 自动审查 / 每 5 分钟 / 04:10 完成（初始选中）。
- 慢页① aidata-digest → 个人数仓晨报 / 每日 04:00 / 04:01 完成、5/5。
- 慢页② daily-learning → 每日学习推荐 / 每日 04:15 / 04:15 投递3题。

侧票第一部分的真实stage_id序列为 collect [① 个人源采集]、normalize_merge [② L2-L3 入仓]、retro_roi [③ Retro-ROI]、learning_topics [④ 学习寻题]、digest_push [⑤ Brief 投递]，五项通过，环的每段与此对应。第二部分「Linear TIA · 学习送达3/3」列：如何用证据区分实现缺陷与规格缺口？；如何让增量入仓保持幂等？；怎样区分 Cache 命中率与上下文占比？。问题属于固定代表性选型输入，并非查询到的线上issue；不写假issue编号、虚构链接或未经来源提供的阶段耗时。daily-learning只负责三题交付。

按以下html骨架补足语义button与dl，不把三列压进一个generic wrapper。24x24 inline SVG用currentColor、1.6px圆笔，环本身有摘要label，五个effective hit区有各自名称。

```html
<main class="alcove-card topology-alcove-tray-console">
  <section class="content">
    <section class="alcove-lip-dock"><h1></h1><nav class="pocket-switch"></nav><svg class="alcove-segment-ring"></svg><output></output><time></time></section>
    <div class="workspace-split">
      <div class="job-pocket-column"><section class="fast-pocket-page"><article data-job="linear-bot-bridge"></article><article data-job="my-pr-supervisor"></article><article data-job="pr-auto-review"></article></section><section class="slow-pocket-page"><article data-job="aidata-digest"></article><article data-job="daily-learning"></article></section></div>
      <dl class="stage-ring-column"><dt class="selected-stage-label"></dt><dd class="selected-stage-note"></dd></dl>
      <article class="ticket-slide-vault"><button class="ticket-grip"></button><section class="ticket-body"><ol class="ticket-stages"></ol><ol class="ticket-questions"></ol></section></article>
    </div>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets
不能重演R2 v03的五点orbital布局：这里只保留精细SVG分段环，任务绝不环绕摆放。禁 .caustic-veil、.ruler、Active/Matte bars、<select>内部测试状态、沙盒说明上屏与innerHTML重建。不要给短檐加完整第二标题栏，也不要让收起票的inert覆盖可点击把手；主题和画廊选择交给外层chooser。

四项状态证据为A 首屏快页/PR审查/晨报5/5/侧票闭；B 切慢页并选学习，三张快页标题仍独立可见；C 点环④使侧票完整滑出，五段与三题均能读并Esc回收；D 选中行手动运行，在排队和运行中切页，完成反馈仍属于原job。全部状态要做双主题WebKit1280x800测量和对象身份对照，确认初始节点没有换批、无numeric ellipsis、无l10n key、横纵scroll delta均为0px。再用键盘与Reduce Motion走相同链路；Stage 2实际截图负责证明这些要求，而非本设计文件预宣称通过。
