# v05 · 回溯仪表双抽柜 (topology-trace-matrix-cabinet)

## 1. Visual Metaphor & Archetype Lock

用一个偏心55/45仪表柜让左脊的五步回溯决定右侧哪只证据抽屉被照亮。这里55/45仅是柜体布局比例，不混同S7统计尺。VS-007、CL-008，组合IP-003原位详情、IP-001图带联动、CP-002实体纸袋；X=五节点选择，Y=左长脊与右上下双bay，Z=柜0/凹口2/抽页3。参考Linear的有序读数、SWWallet的嵌入式纸页及R2全链路回溯。Vault的SWWallet/Things匹配可引用；Alcove/CleanShot X/Sankey没有匹配，具体柜体是本轮独立组合。只做desktop/macOS卡片提示，不增管理功能。

## 2. Single P0 Focus & Initial Showcase State

P0设为cache-hit的96.8%闭合带，activeBranch=cache-hit、selectedStage=1/S11；顶部右抽屉context open=true、下抽屉gates-roi closed，露36px标签。96.8%读数24px，其余普通13px，左站一selected。切Stage2选L0，Stage3打开下抽屉门禁面、Stage4打开摩擦面、Stage5打开提案面；顶/底正文互斥激活但都常驻。不将cache当context的第六条，也不把下游摩擦数量按命中率筛分。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

P1在spine只给紧凑节点与分母标，P2为双drawer及柜底口径slip。全体SVG <path> ribbons、5 trace stage nodes、S1..S12 metric readouts和所有pocket drawers在初始load就永久挂载。右bay不能以innerHTML/outerHTML/replaceChildren/insertAdjacentHTML重建正文，禁止销毁旧panel再生成；仅用class、dataset、CSS变量、transform与已有叶子textContent。inactive正文设置inert/aria-hidden并保留标签按钮，selected节点aria-current。hover临时亮支不提交，Enter/Space与click同步；Esc关最近drawer还焦点，反复选择不会改变Element identity。S5缺失读数与零值必须可区分。

## 4. Measured Layout & 1280x800 Viewport Geometry

窗1280x800；main x88 y76 w1104 h648/padding28，content1048x592，外留白308,608px²=30.1375%（>=22%）。cabinet-split-frame宽1048，沟16，余1032分配55%＝567.6px spine、45%＝464.4px bay。左五阶段各96px，4沟16px，共544；顶部48px留标题。右bay220+16+220+16+footer120=592。每drawer的220px是最大高度，closed仅36px可见，展开translate不得增长框体；脚注不是底部floating bar。spine SVG viewBox="0 0 548 544"，置于局部20px安全边；细弧与文字分列，13px文字wrap不裁数。所有操作>=28x28px（32px默认），细未命中带配32x32px代理标签。0px unintended scroll overflow，包括顶抽屉peek和下抽屉全开态。

bay-ledger 120px不是十二行堆表：口径组签32px、正文80px、底余8px。dl内data-face按质量/实践/披露/摩擦/提案分面，每面至多两指标、每项最多两行20px；上下文拆为五片面（五行16px）和cache/P95面。分组预挂载、互斥opacity/inert，点击“全表”先选质量面。较长R1证据说明转下drawer已有面，不在footer做小字或滚动遮盖。

内联S7桥T=80，L0 44px d="M 164,154 C 230,154 286,130 368,130 L 368,174 C 286,174 230,198 164,198 Z"，L1 36px d="M 164,198 C 230,198 286,208 368,208 L 368,244 C 286,244 230,234 164,234 Z"。独立旗用12px（15%×80），在x400侧隔离，不构成三支总和。S11切片T80厚9.6/6.4/12.8/32/19.2；cache另80尺厚77.44/2.56。闭合支流生成式 M x0,y0 C x0+40,y0 x1-40,y1 x1,y1 L x1,y1+h C x1-40,y1+h x0+40,y0+h x0,y0+h Z。左脊上下导线只1.5px导航边，绝不以门禁8/40、返工18或ROI0.4的异分母厚度伪造连续流量。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

Light：desk #F7F9FC、cabinet #FFFFFF、drawer #EDF1F7、ink #1F2B3E、muted #52617B、hit/l0 #4A5BA8、miss/l1 #267188、flag #98612E、focus #295EBC。Dark：#101827、#1E293B、#2C3A50、#F0F5FD、#BCCBE0、#AEBEFF、#97D4E8、#ECC58F、#B6D1FF。branch linearGradient 0%/.22与100%/.58，filled cubic ribbon体积另加1px白specular rim .5/.18。双drawer各有凹8px纸唇、18px圆角、0.5px inner-white highlight和0 4px 12px #1D2A4014软影；不画铁柜厚边框。表面全部opacity1、blur0，glass只可用于功能popover且有Safari/Reduce Transparency实体回退。SF Pro13/16/22，数字tabular-nums；内联24x24 currentColor图标用1.5px笔画。正文对比4.5:1及大数3:1在两主题都检查。

## 6. Apple Native Spring Physics & Flow Animation

右抽纸460ms cubic-bezier(0.22, 1.35, 0.36, 1)，hover peek translateY(-6px)，整体保持220pxbay静止。左活跃桥沿中心C曲线跑1.5px dash脉冲，dasharray4 20、offset0→-96/3000ms；缓存miss仍用窄实带，不给脉冲误导加粗。焦点圈与hover同步增亮，mouseleave还原committed。prefers-reduced-motion: reduce关闭dash循环和overshoot/peek，90ms opacity表达当前抽屉；即使连点五个节点，class切换从当前transform续接，数据与焦点不丢。

## 7. Production Data Inventory & Exact DOM Topology

左脊全链路回溯的5节点一律按Stage1 S11上下文构成（50,000 tok / 96.8%缓存），Stage2 S7渐进披露分流（L0 55% / L1 45% / 越界15%），Stage3 S1/S2/S3触发与门禁（命中2/8 · 拦截8/40 · 误报4/40 · 审计9/12），Stage4 S8/S9返工与逃逸摩擦（返工18次 / 重试6次 / 逃逸3+5），Stage5 S10提案转化与健康度（my-designer0.4 · code-review1.2 · team-lead1.8 proposals/100 runs）。S1的“命中”题签附口径Pin Drift 2/8 behind，不能反向当成功。Operational/data lineage是导航与证据追溯，不等于因果论证。

上drawer专属S11五片：50,000 tok=100%，System / AGENTS 6,000 tok(12%)；Skills4,000 tok(8%)；Tool schemas8,000 tok(16%)；Tool results20,000 tok(40%)；Conversation12,000 tok(24%)。其cache独立命中96.8%＝96,800/100,000 eligible requests，未命中重算3.2%＝3,200/100,000；S7 L0索引浅读55%、L1局部深读45%，越界全量深读15%重叠旗另立分母、无绝对样本数。上页底注S12 Search P95 18,400 tok/120次/7天。下drawer门禁面常驻S1 2/8落后、S2 8/40=20%拦截/4/40=10%独立误报、S3 9/12审计/48 eval cases/+6本周，S4 my-designer40次加载和R1审查证据入口，S6 12次脚本、触达8/40=20%（12不能作触达率分子）。同drawer的摩擦面为S8 20会话内18次编辑返工与6次重试、S9 [IMPL_BUG]3/[SPEC_GAP]5；ROI面为S10三个报告读数和查看建议/收藏/稍后/撤销本地状态操作。bay-ledger提供S5 暂无统计及全S1..S12口径入口，不捏造证据正文或货币公式。

```html
<main class="aidash-card topology-trace-matrix-cabinet">
  <section class="content">
    <div class="cabinet-split-frame">
      <section class="vertical-lineage-spine"><header class="spine-title"></header><svg viewBox="0 0 548 544"><defs></defs><g class="cabinet-cubic-bridges"></g></svg><ol class="cabinet-stage-nodes"><li data-stage="1"></li><li data-stage="2"></li><li data-stage="3"></li><li data-stage="4"></li><li data-stage="5"></li></ol></section>
      <div class="twin-drawer-bay"><article class="context-disclosure-drawer"><button class="context-pull"></button><div class="context-drawer-face"></div></article><article class="gates-roi-drawer"><button class="gates-pull"></button><div class="gates-face"></div><div class="friction-face"></div><div class="roi-face"></div></article><footer class="bay-ledger"><dl class="cabinet-s1-s12-slip"></dl></footer></div>
    </div>
  </section>
</main>
```

li必须展开成有名32px按钮，g必须初始展开五片/cache/S7/flag闭合path，dl包含全部指标。此父子层级不能换成content下的hero、fold-panel、secondary。

## 8. Explicit Anti-Patterns & Verification Targets

柜体不得画stroke-width >24的流管（132/74/58也禁），不得55+45+15求100或96.8%cache占第六片，不得宣称因果美元收益；.caustic-veil/.ruler/Active-Matte/<select>测试控件/沙盒免责copy/innerHTML替换节点都fail。双bay不能通过新增管理页、真实遥测或真实Linear调用实现。

四态双主题验收：I缓存命中/S11/上drawer开启；II hover未命中后Enter提交3.2%，与96.8%独立100,000分母相合；III第三站下drawer门禁面→第四站摩擦面，读取独立误报及3/5归因；IV第五站提案收藏、稍后、撤销、Esc还原pull焦点。测最大抽取边界0px溢出、窄支32px代理、对象全常驻、无数字省略和Reduce Motion停流。十套及全部已到位R3提示的normalized non-heading paragraph overlap必须<=20%才可记complete。
