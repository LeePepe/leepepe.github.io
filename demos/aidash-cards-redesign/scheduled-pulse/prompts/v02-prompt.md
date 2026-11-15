# v02 · 装订晨间账 (topology-saddle-ledger-book)

## 1. Visual Metaphor & Archetype Lock
这次不是一摞散纸，而是展开在桌上的骑马订薄册。左叶是三项分钟工作，右叶是两项晨间交付，窄书脊承接一枚阶段环，订缝下方藏一张横向抽出的结果纸。采用 VS-002 Swiss Editorial、CL-002 Warm Ivory，以 CP-002 的 SWWallet 袋层、DV-003 的精密读数和 MI-006 的抽页触感约束制作。X 轴将左叶选中条与右叶陪衬分开，Y 轴把回执折进中央缝，Z 轴使页边、书脊和袋盖真实遮挡。参考 Things 3 的空白边注、SWWallet 的卡层、CleanShot X 的工具紧凑度与 Alcove 的收纳边缘；不复制任何 App 的导航。R3-SaddleLedger 是候选 AppTheme，平台明确为 macOS 26 桌面卡片。

## 2. Single P0 Focus & Initial Showcase State
打开就能读到快慢两页；焦点落在左页「Linear @bot 桥接」原行，最近完成04:14，节律每1分钟，展开的行内区域只提供完成状态和立即运行。它是唯一主角，右页两任务保留摘要。中缝环始终标注「晨报阶段 · 04:01」，中心5/5为 digest 通过数，即使选择分钟任务也不冒充其进度。右页学习条显示已投递3题 / 04:15，时钟为11月15日04:15。gutter-receipt-drawer 首屏关闭、仅有32px订缝拉柄。所有五个名字在两叶各出现一次，书名和回单不再复读当前 job。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract
书页不随点击重建。P1 是页眉的「分钟脉搏 3」「每日批处理 2」与 ring caption；P2 阶段表和学习三题随书脊抽屉取出。五条任务、两张叶页、SVG 五个独立圆段、订缝回执全量初始挂载，close 通过 translateX、opacity 和 inert 收纳，不能依赖插入节点或 display:none 瞬间跳变。只有 selectedJobId 管选择；选中右页时左页当前条还原，细节就地展开，中央读数仍有自己的明确晨报语义。按环段可展开回单并用 class 标出同一个 stage ID。禁止 innerHTML / outerHTML / replaceChildren / insertAdjacentHTML，允许改现有 textContent、aria 属性与 CSS 自定义变量。退回动作关闭抽屉而不清空选中记录，Esc 分两步先关回单、再收行，焦点还给触发控件。

## 4. Measured Layout & 1280x800 Viewport Geometry
纸册在1280x800画框内占 x=88、y=80、1104x640px，周围留白31%，>=22%的空间不被卡面占用。24px外内边距形成1056x592内容；folio-spine-bar 为44px，下面16px空气，book-spread 占440px，再16px间隔与76px抽屉基座，总和592px。spread 三列依次448/136/448px、两个12px沟槽：左叶三个摘要行56px且当前条可扩为144px，右叶两行64px且当前条可扩为176px。书脊 SVG 112x112px，圆心读数28px；页内文字13/15/20px，行距20px。展开回执时将 spread 收为268px、抽屉增为248px，两叶原有操作正文归纸，仅留32px任务头与24px组题头，左叶3头、右叶2头都能落入268px；结果仍在同一个592px框内；抽屉正文按5阶段一列与3题一列各400px，行高32px、题目最多两行。骑马订只画三处1px短缝，不画满页刻度。凹袋口是偏中心 r=12px、深12px的半圆，页角18px、外角28px。任务按钮56px高、运行32px高，环有效选择区32x32px，所有目标不小于28x28px。保证页角阴影、展开端点、焦点环都在册内安全区；WebKit检查 0px unintended scroll overflow，不以裁掉数字来换取尺寸。

## 5. Dual-Theme Surface Polarity & Liquid Glass / Paper-Pocket Craft
账册 Light 色表：desk #F5F1E9、binding #E7E0D4、leaf #FFFCF6、ink #29332D、secondary #59675E、accent #365D48、passed #2D6547、attention #885709、focus #0868C9。Dark 色表配对为 #111A17、#1E2D25、#2D3C33、#F3F5EC、#BDCDBE、#B6D5BB、#A4DDB5、#E9C784、#8FBFFF。左叶偏明纸、右叶不加第二套艳色，页内分组用binding/leaf亮度差而非边框套盒。前袋盖真实切出内凹 lip，0.5px 内高光为浅色 #FFFFFFD9、深色 #FFFFFF2E；多停环境影 Light 为0 2px 3px #25372A0A, 0 10px 22px #25372A10, 0 26px 40px #25372A14，Dark 影 #00000016/#00000024/#00000032。纸页两缘仅有一条折光，不拟真皮革照片。玻璃限于订缝控制：IOR1.5、8px bevel、blur6px、saturation135%、0.5px specular；Safari不支持透射或减弱透明时用binding全实底。5/5、日期、cadence、14s统一 tabular numerals；浅色CTA用白字，深色CTA用desk字，文本实测4.5:1后方可验收。

## 6. Apple Native Spring Physics & Micro-Interactions
选择页内行像翻开短纸签：480ms cubic-bezier(0.22, 1.35, 0.36, 1) 将其抬24px，其他纸条仅让位；书脊回单从左侧缝横移96px并显出正文。悬停页头取 translateY(-6px) peek，不绕书脊做180°翻面。环在128x128 viewBox内以中心64、r=44、stroke5绘制五个 circle，pathLength=100，stroke-dasharray="16 84"，五段 offset 顺序0、-20、-40、-60、-80，stroke-linecap="round"；-90°起点让①在十二点钟。段焦点与hover用局部明度和1px细边响应，点击对应段将回单该行染亮，整环不旋转。运行按钮立刻旁显已排队，350ms后运行中，1400ms后刚刚完成 · 耗时14s；这些是离线时间压缩的反馈过程，不伪造真实经过14秒，也不访问调度器/Linear。任务状态各自保存，运行中防双击。prefers-reduced-motion: reduce 改为无抬升、无peek的120ms淡入，仍能打开书脊抽屉和选择五段。

## 7. Production Data Inventory & Exact DOM Topology
左叶三个订签依次绑定 linear-bot-bridge（Linear @bot 桥接，每 1 分钟，04:14完成）、my-pr-supervisor（我的 PR，每 5 分钟，04:10完成）、pr-auto-review（PR 自动审查，每 5 分钟，04:10完成）。右叶上签是 aidata-digest（个人数仓晨报，每日 04:00，04:01完成且5/5通过），下签是 daily-learning（每日学习推荐，每日 04:15，04:15已投递3题）。节律与完成时间有独立字段，不把每天的任务误写成分钟间隔。

书脊回单采用可定位 definition list：collect 的 term 是① 个人源采集；normalize_merge 对应② L2-L3 入仓；retro_roi 对应③ Retro-ROI；learning_topics 对应④ 学习寻题；digest_push 对应⑤ Brief 投递，definition均为通过。与它并排的学习栏写「Linear · TIA · 已投递3/3」；三个问题按以下次序：怎样区分 Cache 命中率与上下文占比？ / 如何让增量入仓保持幂等？ / 如何用证据区分实现缺陷与规格缺口？。三题作为选型代表内容，不添加未经提供的issue URL、编号或真实写入能力。学习记录只有投递结果，不被塞入digest的五段列表。

DOM须保持书页—铰链—书页关系。SVG工具图标24x24、currentColor、stroke1.5、round join，装订装饰 aria-hidden；interactive ring 配五个有明确阶段名称的原生按钮命中层。

```html
<main class="ledger-card topology-saddle-ledger-book">
  <section class="content">
    <nav class="folio-spine-bar"><h1></h1><time></time><button class="spine-grip"></button></nav>
    <div class="book-spread">
      <section class="left-leaf"><h2></h2><ol class="minute-signatures"><li data-job="linear-bot-bridge"></li><li data-job="my-pr-supervisor"></li><li data-job="pr-auto-review"></li></ol></section>
      <figure class="center-ring-hinge"><svg class="digest-dial"></svg><figcaption></figcaption><output></output></figure>
      <section class="right-leaf"><h2></h2><ol class="daily-signatures"><li data-job="aidata-digest"></li><li data-job="daily-learning"></li></ol></section>
    </div>
    <aside class="gutter-receipt-drawer"><button class="drawer-return"></button><dl class="bound-stage-receipt"></dl><ol class="bound-learning-receipt"></ol></aside>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets
书脊设计不许 .caustic-veil、不许 .ruler；Active/Matte bars、<select>状态测试器、沙盒免责声明都不得上屏。废除五点 orbital canvas 与任何 innerHTML 替换式翻页，拒绝用大范围旋转把文字倒置。也不能把中央环放大到压过左叶 P0，或加一个卡外悬浮底部 action bar。Chooser的theme/gallery/bezel控制仍归外层。

验收取四个状态而非四个按钮截图：①首次加载左桥接展开、书脊5/5、回执闭合；②换到右页每日学习且左页恢复摘要；③由环②抽出订缝回单，五段及三题完整，按Esc回原按钮；④选中任务立即运行，已排队/运行中/完成均可观察且切页不串结果。每状态双主题截图、1280x800实际WebKit边界、keyboard与Reduce Motion测试。节点身份快照应证明五任务、两叶、五环段及回单始终同一批 Element；无数值…、无 raw localization keys、无多余滚动。Stage 1交付的只是已指定设计，渲染凭据由后续Writer生成。
