# v08 · 两层五签药柜 (topology-apothecaries-five-slips)

## 1. Visual Metaphor & Archetype Lock
把五个作业放进两层窄抽屉胸柜：上层三只分钟纸抽、下层两只日批纸抽，右边只设一个验看井，容纳分段环和展开的结果账。这一变体强调「逐抽屉挑选」与右侧检视，既不是五点星图也不是五块平铺仪表。VS-002触感账册、CL-002象牙/森林，CP-002提供纸袋层而非灰底table，DV-003提供精密环，MI-006保证独立抽屉过渡。X=两层抽签同一selection，Y=右验看井收纳详情，Z=每签前唇与内纸真实相扣。参考SWWallet的厚度、Things3的名称清晰、CleanShot X的单工具焦点、Alcove的唇口；候选R3-ApothecarySlips面向Native macOS26。

## 2. Single P0 Focus & Initial Showcase State
默认下层晨报抽屉抽出24px，个人数仓晨报标题与04:01完成只留在这只抽签上，它是唯一P0。右验看井的圆印5/5与「晨报阶段」说明响应此记录，上三抽分别露04:14/04:10/04:10；另一下层抽显示每日学习推荐04:15已送3题。右receipt-ledger-box默认缩为40px入口，stage/question正文未暴露。时钟11月15日04:15。右井从不复制selected job name成第二标题，action-strip只提供已有操作「立即运行 / 执行回执」。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract
五只slip全部横向单行排列，但物理上分为fast一层与daily一层，不是同权五个模块；共同占一组胸柜。P1是纸头频率与验看井环，P2是抽签正文及receipt。tier-fast-group初始三job、tier-daily-group初始两job，二者就是永久快慢pages；五环segment、五stage和三question的结构账也初始存在。点击改selectedJobId和--slip-extract，抽签既有button/内容保持对象身份；关账用CSS类和inert收正文，不移除，杜绝innerHTML、outerHTML、replaceChildren、insertAdjacentHTML。所有选择单拥有者，若开账则左侧选中抽签正文回收，只留标题状态，右账成为明细唯一展示处。Esc收账并还焦点，再归抽签；环stage选择与账行data-stage绑定，不生成另一个列表。

## 4. Measured Layout & 1280x800 Viewport Geometry
在1280x800安排1120x624px胸柜、(80,88)，外围留白31.75%，>=22%。padding24使content1072x576，横向tiered-drawer-chest672px +gap24+inspection-well376px。左内距20px，fast组244px、组间24px、daily组268px，合536px；fast题头32、三只56px抽签+2×12px缝=224，余20px留呼吸；daily题头32、两只88px抽签+12px缝=220，余48px供选中24px抽取。右well内20px，ring box160px、gap16、receipt ledger264px、gap16、action strip80px=536px，运行按钮32px+状态行24px不形成卡外底栏。receipt开时固定264px不推高卡：五stage左144px与三question右168px、gap12，stage26px/题48px，标题与内距共72px，能容纳264px。左屉沿x方向抽取最大24px已计入672px范围；凹唇r10px/depth10px，签角14px、胸柜角26px。文本13/15/20/32px，数据槽76px，hit默认32px、签button56px，>=28x28px。ring有效按钮32方。所有动画超调再留8px井内空气，0px unintended scroll overflow是实际WebKit检查项，不能通过ellipsis或隐藏滚动达成。

## 5. Dual-Theme Surface Polarity & Liquid Glass / Paper-Pocket Craft
纸签柜的Light色为desk #F3F1EB、chest #E9E5DB、slip #FFFEF8、ink #30372F、muted #596355、accent #405F46、passed #2D6748、warning #875A0B、focus #086BC9。Dark选择#121A16、#233129、#324438、#F3F6EE、#C2D0BE、#B8D8B7、#A3E0B7、#EFCB88、#90C2FF。五屉使用同样实面，仅当前纸签更亮并带4px插纸错位；相同数据显示不涂五色。每屉有concave semicircle lip而非平直按钮矩形，0.5px inner highlight分别#FFFFFFD2/#FFFFFF2B；浅色多停ambient depth shadow为0 1px 2px #2A38260A, 0 6px 14px #2A382610, 0 18px 32px #2A382616，深色用#00000018/#00000024/#00000032。右井上方只给阶段命中控制玻璃：IOR1.5、bevel8px、blur6px、saturation135%、0.5px specular，Safari与reduced-transparency换chest不透明面，不让图表或receipt成为glass。tabular-nums用于所有时间、5/5、3/3、14s；深色主按钮亮accent配desk字。

## 6. Apple Native Spring Physics & Micro-Interactions
每抽屉只对自己的纸签执行translateX(24px)，440ms cubic-bezier(0.22, 1.35, 0.36, 1)，底屉回收与上屉抽取同时而非新节点换位；hover纸签translateY(-6px) peek，mouseleave归位。右账由248px内井自下向上抽80px，用同曲线500ms，边缘高光随着class加亮。环viewBox160x160、center80/r56、stroke6，五circle以pathLength100和stroke-dasharray="16 84"、offset0/-20/-40/-60/-80精确分段，stroke-linecap="round"、起点-90°。hover高亮一弧但不改selection，click/Enter固定stage并打开原账；中心5/5不被换成5job健康分母。运行从右action-strip对选中的job执行内存反馈：已排队→运行中→刚刚完成 · 耗时14s，running禁重复，回调绑定job ID，换抽屉也不串写。没有实际调度器、CloudKit或Linear连接。prefers-reduced-motion: reduce取消抽取/peek的位移与超调、保留100ms opacity，所有记录照常可读与可操作。

## 7. Production Data Inventory & Exact DOM Topology
上层抽签原始资料是：linear-bot-bridge / Linear @bot 桥接 / 每 1 分钟 / 04:14完成；my-pr-supervisor / 我的 PR / 每 5 分钟 / 04:10完成；pr-auto-review / PR 自动审查 / 每 5 分钟 / 04:10完成。下层资料是aidata-digest / 个人数仓晨报 / 每日 04:00 / 04:01完成且5/5通过，以及daily-learning / 每日学习推荐 / 每日 04:15 / 04:15已投3题。不要把每日3题写成5stage成功。

右账的data-stage依次collect:① 个人源采集、normalize_merge:② L2-L3 入仓、retro_roi:③ Retro-ROI、learning_topics:④ 学习寻题、digest_push:⑤ Brief 投递，状态均通过；不提供未来源证实的每stage时间。学习投递栏「Linear TIA · 已送达3/3」列三题：如何让增量入仓保持幂等？；怎样区分 Cache 命中率与上下文占比？；如何用证据区分实现缺陷与规格缺口？。这是固定代表性问题输入，不是已检索线上issue，不补假TIA编号/链接或写入操作，交接说明不展示在卡面。

左tier和右well是content下两个直接父节点，不塞成book spread。SVG图标24x24、currentColor、round joins/stroke1.6，命中圈与可访问名称独立于细小的绘制弧。

```html
<main class="slip-chest-card topology-apothecaries-five-slips">
  <section class="content">
    <div class="tiered-drawer-chest">
      <section class="tier-fast-group"><h2></h2><article class="horizontal-drawer" data-job="linear-bot-bridge"></article><article class="horizontal-drawer" data-job="my-pr-supervisor"></article><article class="horizontal-drawer" data-job="pr-auto-review"></article></section>
      <section class="tier-daily-group"><h2></h2><article class="horizontal-drawer" data-job="aidata-digest"></article><article class="horizontal-drawer" data-job="daily-learning"></article></section>
    </div>
    <aside class="inspection-well">
      <figure class="ring-gauge-box"><svg></svg><output></output><figcaption></figcaption></figure>
      <article class="receipt-ledger-box"><button class="ledger-pull"></button><div class="ledger-paper"><ol class="inspection-stage-proof"></ol><ol class="inspection-question-proof"></ol></div></article>
      <footer class="action-strip"><button class="run-selected-slip"></button><p aria-live="polite"></p><time></time></footer>
    </aside>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets
药柜不允许.caustic-veil、.ruler、Active/Matte bars、<select>测试开关、沙盒免责copy、五点orbital星图或innerHTML替换对象。禁将五签做五个大号equal KPI、右井重复左侧选中标题、卡外固定bottom CTA。画廊、viewport、theme均归外层chooser，右井只是业务回执检视。

四态为首屏下层晨报抽24/环5/5/账闭，换上层桥接并让其他4签归位，开账选④完整看到5stage+3question并Esc收账，最后当前job立即运行经过排队→运行→完成且能跨层保留状态。交付时每态Light/Dark共8张实际WebKit1280x800截图与持久DOM对象记录；五job、两tier page、五circle和账必须同一批Element。验证28px命中、keyboard、Reduce Motion、>=4.5:1文字、0px意外横纵scroll、零数字…与raw localization key。Stage1不生成HTML，以上像素门禁留给Stage2，不虚报PASS。
