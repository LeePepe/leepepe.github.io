# v01 · 纸缝里的上下文去向 (topology-inline-bifurcation-pockets)

## 1. Visual Metaphor, Palette & Anti-Clone Spatial Lock

把这张 AIDash 卡设计成一册瑞士排版的薄页索引：六张档案口袋沿同一左边线排列，选中的纸页从袋口向下展开，把抽象的上下文消耗变成能沿着指尖读下去的文件去向。主要平台是 web、macOS 指针语义；探索坐标取 VS-002 × CL-002 的纸感变奏，X 为查阅、Y 为单项行内展开、Z 为实体纸页与低抬升抽屉。它不是左栏加右侧 inspector，不是磁贴阵列，更不是顶部大型总图。一个独立 Writer 只手写 skills-context-roi/v01.html；不得借用其他候选的 CSS 骨架或批量生成页面。

暖象牙画布 #FAF8F4、浅纸页 #FFFDF9、深墨 #242329、附注 #646169、袋缝 #DCD6CC 构成 Light；Dark 改为黑曜岩 #151619、纸页 #222328、选中内页 #2B2C32、正文 #F1EDE6。选中强调用非状态的石墨细线，而非高饱和背景。页眉 24px 中等字重宋体/系统 serif，仅标题使用；技能名 13px system-ui，数值和文件名 11px SF Mono/monospace，图注 11px。除状态脊和流带外保持低彩度；拒绝满页棕色拟物噪点、木纹、宽阴影与装饰性邮票。

## 2. Single P0 Focus, Semantic Status Colors & Initial Showcase State

唯一 P0 是「my-designer 的 L1 连带 Token 花在哪里」；初次进入便打开第一张 my-designer 口袋，使 navigation-evidence-contract.md 的高频命中与 remotion-video.md 的冷分支同场可见。其他五张保持完整指标正面、详情关闭；顺序固定为 my-designer、team-lead、design-studio、m2-dispatcher、linear-board、archive-deck-helper。P1 是相邻调用/Token/脚本/Eval 四个摘要，P2 是抽屉里的逐文件路径与脚本执行明细，源时间和覆盖说明退到页脚。

六张卡各有 6px 左侧语义脊：team-lead、design-studio、m2-dispatcher、linear-board 用 #10B981 翡翠绿并写「主力健康」；my-designer 用 #F59E0B 琥珀与「L1 偏高 · 冷门分支」；archive-deck-helper 用 #8B5CF6 紫脊，另配 #F43F5E 逃逸小标，文字保留「🧟 30d 零调用 · 建议归档」及「7d 0 次 · 30d 0 次 · 逃逸 3」。绿色表示本轮 Owner 指定的健康分类，不是未经计算的收益金额或臆造 ROI 分数。所有颜色搭配文字和小型 inline SVG 状态符号，浅色主题不能直接用亮绿充当细字，文字采用更深的同色墨。

正面四枚宽而扁的指标胶囊都有明确读序。第一枚含 7d/30d 调用、30d 活跃会话与僵尸状态；第二枚含 L0 (SKILL.md) Token、L1 平均连带 Token 和 Cache 96.8%；第三枚含 scripts/*.py 次数、均值/P95 ms 与成功率；第四枚含 eval-cases.json 用例数、+本周新增、通过率、拦截/逃逸及归因。Owner 给定的 my-designer 展示例为 7d 42 次、30d 156 次、28 会话，L0 1.8k tok、L1 均值 +3.4k tok，Eval 24 用例 (+4 本周)、100% 通过、拦截 19 次、逃逸 2 次 [1 IMPL_BUG / 1 SPEC_GAP]；这些是规格示例而非本次查库得到的观测值。未给定的其他技能计数、会话、Token、脚本耗时和评测值保留字段并显示「待采集」，绝不把同一示例复制给所有技能。

## 3. Hover Brief Preview ([data-hover-brief]) & Click-to-Pull-Out Bifurcation Drawer ([data-bifurcation-panel]) Contract

每个 article.skill-pocket-card[data-skill-row] 都包含真实 button[data-skill-trigger] 与专属 [data-hover-brief]。非按钮空白处点击可委托给该 trigger，但不能嵌套按钮。卡面底边预留 16px 纸缝，平时简介透明，pointerenter 或 :focus-within 后整张卡 translateY(-4px)，纸缝中简介 opacity 从 0 到 1、translateY 从 4px 到 0；指标绝不被浮层盖住。my-designer 的一行文案为「诊断快览：navigation-evidence-contract.md 62% · remotion-video.md 0 命中 · P95 310ms」；其余行以本技能最高命中资产和治理建议生成，尚无资产明细时写「诊断快览：主力健康 · Reference / Script 明细待采集」，归档样本则写「诊断快览：30d 零调用 · 逃逸 3 · 核对归档建议」。简介可以在卡宽内读完，不用 title 属性代替可见文字。

点击 trigger 的状态机为 closed → opening → open → closing；aria-expanded 与 aria-controls 同步，最多一页展开。每个口袋预置自己的 [data-bifurcation-panel]，关闭时 grid-template-rows:0fr、内部 min-height:0、inert，展开时 1fr；不要用固定 max-height:9999px 伪造动画。打开新页同时收回旧页，并保持被点击标题可见；仅在它位于视口外时使用 scrollIntoView({block:'nearest'})，不强迫每次点击跳到顶部。Esc 收起当前页、焦点回到 trigger，Enter/Space 与鼠标等价。

常驻 DOM 是硬约束 removedElements = 0：切换 class、dataset、CSS 变量、文本节点值，不使用 innerHTML、replaceChildren、条件销毁 SVG 或把 article 移到别的父节点。点击每条 [data-branch] 流带只锁定该路径并更新抽屉底部读数，不触发父卡收起；再次点同一路径解除，Esc 首先解除路径焦点再收抽屉。冷文件的「查看冷门分支」只是阅读库存与命中证据，不能自动删除文件。

## 4. Measured 1280x800 Viewport Geometry & Spatial Bounding Boxes

按 CSS 像素锁定 1280×800。页面左右各 64px，content 宽 1152px；swiss-roi-masthead 位于 (64,28,1152,44)，口袋区域从 y=84 起。六张闭合正面各高 72px，邻页 8px 间隔；首张下方展开页固定目标 196px。初始盒子为 my-designer (64,84,1152,72)、它的抽屉 (64,156,1152,196)、team-lead (64,360,1152,72)、design-studio (64,440,1152,72)、m2-dispatcher (64,520,1152,72)、linear-board (64,600,1152,72)、archive-deck-helper (64,680,1152,72)；页脚 y=760..780。这样六个正面和一个实际分岔抽屉在一屏内成立，而不是声称所有 6 个 300px 抽屉同时可见。

卡面 x=84..312 给名称与语义徽章，四枚指标从 x=328 起使用约 208px 等宽列、8px 间距，最右止于 1184。胶囊顶部 y=cardTop+6、高 46px，内部最多三行、11px/14px 行高；预览缝 y=cardTop+54..70 独占一条通栏。Eval 的归因另占胶囊第三行，不把长分类名挤进数值旁。身份列允许 archive-deck-helper 名称一行完整显示，禁止全卡 nowrap 或以省略号截掉数值。

抽屉采用 (84,164,1112,144) 的横向 SVG 区域，再在 y=312..344 放一条 32px 明细收据。SVG viewBox 为 0 0 1112 144：意图标签 x=4..208、L0 枢纽 x=274..460、输出文件标签 x=752..1108；三个入口中心 y=32/70/108，右侧四个 Reference 与三个 Script 中心 y=14/33/52/71/90/109/128。文件名与指标使用 10.5–11px 等宽字体且独立 HTML/SVG 可访问标签；若字体实测不够宽，路径名分成 basename 和元数据两个区域，不缩到不可读。底部明细是单选路径的补充，不把所有 7 条明细再做一次平铺表格。

小于 1080px 时让身份区域与指标转为上下两行、口袋高度随内容增长，整页正常纵向滚动；分岔图在本抽屉内拥有独立横向滚动，最低图宽 1000px。390px 宽不能保持六列硬挤，触控 target 不低于 44px；desktop trigger 有覆盖卡面的大 hit area，独立路径标签至少 32px 点击高度。仅图表容器可横滚，根页面 scrollWidth 必须等于 clientWidth。

## 5. Dual-Theme Surface Polarity & Filled Cubic-Bezier Ribbon Craft

纸页的层次由亮度差而非粗边框表达：Light 卡片 inset 0 1px 0 rgba(255,255,255,.8)，0 2px 6px rgba(40,32,20,.035) 的贴地影与展开时 0 9px 24px rgba(40,32,20,.07)；Dark 用 .07 白色内高光、低透明黑影，不把内页反成白纸。外角 12px、内页 8px，袋口用 1px 内凹弧线，不采用通页锯齿蒙版。正文对比至少 4.5:1。该候选没有 backdrop-filter；抽屉卡内容是实面材质，绝不以玻璃采样纸页。

每条有效流带使用闭合填充路径，非粗描边管道。例如本地坐标的一条 Reference 可写成 <path data-branch="paper-navigation" d="M 460,62 C 560,62 630,10 742,10 L 742,21 C 630,21 560,73 460,73 Z">，fill 使用 paper- 前缀唯一 linearGradient，从低透明石墨/琥珀入口渐变到文件语义色，轮廓 stroke-width=0.75。所有流带 stroke-width <= 24，实际设计 <=1；热路径有薄内高光。意图→枢纽与枢纽→Reference/Script 是两级分岔，不画成单条绕过 SKILL.md 的彩线。

右支显示 navigation-evidence-contract.md (62% · 2.4k tok)、interaction-layering.md (28% · 1.6k tok)、appearance-ledger.md (19% · 1.4k tok)，以及 remotion-video.md (0 命中 · 冷门冗余告警)。命中百分比是可重叠的会话覆盖而非互斥份额，62+28+19 不要求等于 100；带宽按同组独立命中强度映射，不伪装质量守恒的 Token 桑基账。0 命中出口保留库存标签及细虚线 tether，它的 data-branch 闭合路径为零宽、无填充、无粒子，不给冷资产发明正流量。脚本分支宽度使用本组执行次数，不能混用 Reference 命中率作为脚本成功率。

## 6. Apple Native Spring Physics & Animated Flow Particles

纸页运动取轻而短的机械阻尼：hover 260ms，展开 480ms、收回 360ms，统一 cubic-bezier(0.22, 1.35, 0.36, 1)。卡片只升 -4px，不做旋转、夸张缩放或所有兄弟的弹跳；展开内页从 translateY(-6px) 回到 0，阴影延后 60ms 达峰，让「纸页离开缝口」先于「阴影扩散」。布局行高动画由包裹层完成，文本 opacity 单独 140ms ease-out，不用过冲曲线作用于透明度。

对当前选中 my-designer 的活跃分支每条放 1 个 1.5px 流光点，沿另存的三次贝塞尔中心线 animateMotion，周期 3.2s、分支错开 240ms，尾迹只占 8px。渐变 fill 保持稳定，脉冲另加 0.7px 中线高光；未展开口袋暂停动画，冷 Reference 停止发光。pointerleave 消除 hover 升起但不关闭用户已点击的页；快速点击必须从当前动画进度反向，不排队产生开/关回放。

prefers-reduced-motion 下取消所有位移、粒子和高度过冲，状态用不超过 100ms 的交叉淡入或即时展开，读数仍然可达；页面离屏或 visibilityState=hidden 时暂停路径运动。没有音效或伪 haptic。键盘 focus-visible 使用 2px 高对比描边与 3px offset，outline 不得被袋口 overflow 裁去。

## 7. Production Data Inventory (Zero S1-S12 Jargon) & Exact DOM Topology

生产数据读取接口以 Snapshot 为唯一上游：L1_collect/raw → L2_normalize/clean → L3_merge/schema → L4_serve SQL → L5_apps/digest/skills_roi_snapshot.py → skills-roi.json。2026-11-15 在 ~/Development/AIDash/aidata 运行 inspect_aidata_pipeline.py --metrics skills_roi,reference_hits,script_latency,eval_effect --check-contract --json；reference_hits、script_latency、eval_effect 结果均为 needs_l1_collection。此检查没有验证任何展示数值。故 Writer 可将 Owner 指定数值作为本轮封闭展示输入，但必须在数据对象保留 provenance=owner_spec_example；不得将这些数值写入生产遥测或把旧 fact_turn.tool_calls 字符串数组当作逐文件/逐脚本事实。真正接入前需先补路径、执行时间及 Eval 事件采集，按上游 aidata-metric-extension/spec.md 的蓝图建模与导出。

每个 skill 的载荷包含 calls_7d、calls_30d、active_sessions_30d、is_zombie_30d、l0_tokens、l1_avg_attached_tokens、kv_cache_hit_pct、scripts[] 的 calls/avg_duration_ms/p95_duration_ms/success_rate，以及 eval_cases_total/weekly_delta/pass_rate/intercepted_count/escaped_count/escape_breakdown。缺失、覆盖不足与实际 0 是不同状态；只有完整 30d 观察窗口和库存存在时生产端可判僵尸/冷文件。Cache 展示例 96.8% 不等同于 Reference 缓存，也不可把无调用技能的未知均值变成 0ms。快照 window、coverage_status、source_as_of 留在页脚与详情的覆盖说明，不在卡面放内部指标编号。

my-designer 左入口明确列 UI 探索画廊 48%、实现后截图回溯 34%、规范审计 18%；中央写 SKILL.md (L0 入口 · 1.8k tok)。右下脚本须逐项可选：design_evidence.py (46次 · P95 310ms · 98.5%)、design_catalog.py (39次 · P95 480ms · 100%)、verify_design_cases.py (18次 · P95 190ms · 100%)；均值未获 Owner 数值时用待采集。其他 5 张详情各拥有自己的图节点和资产清册，未知路径不可冒充 my-designer 的三个脚本；无数据时仍打开完整入口/枢纽/Reference 与 Script 两组结构，显示「路径明细待采集」，archive 样本保留零调用状态而不生成流动流量。

具体子树必须是 main.topology-inline-bifurcation-pockets > section.content，其直系孩子按序为 header.swiss-roi-masthead、div.inline-pocket-stack、footer.swiss-governance-foot。stack 含 6 个 article.skill-pocket-card[data-skill-row]；每个 article 内为 .paper-face（身份、4 胶囊、button[data-skill-trigger]、[data-hover-brief]）与 .paper-slide[data-bifurcation-panel]（figure 的常驻 SVG、.paper-branch-receipt）。禁在 content 中追加 aside inspector、第二总览 chart 或磁贴 grid；专属 CSS 使用 paper-/swiss- 命名，不共享兄弟页的 selector 集合。

## 8. Explicit Anti-Patterns & Verification Targets

v01 的失败形态包括：六行被换成 2×3 方舱、详情放到右侧、把虚线库存节点画成活跃路径、四个摘要胶囊只剩四个标题而没有值、hover 依赖点击才出现、卡片向上抬时把第一行盖到页眉、长文件名截断成 navigation…、整页塞满图例与彩色标签。页面不出现沙盒说明、内部状态 select、重复主题/视口控件、Active / Matte 调试条、ruler、caustic 条纹、raw localization keys；Owner 命名里的 L0/L1 与真实脚本名不是要删除的产品信息。

Stage 2 自证必须包含 headless WebKit 1280×800 Light/Dark 初始态、my-designer hover 态、打开 archive 后返回 my-designer 的点击态截图及几何 JSON。测 6 个 data-skill-row、6 个 data-hover-brief、6 个 data-bifurcation-panel 的常驻数量；hover 后 opacity>0、高度≥16px、transform 的 Y=-4±0.5px；展开首抽屉高度 196±4px，首屏第六正面底边≤752±4px。用 MutationObserver 只监测 childList removedNodes，在 hover、连续切换、冷分支点击、Esc 和主题切换整个序列中累计 removedElements=0；确认闭合 panel inert、trigger aria-expanded 正确，所有有效 branch 都是 M/C/L/C/Z 填充路径且描边不超过 24。数值、脚本成功率、Eval 归因与输入值逐字核对，未知不得变零，root 无水平溢出。独立 Visual Traceback 只由上游 Reviewer 执行；本文件是 Stage 1 设计交接，不声称页面已渲染验收。
