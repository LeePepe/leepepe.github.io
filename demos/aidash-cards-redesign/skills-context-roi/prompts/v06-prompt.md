# v06 · 五站穿带回溯簿 (topology-causal-passbook-ribbon)

## 1. Visual Metaphor & Archetype Lock

直接精炼R2 v06的全链路回溯：五张开凹口的纸列并排，贝塞尔带穿过纸列上部，底部抽出完整审计凭条。class保留 mandated causal-passbook 名称，但产品文案只写“全链路回溯”，绝不借类名暗示因果。VS-002瑞士账本、CL-002暖纸、CP-002纸袋、IP-003回溯详情和IP-001流带选择；X=五列顺序，Y=各列折页与底审计条，Z=纸列1/流场2/袋口3/抽条4。依据SWWallet/Things vault命中和Owner B-v04/v06、A-v09锚点；Alcove/CleanShot X/Sankey无vault条目，如实视为brief参考。desktop单卡，不交出生产AppTheme冻结。

## 2. Single P0 Focus & Initial Showcase State

首载branch=l1、selectedStage=4/S8-S9；唯一P0为第四列“返工18次”与所选L1带形成的回溯聚焦，不将18归因到L1。第四列口袋正文open，其他四列只露节点与折签；audit-pullout closed，32px把手可見。L1 45%是当前亮带但数值不大于P0 30px返工读数。点stage5抬提案列，点带切stage2并显示定义，底把手抽审计slip，状态不更改固定输入或编造条件数据。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1为五个stage题签与当前带标签，P2为列内证据面和底审计slip。初始HTML必须永久挂载全部SVG <path> ribbons、五个trace stage nodes、完整S1..S12 metric readouts及所有pocket drawers，折叠列不是懒加载模板。CSS classes/variables/transforms、dataset与aria控制打开、收起和高亮；仅已有叶子textContent可变，不用innerHTML/outerHTML/replaceChildren/insertAdjacentHTML或重新插入节点。closed正文inert/aria-hidden，题签仍为32px按钮；5列同一selection owner。hover临时亮带，click/Enter/Space提交；Esc先合底条再归列并回开启题签。重复操作与主题切换都保持node reference稳定。

## 4. Measured Layout & 1280x800 Viewport Geometry

viewport1280x800，main x88/y76/w1104/h648，padding28；content1048x592。外部留白308,608px²=30.1375%>=22%。masthead48、gap16、五列book352、gap16、底slip160总592。五列各200px，4×12px gap；每列title64/流域120/口袋168，文字13px且允许分行，完整skill名与单位不得ellipsis。overlay SVG viewBox="0 0 1048 352"，pointer-events只在独立branch控件上，不能挡stage。底slip160px里全表采用三列指标组，各组≤4读数，每项24px行高；折叠只32px把手露出。最大纸页抽取与hover留在原352/160槽，0px unintended scroll overflow。28x28px为最小命中区，实际用32x32px代理细带。

160px审计条内32px口径签与112px数据区，底16px安全边。原三列指标组仅用于质量等短读数，禁止同时显示十二项全部定义；实践/摩擦/提案/披露都是已挂载data-face，context另拆五片与cache/P95。五片行高20px，其余面最多两项两行20px，inactive组inert。切口径签复用原readout身份，诊断入口先呈质量组；收条归还把手焦点。

五列中的S7局部T80，L0 44px d="M 224,100 C 270,100 300,72 360,72 L 360,116 C 300,116 270,144 224,144 Z"；L1 36px d="M 224,144 C 270,144 300,158 360,158 L 360,194 C 300,194 270,180 224,180 Z"。越界旗于列二侧以独立12px带=15%×80，不与80合并。S11左列五片厚9.6/6.4/12.8/32/19.2共80，cache另80尺77.44/2.56。所有分岔均按 M x0,y0 C x0+36,y0 x1-36,y1 x1,y1 L x1,y1+h C x1-36,y1+h x0+36,y0+h x0,y0+h Z 闭合，flow overlay仅细光轨；后续列边是1px lineage connectors，不把未观测的S7→gate→friction→ROI联系画成可量化因果守恒。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

Light枚举desk #FBF7EF，paper #FFFFFF，pocket #F4EEE4，ink #302A28，muted #6D625B，l0 #3A7053，l1 #705D7D，flag #975635，focus #315B9B；Dark逐项#1B1A20/#28262D/#35313A/#F8F1E9/#C9BCB2/#B5D9BD/#CBB9D8/#E8B093/#A9C7FF。各closed ribbon用linearGradient .22→.58 opacity（0%/100%）和1px specular白rim .50/.20。五列纸袋上口凹8px，16px口边与0.5px inner-white highlight形成同A-v09家族；阴影0 4px 12px #302A2812，边不做表格网格。数字tabular-nums，SF Pro13/16/22，P0 30，图标inline24x24 currentColor/1.6px。实体content opacity1/blur0/displacement0，不应用Liquid Glass；功能popover仅可用单层玻璃并给Safari与Reduce Transparency不透明fallback。对比正文4.5:1，大字3:1。

## 6. Apple Native Spring Physics & Flow Animation

列内抽纸和bottom slip用480ms cubic-bezier(0.22, 1.35, 0.36, 1)，hover题签peek translateY(-6px)，展开offset和peek以CSS变量相加。选中L1中心曲线2px粒子animateMotion 3200ms往复循环，不让粒子在不存在分母的五站间装作同一token旅行。其余列仅静态navigation连线。prefers-reduced-motion: reduce关闭particle、overshoot与hover平移，100ms opacity保留阅读顺序；focus-visible与hover均亮同一branch，快速跨列点击沿当前transform续接，不destroy/create。

## 7. Production Data Inventory & Exact DOM Topology

五stage column依次：1 S11上下文构成（50,000 tok / 96.8%缓存）；2 S7渐进披露分流（L0 55% / L1 45% / 越界15%）；3 S1/S2/S3触发与门禁（命中2/8 · 拦截8/40 · 误报4/40 · 审计9/12）；4 S8/S9返工与逃逸摩擦（返工18次 / 重试6次 / 逃逸3+5）；5 S10提案转化与健康度（my-designer0.4/code-review1.2/team-lead1.8 proposals/100 runs）。第三列定义S1 Pin Drift 2/8 behind，不能把命中短标解释为成功触发；全链路回溯是operational/data lineage，非原因证明。

第一列折页有S11总50,000 tok=100%，五slice全部：System / AGENTS 6,000 tok(12%)、Skills4,000 tok(8%)、Tool schemas8,000 tok(16%)、Tool results20,000 tok(40%)、Conversation12,000 tok(24%)。Cache另外eligible requests分母100,000：缓存命中96.8%即96,800/100,000，未命中重算3.2%即3,200/100,000。第二列S7 L0索引浅读55%与L1局部深读45%，越界全量深读15%独立重叠，不伪造样本总数。第三列S1落后2/8、S2拦截8/40=20%与误报4/40=10%各自标签、S3审计9/12/48 eval cases/本周+6。第四列S8 20会话中18次编辑返工和6次重试不相加，S9 [IMPL_BUG]3/[SPEC_GAP]5。第五列S10三个报告读数，不造货币公式，提案仅查看建议/收藏/稍后/撤销本地状态。底审计条补S4 my-designer40次加载和R1审查证据入口、S6同技能12脚本执行及触达8/40=20%（脚本不是触达分子）、S12 Search P9518,400 tok·120次/7天、S5 暂无统计；条内全S1..S12都有常驻readout，不能空壳引用未加载指标。

```html
<main class="aidash-card topology-causal-passbook-ribbon">
  <section class="content">
    <header class="passbook-masthead"></header>
    <div class="five-column-passbook">
      <section class="stage-column" data-stage="1"><button class="stage-notch-tab"></button><div class="stage-paper-face"></div></section>
      <section class="stage-column" data-stage="2"><button class="stage-notch-tab"></button><div class="stage-paper-face"></div></section>
      <section class="stage-column" data-stage="3"><button class="stage-notch-tab"></button><div class="stage-paper-face"></div></section>
      <section class="stage-column" data-stage="4"><button class="stage-notch-tab"></button><div class="stage-paper-face"></div></section>
      <section class="stage-column" data-stage="5"><button class="stage-notch-tab"></button><div class="stage-paper-face"></div></section>
      <svg class="overlay-ribbon-field" viewBox="0 0 1048 352"><defs></defs><g class="passbook-closed-ribbons"></g><g class="passbook-flow-particles"></g></svg>
    </div>
    <article class="audit-pullout-slip"><button class="audit-tab"></button><dl class="passbook-full-readouts"></dl></article>
  </section>
</main>
```

stage faces、g和dl在初始HTML展开完整内容，不留等待innerHTML的空占位。content禁止通用直接孩子hero、fold-panel、secondary。

## 8. Explicit Anti-Patterns & Verification Targets

严禁stroke-width >24（R2 132/74/58）、55+45+15归一化或把cache96.8%塞成第六slice；因果美元节省、.caustic-veil、.ruler、Active-Matte、<select>测试开关、沙盒免责文案、innerHTML换页均fail。不能用causal类名推销未经证实的因果，也不能真实调度或连接Linear/CloudKit/遥测。

四态双appearance证据：a初载L1/Stage4/返工口袋开且audit收；b键盘选L0并聚焦Stage2，上下支55/45与独立旗仍完整；c第三站读门禁后抽audit，查40 loads/12 scripts/8 touches和S5；d第五站收藏、稍后、撤销、Esc还原stage-tab焦点。1280x800检查0px溢出、overlay不挡按钮、全节点identity不变、数值完整、reduced-motion静态可用。跨所有已在场R3 prompts的非标题段落重叠<=20%是交接complete条件。
