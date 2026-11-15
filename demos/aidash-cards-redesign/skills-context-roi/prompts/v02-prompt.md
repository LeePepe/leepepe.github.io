# v02 · 双页流向卷宗 (topology-bifurcation-book-folio)

## 1. Visual Metaphor & Archetype Lock

像翻开的工作账本，左页读分岔、右页读去向，抽出的建议卡仍夹在同一书脊中。方向采用 VS-002 瑞士人文账本、CL-002 暖纸森林墨、CP-002 纸卡钱包、IP-003 原位主从；X=左分流选取，Y=右竖向回溯与下方插页，Z=书页0/袋沿2/建议纸3。SWWallet 给纸层关系，Things 3 给标签节奏，R2 B-v04 与 B-v06 给 Owner 已认可的分岔/回溯而不继承粗描边。已查 vault 的 CP-002/VS-002；Alcove、CleanShot X、Sankey 无匹配，只是 brief 参考而非已核实 API。平台 desktop，HTML 只是下游 macOS 单卡选型承载物；不创建 App 页面。

## 2. Single P0 Focus & Initial Showcase State

首屏唯一视觉重心在左页 L1 局部深读 45% 的下支。activeBranch=l1，selectedStage=2/S7；右页节点二选中，proposal drawer 默认 closed，露出 36px“查看建议”纸签，右页 S7 定义已可见。跨页不复刻一组大数字：L1 数字 34px，其余 13px。悬停 cache 小支仅预览“未命中重算”，点击或 Enter 才切换为 cache-miss 并选择 Stage 1；点建议纸签选第五站并在预留底槽内上抽。解释中不制造 L1 专属门禁收益。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

左页的分母边注和右页五个节点属于 P1；门禁、摩擦、S1..S12 诊断和 S10 建议是 P2 的多面插页。HTML 初始加载必须永久挂载全部 SVG <path> ribbons、5 个 trace stage nodes、每一项 S1..S12 metric readout 与所有 pocket drawers；没有首次点开才生成的正文。每页的已有节点靠 CSS class/变量/transform 过渡，叶子文字允许 textContent 更新，禁止 innerHTML、outerHTML、replaceChildren、insertAdjacentHTML 或替换 Element。folded 面设置 inert/aria-hidden，标签保留焦点入口；选中使用 aria-pressed，stage 使用 aria-current，drawer 使用 aria-expanded。hover 不写永久 selection，Esc 先收插页再还原开启按钮，Tab/Enter/Space 与指针同效。

## 4. Measured Layout & 1280x800 Viewport Geometry

在 1280x800 viewport 内 main=(88,76,1104,648)，28px 内边距得到 content 1048x592；main 外空白 308,608px²/1,024,000=30.1375%，>=22%。行预算：header 44 + gap16 + 双页392 + gap16 + 插页124=592。two-page 为 568px 左页、24px 书脊、456px 右页，页内各 20px padding。左 SVG 528x300，viewBox="0 0 528 300"；右节点五行 64px 共320，4个8px gap=352。插页只在124px bay 内移动，文字和动作不超过104px，折叠露36px；0px unintended scroll overflow，不能用 overflow:hidden 掩盖有效文本。正文13px，名称可两行，数量禁止 ellipsis。

124px底插页的全诊断并非同时排十二项：32px分组签加88px正文，dl内data-face把质量拆成S1/S2与S3，实践拆成加载/触达与返工/逃逸，披露和ROI各一面；上下文分五片与cache/P95两面。每面最多两指标、每项两行20px，五片特例五行16px。所有面从初始HTML展开，单面可读，原指标可重用同一readout而非新增相同可见副本。分组签是口径导航，不是测试开关。

左页 S7 的基准 T=80：44px 对55%，36px 对45%。闭合上带 d="M 180,80 C 238,80 286,40 352,40 L 352,84 C 286,84 238,124 180,124 Z"，下带 d="M 180,124 C 238,124 286,148 352,148 L 352,184 C 286,184 238,160 180,160 Z"。旗带独立放在 y230，高12px=15%×80，不从主带分割；每支填充边界用 M x0,y0 C x0+32,y0 x1-32,y1 x1,y1 L x1,y1+h C x1-32,y1+h x0+32,y0+h x0,y0+h Z。五片 T80 的厚度9.6/6.4/12.8/32/19.2；cache 独立80尺为77.44/2.56。两种分母留8px隔断，跨域只绘细语义连线；未提供分支级人数的门禁、摩擦、ROI 不做守恒流量。窄支配32x32px独立 HTML 命中标签，所有控件至少28x28px。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

Light 调色：desk #FAF7F2 / paper #FFFFFF / pocket #F0EADF / ink #302A28 / muted #6D625B / L0 #315E49 / L1 #705D7D / flag #975635 / focus #315B9B。Dark 对应：#1B1A20 / #28262D / #35313A / #F8F1E9 / #C9BCB2 / #B5D9BD / #CBB9D8 / #E8B093 / #A9C7FF。所有带使用自己的 linearGradient，0%→100% stop-opacity 0.22→0.58；1px specular rim 为 #FFFFFF .5/.2。书脊仅1px低对比折影，不画整面网格。下插袋圆角18px、上口中间凹8px，inset 0 0.5px 0 #FFFFFF80（dark #FFFFFF29），外影0 4px 12px #302A2814；抽页14px角。SF Pro正文13px，标题22px，读数 tabular numerals，24x24 currentColor 图标用1.5px圆头描边。纸页始终不透明，glass blur=0、refraction=0；功能提示如需透明只在 chrome，Safari 与 Reduce Transparency 切实体 paper。文本4.5:1/大字3:1是双主题验收底线。

## 6. Apple Native Spring Physics & Flow Animation

proposal pocket 从 collapsed translateY(88px) 到 open translateY(0) 在固定bay内走520ms cubic-bezier(0.22, 1.35, 0.36, 1)；hover peek translateY(-6px) 加在当前位移上。左选中带有一枚2px <animateMotion> 粒子沿对应中心 cubic path 2.8s 循环，使用相同轨迹 id，非选中无常亮粒子。书页不翻转或3D晃动，流动与纸页抽取各有明确角色。prefers-reduced-motion: reduce 删除粒子运动、弹性和peek，仅80ms明暗交叉，选取结果、标签和焦点圈不消失。点击打断正在进行的过渡应从当前值返回，不重挂 DOM。

## 7. Production Data Inventory & Exact DOM Topology

右页的 operational/data lineage 叫全链路回溯，五节点按：Stage 1 S11 上下文构成（50,000 tok / 96.8% 缓存）；Stage 2 S7 渐进披露分流（L0 55% / L1 45% / 越界15%）；Stage 3 S1/S2/S3 触发与门禁（命中2/8 · 拦截8/40 · 误报4/40 · 审计9/12）；Stage 4 S8/S9 返工与逃逸摩擦（返工18次 / 重试6次 / 逃逸3+5）；Stage 5 S10 提案转化与健康度（my-designer 0.4、code-review 1.2、team-lead 1.8 proposals/100 runs）。S1“命中”短标必须有定义，2/8 指 Pin Drift behind，不称成功触发。整条链仅连接观察资料，不证明因果或金额。

左页五片必须标注 System / AGENTS 6,000 tok (12%)，Skills 4,000 tok (8%)，Tool schemas 8,000 tok (16%)，Tool results 20,000 tok (40%)，Conversation 12,000 tok (24%)，合计50,000 tok=100%。缓存栏另写命中96.8%（96,800 / 100,000 eligible requests）与未命中重算3.2%（3,200 / 100,000）；S7 为 L0 索引浅读55%和L1 局部深读45%，越界全量深读15%是独立重叠标记，绝对样本数未知。右插页诊断包括：S1 2/8落后；S2 8/40=20%拦截、4/40=10%误报；S3 9/12审计、48 eval cases、本周+6；S4 my-designer 40次加载与 R1 审查证据指向；S6 12脚本执行、触达8/40=20%，脚本数不作触达率；S5 暂无统计。摩擦面 S8 20会话/18次编辑返工/6次重试，与S9 [IMPL_BUG]3/[SPEC_GAP]5分列。S12 边注 Search P95 18,400 tok、120次/7天。S10 三技能数值仅报告转化读数，建议动作限查看建议、收藏、稍后、撤销，本地可逆，不执行治理或调用真实服务。

```html
<main class="aidash-card topology-bifurcation-book-folio">
  <section class="content">
    <header class="folio-header-strip"></header>
    <div class="folio-two-page">
      <section class="ribbon-left-page"><svg viewBox="0 0 528 300"><defs></defs><g class="folio-slice-streams"></g><g class="folio-disclosure-streams"></g><g class="folio-cache-streams"></g><g class="folio-flag-stream"></g></svg><div class="folio-branch-labels"></div></section>
      <section class="trace-right-page"><ol class="folio-five-nodes"><li data-stage="1"></li><li data-stage="2"></li><li data-stage="3"></li><li data-stage="4"></li><li data-stage="5"></li></ol><div class="folio-definition-face"></div></section>
    </div>
    <aside class="proposal-pocket-drawer"><button class="proposal-pull-tab"></button><div class="folio-proposal-face"></div><div class="folio-friction-face"></div><dl class="folio-s1-s12-audit"></dl></aside>
  </section>
</main>
```

这些子树须直接展开为初始HTML，g内填所有真实path、li内放32px stage按钮，dl内完整12指标；不要留下空槽再由JS渲染。content 的 direct children 不准改成 hero/fold-panel/secondary。

## 8. Explicit Anti-Patterns & Verification Targets

不许粗线管 stroke-width > 24（尤其132、74、58），不许55+45+15=100、不许cache96.8%成为第六切片；因果美元节省、.caustic-veil、.ruler、Active-Matte、<select>测试切换、沙盒免责文案、innerHTML替换均被拒绝。也不能凭参考书页造历史库或新管理页。

四态截图每态双主题：A 首载L1/S7/插页收起；B hover cache-miss后键盘提交，Stage1边注显示3,200/100,000且带宽不变；C 从第三站到第四站，在原位定义面核对8/40、4/40与18/6及3/5；D 抽建议、收藏、稍后、撤销、Esc收起。验证节点引用全程同一、未命中仍有32px命中区、最大抽出0px滚动、无数字截断、reduced-motion可操作。Stage1交接前跨全部可用R3 prompt跑<=20% normalized non-heading paragraph overlap。
