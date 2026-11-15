# v09 · 瑞士三页通行袋 (topology-swiss-passbook-pocket)

## 1. Visual Metaphor & Archetype Lock
以Owner选择的v09纸袋为主骨，把快页、慢页、执行回执三张插页收入一本Swiss passbook。前面内凹唇承担两页切换与分段圆印，三张纸依深度滑出，而不是三个横向门户。VS-002 Swiss Tactile Wallet与CL-008克制靛蓝组合，CP-002的SWWallet叠层、DV-003精密环、MI-006 spring构成R3-SwissPassbook候选主题。X=快慢页选择和该页单job，Y=第三张回执插页按需取出，Z=底纸/前纸/凹唇/功能切页control。Things3和CleanShot X负责清楚而短的操作，Alcove提供凹唇灵感；平台是Native macOS26，不造passbook业务功能。

## 2. Single P0 Focus & Initial Showcase State
初始前纸是「日批页」，其中个人数仓晨报就地展开，04:01阶段通过。唇上的ring中心5/5、caption「晨报阶段」，当前纸不再重复巨大读数。日批第二头为每日学习推荐、04:15已投递3题；后面的高频页露三个名字与节律。前纸与后纸共五个任务名各出现一次，passbook title和action bar不复读。第三插页「执行回执单」只露44px拉头，没有五段/三题正文。时钟固定11月15日04:15，唯一P0是前纸所选作业而不是票据或仪表。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract
insert-slots内必须从初始parse起就有三个section：fast insert三job、daily insert两job、receipt insert含五stage和三question；ring五个circle也要在初始HTML挂好。第三insert是既有详情，不是第三个任务page。P1留在纸头的cadence/latest与唇印，P2由插页抽取暴露；选新job只展开原行，不复制内容到another inspector。用--active-insert、class、dataset、CSS transform切深度，隐藏正文inert但露头button仍可focus；严格禁止innerHTML、outerHTML、replaceChildren、insertAdjacentHTML与交互后再创建卡。selectedJobId唯一，receipt打开时当前作业缩正文，纸头名保持可读。Esc先送回receipt并返回其拉手，然后收任务；ring段点击取回执并选已有同stage行，hover不更换job。

## 4. Measured Layout & 1280x800 Viewport Geometry
护照袋占1064x648px，左108/上76，外部未覆盖32.67%符合>=22% whitespace。padding24后content1016x600，passbook-frame填满它；frame里notched-lip-front高120，insert-slots高400，footer action-bar高48，两个16px留缝=600。ring-stamp-panel是front-lip右侧168x120px的定位兄弟，位置预留在lip而不压到页签；唇左848px放标题与快慢控。slots中四个未选job纸头40px、活动正文160px，另有receipt头44px和36px抽取安全空位，总400px；三页内部都永久存在。receipt打开后slots顶部40px将快/慢两组paper-head并排，各含32px页按钮；五job正文和任务头暂收在原页内并设inert，仍可经页按钮关闭回执返回任务。下方360px专供receipt横向两栏（每440px，gap24），不与任务字重叠。card r28、insert r18，中心唇notch r22px/depth16px，左右斜角12px；controls32px、拉柄44px、ring命中36px，全部>=28x28px。UI字号13/15/20/32，数值单位紧邻且独立保留宽。每张纸translate的终态与超调要计入既有400pxslots，不靠overflow:hidden裁掉内容；1280x800必须0px unintended scroll overflow。

## 5. Dual-Theme Surface Polarity & Liquid Glass / Paper-Pocket Craft
通行袋Light tokens为desk #F3F2EE、frame #E8E8E2、insert #FFFEFA、ink #2B3140、muted #596270、accent #4E5AB6、passed #2B664B、warning #85550D、focus #0968CD；Dark为#111722、#202B3C、#303E52、#F2F5FC、#BFCBDE、#BBC3FF、#A3DDBB、#EECB88、#8BBEFF。纸页实底、前唇实底，亮度层级取代厚框；可见后纸错4/8px保持SWWallet tactile depth。front lip用真实凹切圆弧与斜接，两侧边缘0.5px内高光Light #FFFFFFDA / Dark #FFFFFF2B；ambient影三停0 1px 3px #25324A0A, 0 9px 20px #25324A12, 0 25px 44px #25324A18，Dark#00000018/#0000002A/#00000038。只有快慢switch是玻璃chrome，IOR1.5、bevel10px、blur8px、saturation140%、0.5px rim；Safari/reduced-transparency落为frame不透明，不对纸施折射。读数5/5、3题、time与14s统一tabular-nums，Dark明accent按钮用深desk文字，状态只占小面积。

## 6. Apple Native Spring Physics & Micro-Interactions
插页切换以500ms cubic-bezier(0.22, 1.35, 0.36, 1)将当前纸上抬32px，背页只退8px、12px，前唇不随纸飘；receipt沿同样轴抽出160px，用520ms，阴影随--extract-depth变化。hover纸头严格translateY(-6px) peek，焦点只加轮廓而非强制动画。ring viewBox160、center80/r56/stroke6，五circle用pathLength100、stroke-dasharray="16 84"、dashoffset0/-20/-40/-60/-80、stroke-linecap="round"，-90°起点；hover/focus亮弧，click/Enter高亮既有stage行并揭receipt，环绝不带五个绕圈job。立即运行就在passbook-action-bar旁已有live region显示已排队→运行中→刚刚完成 · 耗时14s，运行未完禁重复，反馈绑定原job并在切页时保留。仅内存时间推进，无真实调度器/CloudKit/Linear读写。prefers-reduced-motion: reduce关闭spring overshoot、peek、纸位移，120ms opacity与固定终态维持全部操作和数据。

## 7. Production Data Inventory & Exact DOM Topology
高频插页的三行按照ID线性排布：linear-bot-bridge → Linear @bot 桥接， 每 1 分钟，04:14成功；my-pr-supervisor → 我的 PR， 每 5 分钟，04:10成功；pr-auto-review → PR 自动审查， 每 5 分钟，04:10成功。日批插页为aidata-digest → 个人数仓晨报， 每日 04:00，04:01完成、5/5；daily-learning → 每日学习推荐， 每日 04:15，04:15完成、三题投递。这些显示名不再沿用R1旧名。

回执插页左侧保留五个阶段source ID：collect（① 个人源采集）、normalize_merge（② L2-L3 入仓）、retro_roi（③ Retro-ROI）、learning_topics（④ 学习寻题）、digest_push（⑤ Brief 投递），统一通过。右侧学习列显示「Linear TIA · 已投递3/3」，三条题目顺序为如何用证据区分实现缺陷与规格缺口？、如何让增量入仓保持幂等？、怎样区分 Cache 命中率与上下文占比？。三题是固定代表性选型输入，不是从私有Linear读回的issue；不编TIA编号、假链接、阶段耗时，learning不能冒充五stage流程。

轮廓中三section插页必须是insert-slots的直属子节点。ring-stamp-panel虽是frame下的aside，视觉对齐前唇右边。24x24 inline SVG工具图标用currentColor、1.6pxround stroke，五个环命中按钮明确标识阶段。

```html
<main class="passbook-card topology-swiss-passbook-pocket">
  <section class="content">
    <article class="passbook-frame">
      <header class="notched-lip-front"><h1></h1><nav class="passbook-page-switch"></nav><time></time></header>
      <div class="insert-slots">
        <section class="fast-passbook-insert"><h2></h2><div data-job="linear-bot-bridge"></div><div data-job="my-pr-supervisor"></div><div data-job="pr-auto-review"></div></section>
        <section class="daily-passbook-insert"><h2></h2><div data-job="aidata-digest"></div><div data-job="daily-learning"></div></section>
        <section class="receipt-passbook-insert"><button class="passbook-receipt-grip"></button><div class="receipt-passbook-columns"><ol class="passbook-stage-list"></ol><ol class="passbook-question-list"></ol></div></section>
      </div>
      <aside class="ring-stamp-panel"><svg class="passbook-stage-stamp"></svg><output></output><p class="stamp-caption"></p></aside>
      <footer class="passbook-action-bar"><button class="run-passbook-job"></button><p aria-live="polite"></p></footer>
    </article>
  </section>
</main>
```

## 8. Explicit Anti-Patterns & Verification Targets
禁止.caustic-veil、.ruler、Active/Matte bars、<select>测试页切换、沙盒免责copy、五点orbital星图和innerHTML node replacement。不得仅给普通列表加钱包阴影自称SWWallet，不得为了三insert造第三页产品导航，action-bar不能离卡成为macOS浮动底栏；theme/bezel/gallery只属于外层chooser。

核验四状态：0日批晨报为前纸/5/5/回执头缩；1切快页选我的PR，仅这条展开且五名字各一次；2抽第三纸并点环⑤，5stage+3question完整、Esc回插页柄；3当前任务立即运行，排队、运行、完成逐步出现并能切页保持状态。Writer交4states×2appearance的WebKit1280x800实截，以及五job、两任务页、五circle、第三receipt的相同Element引用证据。测试键盘/Reduce Motion、28px最低命中、4.5:1文字、零数值…、无raw localization key与0px意外scroll。这里只交设计Prompt，不声称已经实现或渲染通过。
