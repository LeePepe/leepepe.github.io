# v08 · 五层伸缩回溯抽屉 (topology-telescopic-trace-drawers)

## 1. Visual Metaphor & Archetype Lock

将五站链折成五层伸缩纸抽屉，左边弯曲流脊给方向，右边凭条检查器给口径；一次仅一层抽开，不把所有指标堆进长表。坐标锁VS-005、CL-006、CP-002、IP-003：X=抽屉stage选择，Y=五层单开accordion+右凭条，Z=槽0/左流带1/纸抽屉2/凹唇3。Things 3给安静列表，SWWallet给实体袋层，R2 B-v06给全链路回溯；R2 B-v04的粗stroke彻底不用。Vault已命中Things/SWWallet，Alcove/CleanShot X/Sankey无条目，不能声称引用可用组件。desktop范围，仅真实AIDash诊断动作。

## 2. Single P0 Focus & Initial Showcase State

默认branch=l0、selectedStage=3/S1-S2-S3，drawer3 open=true，其他四层收成72px纸签。P0是第三层“拦截8/40 · 20%”，24px；L0 55%只是当前流脊选择，不能说它造成拦截。右voucher默认为S2定义，正文含独立误报4/40=10%。点流脊L1选第二层披露，点第四层改voucher看返工/逃逸，第五层才看建议。所有层号的次序固定，不拖拽排序或创造档案记录。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

五层题签是P1，层内证据和voucher二级口径是P2，S1..S12全表是voucher内可抽slip。初始DOM永久挂载全部SVG <path> ribbons、全部5 trace stage nodes、所有S1..S12 metric readouts及pocket drawers。单开只是class/dataset/CSS变量/transform/opacity/aria的改变，不允许innerHTML、outerHTML、replaceChildren、insertAdjacentHTML或delete/recreate元素；已有叶子textContent可变但不生成整面模板。inactive layer正文inert且aria-hidden，layer tab保持可聚焦。hover临时亮带，Enter/Space和click提交；Esc先收voucher slip再收当前层，焦点回该层tab，读屏得到正确展开状态。

## 4. Measured Layout & 1280x800 Viewport Geometry

总画框1280x800，main(88,76)1104x648、padding28，content1048x592；外留白30.1375%=308,608px²>=22%。telescopic-layout三列144 / 552 / 320px，中间两沟16px，共1048。drawer list单开层256px、四收层各72px、4gap12px，合592；切层用grid-track transition，宽高总预算始终不变。inspector320x592，24px内padding，顶部48px/主体384px/审计slip112px；审计slip最大112px，不盖主体按钮。左SVG viewBox="0 0 144 592"，不在144px宽内硬塞长标签，按钮文本放layer/voucher，左边32x32px代理保障小支命中。所有controls>=28x28px、正文13px、数字完整，全部四态0px unintended scroll overflow。

voucher审计slip112px严格分配32px口径签+80px内容：质量、实践、摩擦、披露、提案各为多张常驻data-face，每面不超过两指标、每指标至多两行20px；context五切片专面五行16px，cache与P95另面。全部S1..S12可由口径签走到，却不得同时挤入112px。dl的分组div只以opacity/transform/inert切换，首开质量组，数字不裁不缩到13px以下，不能新增测试开关。

左脊局部沿x展开的T80 split：L0 44px d="M 16,180 C 42,180 68,152 104,152 L 104,196 C 68,196 42,224 16,224 Z"；L1 36px d="M 16,224 C 42,224 68,242 104,242 L 104,278 C 68,278 42,260 16,260 Z"。15%旗独立厚12px摆在y304，不插入80px母带。第一层附近S11五片厚9.6/6.4/12.8/32/19.2，共80；cache另80尺77.44/2.56放y70局部区。所有带的closed cubic公式 M x0,y0 C x0+26,y0 x1-26,y1 x1,y1 L x1,y1+h C x1-26,y1+h x0+26,y0+h x0,y0+h Z；层间连接只1.5px曲线语义边，门禁8/40等不同分母不能假装继承token流量。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

Light用desk #F5F6F8、surface #FFFFFF、drawer #ECF1EE、ink #22332B、muted #58675F、l0/hit #356C50、l1/miss #4C6F9A、flag #956037、focus #2A61AA。Dark相应#151D22、#23312C、#304037、#F0F7EF、#BED0C1、#ACDDBD、#B6D1EF、#ECC39D、#BCD7FF。每branch linearGradient在0% stop-opacity.22、100%.58，closed fill外添1px白rim .5/.2。抽屉纸唇中心凹6px、18px角、0.5px inner-white highlight，阴影0 3px 10px #23332B14；层签只一条细折影，不画全柜边网。SF Pro13/16/22及tabular numerals，inline24x24 currentColor图标1.5px有可见名称。实体content opacity1，无玻璃blur/refraction；功能tooltip如玻璃化需Safari/Reduce Transparency实体回退且正文4.5:1、大字3:1。

## 6. Apple Native Spring Physics & Flow Animation

单层伸展和凭条抽取420ms cubic-bezier(0.22, 1.35, 0.36, 1)，layer tab hover peek translateY(-6px)，位移容纳在12px层沟。高度轨道合计固定，内部纸面用transform沿轨移动，不能一个新层突然撑开窗。选中branch中心加1.5px虚线光轨dash2 22/offset0→-96/2800ms；焦点与hover同支高亮，不改变宽度。prefers-reduced-motion: reduce停dash与overshoot/peek，只80ms opacity和瞬时固定轨道更新；连点层签沿当前animation value接续，旧节点原位不销毁。

## 7. Production Data Inventory & Exact DOM Topology

五drawer依次Stage1 S11上下文构成(50,000 tok / 96.8%缓存)、Stage2 S7渐进披露分流(L0 55% / L1 45% / 越界15%)、Stage3 S1/S2/S3触发与门禁(命中2/8 · 拦截8/40 · 误报4/40 · 审计9/12)、Stage4 S8/S9返工与逃逸摩擦(返工18次 / 重试6次 / 逃逸3+5)、Stage5 S10提案转化与健康度(my-designer0.4/code-review1.2/team-lead1.8 proposals/100 runs)。右voucher标题全链路回溯，定义operational/data lineage；S1 Pin Drift落后2/8是“命中”短标真实口径，不等于成功触发。

层1收S11 50,000 tok=100%的System / AGENTS6,000 tok(12%)、Skills4,000 tok(8%)、Tool schemas8,000 tok(16%)、Tool results20,000 tok(40%)、Conversation12,000 tok(24%)；cache独立eligible requests100,000：命中96.8%（96,800/100,000）、未命中重算3.2%（3,200/100,000）。层2写S7 L0索引浅读55%、L1局部深读45%、越界全量深读15%独立重叠旗，无绝对样本数。层3包含S1落后2/8、S2拦截8/40=20%/误报4/40=10%、S3审计9/12/48 eval cases/本周+6；voucher补S4 my-designer40次加载与R1审查证据入口、S6 12脚本执行和触达8/40=20%（不是12/40）。层4含S8 20会话中18次编辑返工、6次重试（独立计数），S9 [IMPL_BUG]3、[SPEC_GAP]5。层5含S10三技能报告读数与查看建议、收藏、稍后、撤销本地操作，不计算货币公式。voucher全审计slip含全部S1..S12、S5 暂无统计及S12 Search P95 18,400 tok/120次/7天，不能以0冒充缺失或造证据正文。

```html
<main class="aidash-card topology-telescopic-trace-drawers">
  <section class="content">
    <div class="telescopic-layout">
      <figure class="vertical-bezier-spine"><svg viewBox="0 0 144 592"><defs></defs><g class="telescopic-context-bands"></g><g class="telescopic-cache-bands"></g><g class="telescopic-disclosure-bands"></g><g class="telescopic-flag"></g><g class="telescopic-pulse"></g></svg><figcaption class="spine-hit-proxies"></figcaption></figure>
      <ol class="telescopic-drawer-list"><li class="telescopic-paper-drawer" data-stage="1"></li><li class="telescopic-paper-drawer" data-stage="2"></li><li class="telescopic-paper-drawer" data-stage="3"></li><li class="telescopic-paper-drawer" data-stage="4"></li><li class="telescopic-paper-drawer" data-stage="5"></li></ol>
      <aside class="voucher-inspector"><header class="voucher-heading"></header><div class="voucher-definition-faces"></div><div class="voucher-audit-slip"><dl class="telescopic-metric-readouts"></dl></div></aside>
    </div>
  </section>
</main>
```

初始HTML展开li的32px层签/正文、所有closed paths与S1..S12 dl，outline不是空壳JS模板。content直接孩子不许hero、fold-panel、secondary。

## 8. Explicit Anti-Patterns & Verification Targets

必须拒绝stroke-width >24流管（132/74/58旧法）、55+45+15归100、cache96.8%第六slice、因果美元收益，以及.caustic-veil、.ruler、Active-Matte、<select>测试状态、沙盒免责copy、innerHTML替换。伸缩层不能变成历史记录页，也不能接真实Linear/CloudKit/遥测或scheduler。

四态×Light/Dark：一首载L0/Stage3/S2凭条；二hover L1后键盘选中，层2展开45%与独立15%；三层4读18/6和3/5，再抽S1..S12凭条；四层5收藏→稍后→撤销→Esc，焦点回第五层签。测list高度592恒定、0px溢出、所有节点identity、32px细带代理、数字无截断、Reduce Motion无连续流动。所有可用R3提示<=20%非标题段落重叠后才能落完成标记。
