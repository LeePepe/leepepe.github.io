# v10 · 精密流向证据工作台 (topology-workbench-lineage-dock)

## 1. Visual Metaphor & Archetype Lock

用左右纸袋夹住中央全链路流场，像开发者把一张证据单放在精密桌台而非开启新后台。VS-007精密遥测、CL-008靛蓝海军、IP-001交叉高亮、IP-003原位证据、CP-002抽页；X=中场分支与stage，Y=左slice袋/中央trace/右摩擦提案drawer三域，Z=工作台0/纸背1/抽页2/袋唇3。Linear/Flighty提供精确标签参考，SWWallet与Things 3在vault有依据；Alcove、CleanShot X、Sankey无vault结果，不能虚构组件源码。R2 B-v04/v06加A-v09只提取Owner认可的流带、回溯和凹口，desktop单卡且不冻结生产主题。

## 2. Single P0 Focus & Initial Showcase State

初始branch=slice-tool-results，selectedStage=1/S11，leftPocket=context/open=true；唯一P0是“Tool results 20,000 tok · 40%”，24px，中心对应40px切片亮起。rightDrawer=friction/open=false，露36px“摩擦与提案”把手，提案正文常驻收起。中间五stage节点均可见，只有第一站选中。选S7切为L0，选第五站把右drawer切为proposals/open=true；context大数不能与0.4 ROI并列竞争。hover cache miss只暂亮细支及口径，离开还原Tool results。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

中央canvas是P0操作域，P1为top rail与左切片标注，P2为右抽屉的摩擦/提案/全诊断及左袋缓存口径插页。initial load时所有SVG <path> ribbons、5 trace stage nodes、全S1..S12 metric readouts及所有pocket drawers必须永久挂载。选择仅用class、CSS变量、transform、dataset、aria和已有叶子textContent；innerHTML/outerHTML/replaceChildren/insertAdjacentHTML或卸载重建全部不准。inactive面inert/aria-hidden，袋签和stage保留32px命中。hover是可恢复preview，click/Enter/Space才commit；Esc先收右插页并回开启把手，focus-visible必须亮同条带。三域共用一套branch/stage/drawer状态，不能各自改数。

## 4. Measured Layout & 1280x800 Viewport Geometry

1280x800 viewport中 main x88/y76/w1104/h648，padding28，content1048x592。主框外308,608px²=30.1375%净空，>=22%。toprail48 + gap12 + trizone488 + gap12 + bottomlip32=592。trizone列宽212/576/212，中沟各24px。左右袋各212x488、内padding16；长slice/skill名允许两行13px，数值/units整体不ellipsis。中心SVG viewBox="0 0 576 340"，下148px五stage trace（5×104px+4×14px=576），每stage内容48px短标+定义入口，其长口径转已有drawer。所有最大抽取在原488px域内完成，0px unintended scroll overflow，不靠遮掉数据解决。细slice与3.2%分支用32x32px外部代理标签；任何target>=28x28px。

212px右袋不能承载一张未折的十二项全表。诊断面内32px口径签、400px数据区、24px安全边；质量/实践/摩擦/披露/提案为常驻data-face，每面最多三项、每项最多三行20px，S11五片与cache/P95分两面。名称可自然换行，已有dl readouts只在对应面显示，其他面inert，选全诊断先进入质量面。左五片与右S11口径不能同时重复一份图例：读右context面时左面折为签，仍保持原node。

中心S7用T100：L0 d="M 210,96 C 276,96 320,58 408,58 L 408,113 C 320,113 276,151 210,151 Z"；L1 d="M 210,151 C 276,151 320,182 408,182 L 408,227 C 320,227 276,196 210,196 Z"，各55/45px。旗d="M 242,282 C 300,282 338,262 418,262 L 418,277 C 338,277 300,297 242,297 Z"独立15px，不侵入100px母尺。S11五片100尺厚12/8/16/40/24，cache另100尺96.8/3.2；按 M x0,y0 C x0+36,y0 x1-36,y1 x1,y1 L x1,y1+h C x1-36,y1+h x0+36,y0+h x0,y0+h Z生成closed faces。context与disclosure之间是聚合导航，不猜条件分配；stage3/4/5只有1.5px中性连接线，不把异分母数据画成同一流量。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

Light tokens：desk #F8FAFC、surface #FFFFFF、pocket #EDF1F8、ink #202A3E、muted #53617A、slice/l0 #4E5DAB、cache/l1 #28738D、flag #996034、focus #2F5FB8。Dark tokens：#0E131F/#1D283A/#2C3B52/#F1F5FC/#BDCAE0/#B6C0FF/#A0D8E9/#EDC398/#B7D2FF。带fill为linearGradient 0% stop-opacity.22→100%.58，加1px白specular rim .55/.20。左右纸袋凹口深8px、18px圆角、0.5px inner-white highlight，抽纸投影0 4px 12px #15254214；中央图域不用边框再套框。SF Pro13/16/22，P0 24，全部数量tabular numerals；inline24x24 currentColor SVG icon笔画1.6px附标签。实体内容opacity1/blur0/refraction0，glass只能功能popover，Safari与Reduce Transparency用同色不透明回退；正文4.5:1及大字3:1对比均要核验。

## 6. Apple Native Spring Physics & Flow Animation

右paper drawer和左口径插页520ms cubic-bezier(0.22, 1.35, 0.36, 1)，hover把手peek translateY(-6px)，用offset变量叠加，不新增高度。active ribbon沿其中心C路径播放2px animateMotion粒子/2600ms，非选支只有静态高光，不让发光粗stroke变成流量。键盘focus、hover和click联动同条闭合带和对应drawer，连点从当前transform继续。prefers-reduced-motion: reduce取消particle、overshoot与peek，90ms opacity保留选择与全部读数，Esc焦点恢复不变；无需任何测试状态<select>才能看见动作。

## 7. Production Data Inventory & Exact DOM Topology

中心trace五站为全链路回溯：Stage1 S11上下文构成(50,000 tok / 96.8%缓存)→Stage2 S7渐进披露分流(L0 55% / L1 45% / 越界15%)→Stage3 S1/S2/S3触发与门禁(命中2/8 · 拦截8/40 · 误报4/40 · 审计9/12)→Stage4 S8/S9返工与逃逸摩擦(返工18次 / 重试6次 / 逃逸3+5)→Stage5 S10提案转化与健康度(my-designer0.4 · code-review1.2 · team-lead1.8 proposals/100 runs)。门禁口径明确S1 Pin Drift 2/8 behind，“命中”短标不作触发成功；operational/data lineage不声称观察相关性证明因果或美元收益。

左slice袋完整50,000 tok=100%：System / AGENTS 6,000 tok (12%)、Skills 4,000 tok (8%)、Tool schemas 8,000 tok (16%)、Tool results 20,000 tok (40%)、Conversation 12,000 tok (24%)。左cache插页单独命中96.8%（96,800/100,000 eligible requests）、未命中重算3.2%（3,200/100,000）。中心S7 L0索引浅读55%和L1局部深读45%，越界全量深读15%是独立重叠标志，无绝对次数不编。右摩擦面S8 20会话/18次编辑返工/6次重试各自计数，S9 [IMPL_BUG]3/[SPEC_GAP]5；右提案面S10三报告读数及查看建议、收藏、稍后、撤销本地状态，不造货币算法或真实治理操作。右诊断面全部S1..S12：S1落后2/8，S2拦截8/40=20%/误报4/40=10%，S3审计9/12、48 eval cases、本周+6，S4 my-designer40次加载与R1审查证据指向，S6 12脚本执行/触达8/40=20%（12不是触达次数），S5 暂无统计，S12 Search P95 18,400 tok/120次/7天。诊断bottomlip只是打开已有面入口，不再全量重复切片图或造证据正文。

```html
<main class="aidash-card topology-workbench-lineage-dock">
  <section class="content">
    <header class="workbench-top-rail"></header>
    <div class="tri-zone-workbench">
      <aside class="left-slice-pocket"><button class="slice-pocket-tab"></button><dl class="five-slice-readouts"></dl><div class="cache-denominator-slip"></div></aside>
      <figure class="center-alluvial-trace"><svg viewBox="0 0 576 340"><defs></defs><g class="workbench-context-ribbons"></g><g class="workbench-cache-ribbons"></g><g class="workbench-disclosure-ribbons"></g><g class="workbench-overlap-flag"></g><g class="workbench-flow-particle"></g></svg><div class="workbench-branch-proxies"></div><ol class="workbench-five-stage-trace"><li data-stage="1"></li><li data-stage="2"></li><li data-stage="3"></li><li data-stage="4"></li><li data-stage="5"></li></ol></figure>
      <aside class="right-roi-drawer"><button class="roi-drawer-pull"></button><div class="workbench-friction-face"></div><div class="workbench-proposal-face"></div><dl class="workbench-diagnostic-face"></dl></aside>
    </div>
    <footer class="diagnostic-bottom-lip"></footer>
  </section>
</main>
```

初始HTML展开g内所有真实闭合paths、li内32pxstage按钮、dl完整指标和提案actions。此大纲不是等待JS填充的空槽，content不能改成hero/fold-panel/secondary三块模板。

## 8. Explicit Anti-Patterns & Verification Targets

禁stroke-width >24粗管（132/74/58旧法）、55+45+15=100、cache96.8%第六slice、因果美元收益、.caustic-veil、.ruler、Active-Matte、<select>测试开关、沙盒免责copy和innerHTML替换节点。工作台不新增LLM操作/管理页、不连接真实scheduler、Linear、CloudKit或私有遥测。

核验四态×Light/Dark：A首载Tool results40%/Stage1/左袋开右袋收；B hover cache-miss后Enter提交3.2%并打开独立分母，再选L0读55%；C第三站门禁再第四站摩擦，拦截/误报和18/6、3/5保持真实独立口径；D第五站提案收藏、稍后、撤销、抽全诊断、Esc回右把手。测试0pxoverflow、数字完整、三个域节点identity、细带32px代理、focus与hover等价以及Reduce Motion停流；交接前全部现有R3 prompts的normalized non-heading paragraph overlap<=20%。
