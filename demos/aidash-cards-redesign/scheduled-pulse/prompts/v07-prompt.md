# v07 · 悬桌双抽屉 (topology-floating-dock-drawers)

## 1. Visual Metaphor & Archetype Lock
CleanShot式紧凑utility card在桌上轻浮，下面两只纸袋左右并列，中央一枚小环印章把两种节律接起来，整宽的结果抽屉从底部推出。目标是可抓住的纸工具，不是dock应用启动器。VS-005 Zen Paper与CL-006 Sky/Sage候选色，CP-002保留SWWallet纸层，DV-003用于可选分段环，MI-006用于双抽屉滑动。X=左右两袋内一次只选一条，Y=下方满宽回执折叠，Z=utility control→纸头→袋盖→实底四层。参考Things3留白、Alcove圆凹切口和CleanShot X细小工具栏，R3-FloatingDrawers属于macOS26单卡探索坐标，不能生成新的dock或导航页。

## 2. Single P0 Focus & Initial Showcase State
第一眼是右袋的每日学习推荐：其行内显示3题已送达、04:15完成，是唯一展开的作业。同袋的个人数仓晨报摘要04:01完成，左袋三分钟job只显示紧凑纸头。桥心ring为5/5，caption「晨报阶段」避免把它当学习的五阶段；时钟11月15日04:15。receipt-drawer-shell采用永久section，默认只有40px拉手「执行回执」，没有初始化就摊开的八行。左右页始终存在，两组标题「高频脉搏 3」「每日批处理 2」都可读；任务名只留在自己的纸头，不放到utility-bar或drawer标题。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract
这里用满宽回单而不是两袋各塞一份细节。P1为cadence、最近时间和桥心摘要；P2为当前行操作和底层五阶段/三题清单。所有minute-pocket三条、daily-pocket两条、两页节点、五个SVG段以及整个receipt-drawer-shell正文初始就挂载。open class驱动--drawer-depth与原纸层transform，不能用innerHTML、outerHTML、replaceChildren、insertAdjacentHTML替换Element，也不在展开时create新的receipt。不可见正文设inert/aria-hidden，露出的选中按钮不被inert祖先封死。状态只由一个selectedJobId统管；打开回单时收当前行正文而不重复任务名，ring segment以stage ID联动原有行。receipt button具有aria-controls/expanded，Esc关屉并focus回它，纸袋选择保留。

## 4. Measured Layout & 1280x800 Viewport Geometry
1280x800中主卡1040x608px、x120/y96，桌面留白38.25%达到>=22%。卡padding24，content992x560，由utility-bar40、gap20、twin-pockets-bridge356、gap20、receipt-shell124组成。桥区三列420/112/420px，两个20pxgap；左右袋padding16，左3纸头48px且最多一行展开136px，右2纸头56px且最多一行展开176px，均在324px内。底抽屉打开时桥高212、shell268，其余不变；两袋只露左3×48与右2×56摘要。回单内容left440+gap24+right440px，五段28px行、三题40px行，标题与padding56px可容纳。主卡r28px、纸角16px，唇中央凹口r14/depth14px。正常目标32px，grabber40px高，ring按钮32x32px，最小>=28x28px；字号13/15/20/32px。底屉不是position:fixed bar，所有抽取都在卡内分配的终态矩形内，超调与-6px peek预留8px安全空位。要求0px unintended scroll overflow、完整focus描边，禁止隐藏body滚动来掩饰外溢。

## 5. Dual-Theme Surface Polarity & Liquid Glass / Paper-Pocket Craft
R3-FloatingDrawers Light tokens：desk #F2F4F6、pocket #E7ECF0、insert #FFFFFF、ink #293446、secondary #5E697A、accent #285EAA、done #276A4D、attention #86540C、focus #0869CE；Dark分别#111922、#202D3B、#314255、#F3F7FE、#C1CEE0、#ADCFFF、#A2DFBD、#F2C985、#8BBEFF。实纸是高亮L2、内袋为较暗L1，状态色只在文本/细环，不涂满袋。唇用两段圆角边接内凹圆口，独立front-lip层带0.5px内高光Light #FFFFFFD8 / Dark #FFFFFF2A；环境影0 2px 4px #1A2A420A, 0 10px 24px #1A2A4212, 0 28px 44px #1A2A4214，暗影#00000018/#00000028/#00000034。utility-bar仅小范围按钮chrome可玻璃：IOR1.5、bevel8px、blur8px、saturation140%、specular0.5px；Safari/reduced-transparency回退pocket实色，不采样另一层glass。5/5、3题、时间与14s使用tabular numerals，dark亮accent的CTA上用深desk字保障对比。

## 6. Apple Native Spring Physics & Micro-Interactions
双袋纸抽动为460ms、全宽结果屉为520ms，都用cubic-bezier(0.22, 1.35, 0.36, 1)，只移动已有对象的transform与CSS变量。hover只给当前纸头translateY(-6px) peek，不把另一袋拖起；打开receipt把当前纸操作收回并升起144px结果纸，卡边界完全静止。中央SVG ring的viewBox144、center72/r48、stroke5.5，每circle pathLength100、stroke-dasharray="16 84"、offset0/-20/-40/-60/-80、stroke-linecap="round"，以-90°开圈。局部弧highlight在hover/focus出现，点击或Enter选段并滚动零距离地照亮底屉该行，不出现orbital job。立即运行在所属row的aria-live按已排队→运行中→刚刚完成 · 耗时14s推进；running期间button disabled，切到另一袋依然按原job ID落回状态。仅使用离线内存计时，绝不发真实scheduler/Linear调用。prefers-reduced-motion: reduce不移动纸、不开弹性或peek，使用120ms淡入及终态尺寸；所有明细与操作保持可用。

## 7. Production Data Inventory & Exact DOM Topology
左右纸袋分工严格按原产品五作业，不额外添第六项：minute-pocket装linear-bot-bridge（Linear @bot 桥接；每 1 分钟；04:14完成）、my-pr-supervisor（我的 PR；每 5 分钟；04:10完成）、pr-auto-review（PR 自动审查；每 5 分钟；04:10完成）。daily-pocket装aidata-digest（个人数仓晨报；每日 04:00；04:01完成/五段通过）与daily-learning（每日学习推荐；每日 04:15；04:15完成/三题送达）。

全宽屉中的「晨报阶段 · 5/5」区域按collect → ① 个人源采集，normalize_merge → ② L2-L3 入仓，retro_roi → ③ Retro-ROI，learning_topics → ④ 学习寻题，digest_push → ⑤ Brief 投递依次通过。另一边「学习投递 · Linear TIA · 3/3」的问题按怎样区分 Cache 命中率与上下文占比？、如何让增量入仓保持幂等？、如何用证据区分实现缺陷与规格缺口？排列。三题是本轮代表性选型文案，不提供编造的线上issue ID/链接或每阶段duration；不把学习任务当digest的复本。

下列section版本避免details的原生瞬时display切换中断弹性；button语义负责open与close。内联工具SVG24x24/currentColor/1.6px round stroke，ring必须含5常驻circle及命名点击目标。

```html
<main class="utility-card topology-floating-dock-drawers">
  <section class="content">
    <header class="utility-bar"><h1></h1><time></time><span class="utility-feedback" aria-live="polite"></span></header>
    <div class="twin-pockets-bridge">
      <section class="minute-pocket"><h2></h2><ul class="minute-paper-list"><li data-job="linear-bot-bridge"></li><li data-job="my-pr-supervisor"></li><li data-job="pr-auto-review"></li></ul></section>
      <div class="medallion-column"><svg class="bridge-ring"></svg><output></output><p class="bridge-caption"></p></div>
      <section class="daily-pocket"><h2></h2><ul class="daily-paper-list"><li data-job="aidata-digest"></li><li data-job="daily-learning"></li></ul></section>
    </div>
    <section class="receipt-drawer-shell"><button class="wide-drawer-handle"></button><div class="wide-receipt-paper"><ol class="drawer-digest-list"></ol><ol class="drawer-question-list"></ol></div></section>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets
实纸双袋禁.caustic-veil、.ruler、Active/Matte bars、<select>测试器、沙盒免责声明、五点orbital排列以及innerHTML式重建。桥心不能画粗巨环抢右袋3题的P0；不能用bottom-dock隐喻增加一条macOS浮动操作栏；不要让工具bar复制外层theme/gallery/viewport controls。

四态取证：A初始右学习行/3题、bridge5/5、底屉闭；B换到左侧我的PR，两袋只此一行展开；C把满宽回执展开，点环③，五stage与三question完整且Esc归位；D对当前job运行，排队/运行/完成均反馈，跨袋不丢任务状态。Writer需交4×2主题WebKit1280x800截图、Element持久性快照和键盘/Reduce Motion结果。截图应实证0px unintended scroll、无数值ellipsis、无raw localization keys、文本4.5:1与命中28px底线；Stage1没有HTML，不能宣称这类rendering门禁已经通过。
