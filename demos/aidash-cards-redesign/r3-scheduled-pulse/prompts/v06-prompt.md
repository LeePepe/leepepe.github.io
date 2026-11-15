# v06 · 三耳索引纸封 (topology-tabbed-manila-jacket)

## 1. Visual Metaphor & Archetype Lock
让一只Manila文件封拥有三个突出索引耳，而不是三张重复卡。第一耳「每分/5分脉搏」指向三张快纸，第二耳「04:00/04:15 日批」指向两张慢纸，第三耳「五段回执」抽出底部结果笺；封面开一扇圆形环窗。VS-002账本结构配CL-002暖象牙，CP-002的SWWallet遮挡、DV-003分段环、MI-006滑动纸张组成macOS26候选R3-ManilaJacket。X轴是索引耳和单任务选择，Y轴为两页共享封面槽与第三耳回执，Z轴为实封皮→薄纸→袋唇→少量功能chrome。Things 3借鉴文案密度，CleanShot X借鉴短操作，Alcove借鉴圆凹边；纸封是材质隐喻，不造额外文件管理功能。

## 2. Single P0 Focus & Initial Showcase State
首屏第二耳被压下，slow-page-slot前纸为个人数仓晨报，04:01完成，是唯一P0。环窗中心5/5并标注「阶段通过」，与这条晨报关联；该纸不再打印另一个巨大5/5。每日学习推荐仍在慢页第二行显示04:15已投递3题。快页三个名字露在左侧纸头索引，每个只显示一次，当前纸内标题也只有一次。bottom-receipt-slip默认缩为44px拉手；「五段回执」耳有按钮但未激活。展示时钟11月15日04:15，所有latest time来自固定资料。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract
三耳不等于三条路由，只有快/慢两张任务page；第三耳只打开已有receipt。P1是节律耳与非活动纸头，P2是任务操作和结果笺细节。manila-cover初始包含fast-page-slot三job、slow-page-slot两job以及cutout里的五circle，bottom slip初始就有五段表与三题表；节点必须永久挂载。耳按钮改--cover-page和class，不用innerHTML、outerHTML、replaceChildren、insertAdjacentHTML。折起的正文用inert/aria-hidden以及translate留在封内，外露纸头单独可focus；选中作业就地展开，不另复制selected-detail面板。当前selection只有一个job ID，回执展开时保留它但收起正文以让空间给纸笺。Esc先把第三耳收回并恢复按钮焦点，再归并当前展开条；点击ring stage等价于开第三耳并选原有stage行。

## 4. Measured Layout & 1280x800 Viewport Geometry
1280x800里，封体1080x624px置(100,88)，含索引耳的完整边界不能超出此矩形；外部空白34.19%，>=22%。24px内距后1032x576内容：jacket-tabs44px，16px间隔，manila-cover408px，16px间隔，bottom-receipt-slip92px。cover内20px padding，圆窗168x168在右上，快/慢两个槽共享824px纸区并在Z上叠放，纸头和活动行排在剩余368px高：慢页64+144px、快页三条44px，余28px空气。打开底笺时cover缩244px、slip增256px，页面只露五个40px纸头；底笺五stage置左448px，三question右448px，gap24、每行32/40px。窗口r=62px但命中区不由圆洞裁掉；封唇内凹r20px/depth14px，纸角16px，外角26px。控制耳40px高，其他32px，最小28x28px；字体13/15/20/30px，短数值至少64px槽且不ellipsis。peek的上抬要在44px耳区以外的安全间隔里预留6px，阴影与focus不会被clip-path切去。任何开闭态必须0px unintended scroll overflow，不能用页面隐藏overflow抵消错误。

## 5. Dual-Theme Surface Polarity & Liquid Glass / Paper-Pocket Craft
纸封Light使用desk #F5F1E8、jacket #ECE3D3、paper #FFFCF5、ink #32342D、muted #606256、accent #465D43、success #2C6548、warn #8B590B、focus #0868C5；Dark为#141A15、#273126、#354335、#F5F5EB、#C6CEBE、#BED5AF、#A9DDB5、#EDC785、#99C6FF。前封与纸窗都实心，Manila只表现温度和厚度，不用纸纹位图。凹唇独立Shape切圆口，边内加0.5px高光（#FFFFFFC9浅 / #FFFFFF28深）；ambient shadow浅色0 1px 3px #303A270A、0 9px 20px #303A2710、0 23px 40px #303A2716，深色同形#00000018/#00000028/#00000034。三个索引耳仅活动按钮允许薄功能玻璃：IOR1.5、bevel8px、blur6px、saturation135%、specular0.5px；Safari/reduced-transparency统一用jacket全实底，封皮和任务纸不使用玻璃。time、5/5、3/3与14s启用tabular-nums，深色accent按钮配深desk字，禁止五环段五彩染纸。

## 6. Apple Native Spring Physics & Micro-Interactions
文件纸从封口上移28px，结果笺从底槽抽出164px，用480ms cubic-bezier(0.22, 1.35, 0.36, 1)完成；封面本身不翻转，三个耳通过scaleY(0.96)按下再settle。纸头hover做translateY(-6px) peek，移开归位；预览不自动改页。圆窗为160x160 SVG，center80/r56/stroke6，五个circle pathLength100，stroke-dasharray="16 84"，offset0/-20/-40/-60/-80、stroke-linecap="round"，统一-90°起点。悬停/键盘focus只照亮局部弧，点击把对应既有stage行标亮并展开底笺。立即运行给当前行已有status写已排队→运行中→刚刚完成 · 耗时14s，运行未结束前disabled，finish回调以锁定job ID存内存且不会在切耳时丢失；不联系真实scheduler、Linear或CloudKit。prefers-reduced-motion: reduce关闭peek/纸移/耳按压超调，用直接位置与120ms opacity代替；读数与反馈不减少。

## 7. Production Data Inventory & Exact DOM Topology
封内资料卡的ID与出厂文案锁死如下：

| 封槽 | 产品文案及周期 | 底层ID | 最近成功 |
|---|---|---|---|
| fast 1 | Linear @bot 桥接 · 每 1 分钟 | linear-bot-bridge | 04:14 |
| fast 2 | 我的 PR · 每 5 分钟 | my-pr-supervisor | 04:10 |
| fast 3 | PR 自动审查 · 每 5 分钟 | pr-auto-review | 04:10 |
| slow 1 | 个人数仓晨报 · 每日 04:00 | aidata-digest | 04:01 / 阶段5/5 |
| slow 2 | 每日学习推荐 · 每日 04:15 | daily-learning | 04:15 / 三题送达 |

五段回执的行必须按collect「① 个人源采集」、normalize_merge「② L2-L3 入仓」、retro_roi「③ Retro-ROI」、learning_topics「④ 学习寻题」、digest_push「⑤ Brief 投递」排列，均通过。底笺另一栏是学习送达记录，写Linear TIA / 已投递3题，三题按：如何用证据区分实现缺陷与规格缺口？；怎样区分 Cache 命中率与上下文占比？；如何让增量入仓保持幂等？。题干为离线探索固定代表输入，不能补假TIA编号、网络链接或每stage完成时间；学习本身不能被塑造成五阶段任务。

DOM采用menu与封面article的独有关系，索引耳由原生button实现。图标24x24 inline SVG以currentColor/1.5px圆角线绘制，圆窗不是图片，五segment必须有可读名称的有效按钮覆盖层。

```html
<main class="jacket-card topology-tabbed-manila-jacket">
  <section class="content">
    <menu class="jacket-tabs"><li><button class="fast-index"></button></li><li><button class="slow-index"></button></li><li><button class="receipt-index"></button></li></menu>
    <article class="manila-cover">
      <div class="cover-cutout-ring"><svg class="window-stage-ring"></svg><output></output><p class="window-caption"></p></div>
      <div class="fast-page-slot"><h2></h2><div data-job="linear-bot-bridge"></div><div data-job="my-pr-supervisor"></div><div data-job="pr-auto-review"></div></div>
      <div class="slow-page-slot"><h2></h2><div data-job="aidata-digest"></div><div data-job="daily-learning"></div></div>
    </article>
    <section class="bottom-receipt-slip"><button class="slip-handle"></button><div class="slip-columns"><ol class="jacket-digest-stages"></ol><ol class="jacket-learning-questions"></ol></div></section>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets
此封禁止.caustic-veil、.ruler、Active/Matte bars、<select>测试切换、沙盒免责声明、五点orbital星图与innerHTML节点置换。不能用全封磨砂glass替代solid Manila，不能把三耳误造三个业务页面，不能让圆窗crop命中目标。主题、窗口框和画廊切换都在外层，不加inner control bar。

验收四态：I 第二耳/晨报/5/5/底笺归槽；II 第一耳/PR自动审查选中，两个慢纸头不重复；III 由第三耳打开笺并点环②，五段和三题完整，Esc回耳；IV 当前作业立即运行，排队→运行→完成可见且跨耳后仍归原job。以四态×Light/Dark的1280x800实际WebKit截图验证零溢出、0pxscroll、tabular读数完整与4.5:1文本。快慢slots、5job、5circle和slip的初始Element引用必须未变；补keyboard/Reduce Motion与raw localization key检查。此文件交付Stage1设计，不代替Writer的真实像素证据。
