# v02 · 深蓝分岔观测室 (topology-sankey-studio-split)

## 1. Visual Metaphor, Palette & Anti-Clone Spatial Lock

这次不是纸袋阅读，而是一间仪器工作室：技能像六个可抽取的样本匣，固定在左侧窄轨；取出任意样本，右侧整块深蓝观测屏开始解释它的 Prompt、入口文件、Reference 与执行脚本。空间坐标锁定 web 承载、macOS master-detail 操作，VS-003/VS-007 的精密观测语言 × CL-008 的冷海军蓝变奏；X 是样本选择、Y 是左右隔离、Z 是样本匣微浮与同位舞台交叉滑入。右屏占 62%，不能降格成卡片下方的一截小抽屉。

Dark 的总背景必须 #0C1220，匣体 #172238、舞台 #101B2D、台底表格 #152037，主字 #EAF2FC，次字 #A1B2CB；Light 使用 #F2F6FC、#E5ECF7 的轨道衬底、#FFFFFF 舞台、#DCE5F2 dock 和 #14233B 文字。图的非语义连接种子为冰蓝 #60A5FA，选中匣仅有钛蓝边光，不抢健康与警报色。系统字体 13px、舞台标题 22px、数值 11px 等宽；不使用 serif、奶油纸张、印刷封条或玻璃磁贴。Writer-b-v02 仅拥有 skills-context-roi/v02.html，自写 studio- 专属 CSS，尤其不可把 v01 的六个行内详情搬到右边就算新设计。

## 2. Single P0 Focus, Semantic Status Colors & Initial Showcase State

打开页面时左轨已有六张实匣，my-designer 高亮，右屏直接呈现「L1 去向与冷分支」大图，用户的唯一 P0 是在流带上定位值得治理的 remotion-video.md。图中的冷文件标签留在 Reference 组末位；脚本耗时与 Eval 收据固定在舞台底缘而不是生成第二套 KPI 大卡。P1 是左轨的四类五行摘要，P2 是点选路径的采样/覆盖细节与逐脚本表格；工具配置不占本视口。

状态灯沿左匣上缘而非 6px 纸脊：team-lead、m2-dispatcher、linear-board、design-studio 标 #10B981「高频健康」；my-designer 标 #F59E0B「L1 Token 偏高」，并显 remotion-video.md 0 命中；archive-deck-helper 标 #8B5CF6「🧟 30d 零调用 · 建议归档」，其逃逸 3 用 #F43F5E 独立角标。归档匣仍在轨上，不能通过过滤让它消失。警告是语义读数，不允许把整幅海军蓝改成红幕；同色浅底纹最多 14% 透明度，文字与图形都能说明状态。

每张匣的摘要按五条细线排版：调用行提供「7d / 30d 次数 · 活跃会话 · 僵尸判定」，Token 行提供「L0 Token · L1 均值连带 Token · Cache 96.8%」，Script 行提供「scripts/*.py 次数 · 均值/P95 ms · 成功率」，Eval 行提供「eval-cases.json 用例 (+本周新增) · 通过率 · 拦截/逃逸」，末行提供 [1 IMPL_BUG / 1 SPEC_GAP] 等已知归因。采用 Owner 示例时 my-designer 为 42/156 次、28 会话、1.8k/+3.4k tok，24 用例 (+4 本周)、100% 通过、拦截19/逃逸2；archive-deck-helper 必须有 7d 0 次 · 30d 0 次 · 逃逸 3。其余技能没有批准数字的字段以短横加「待采集」说明，不能给它们捏造具体收益、会话、通过率或脚本样本。

## 3. Hover Brief Preview ([data-hover-brief]) & Click-to-Pull-Out Bifurcation Drawer ([data-bifurcation-panel]) Contract

左匣内预置一个 14px [data-hover-brief] 带，hover 只让匣体 translateY(-4px) 并显带，不改变左轨行距或选中项。my-designer 的紧凑单行用「诊断：design_evidence.py 46次 · 冷门 0 命中」，完整 Reference 名字在右图可读；健康技能显示本技能最高频 Reference/Script，未知时直述「诊断：健康主力 · Reference / Script 待采集」；归档匣显示「诊断：30d 零调用 · 逃逸 3 · 核对归档」。pointerleave 恢复微浮，焦点进入也可获得同等预览，不能把预览藏在 browser tooltip。

[data-skill-trigger] 是每张 article[data-skill-row] 的真实 button；按钮触发后右侧已驻留的对应 article[data-bifurcation-panel] 从内凹位置向前滑入。维持 selectedSkill 与 hoveredSkill 两个状态，hover 不得切换右图。相同按钮再次激活把右图降为该技能的收起轮廓与「展开分岔」入口，不挤压舞台尺寸；选择另一技能直接切入该技能展开态。aria-controls 指向唯一 panel，其他五个 panel 为 inert 且不接收键盘。

六个右图 panel 从首帧就具有 SVG、文件标签与 table，均绝对定位在同一 .sankey-full-stage 坐标系。通过 opacity/transform/visibility 和 active dataset 实现互斥，关掉指针命中与 tabindex；全程 removedElements = 0，不能重新 append 选中图、清空 table 或用字符串 HTML 重新绘制。右图的 [data-branch] 与对应标签可以 hover 高亮、click 固定读数；表格联动只更改常驻行的 selected 状态。Esc 从支路回全图，再从展开图回轮廓，最终焦点归还左匣按钮。

## 4. Measured 1280x800 Viewport Geometry & Spatial Bounding Boxes

1280×800 内边界为 x=64..1216。studio-top-bar 是 (64,28,1152,40)，sankey-studio-grid 从 y=84 延伸到 y=772，总高 688px。左 skill-drawer-rail 为 (64,84,422,688)，中缝18px，右 sankey-full-stage 为 (504,84,712,688)；可用列宽按约 38%/62% 分配，百分比不包含列缝。六张匣各108px，高度和8px间隔之和为 6×108+5×8=688；起点 y=84、200、316、432、548、664，最后结束 y=772，footer 为 y=780..794。右图再丰富，也不得使任何左匣坐标上下移动。

匣体左右内距12px，首行18px 容纳 skill 名与灯标，之后70px 容纳五条14px摘要，最后14px 用于预览，余下6px 分摊上下内距；重要数字整段显示。不要改成四个2×2大胶囊，那会使6匣超过屏高。脚本摘要可以写「脚本 46次 · 均值待采集 · P95 310ms · 98.5%」，完整脚本名在 hover 和右侧表中出现；Eval 第五行分离长归因名称。小样本字段为空并不取消这一摘要行。

右 panel 内标题 (524,100,672,28)，图框 (524,136,672,408)，底 dock (524,560,672,192)。SVG viewBox=0 0 672 408：左意图区域 x=8..164，枢纽 x=196..320，连接通道 x=320..424，输出标签 x=432..664；三入口中心 y=94/190/286，L0 中心 y=184。Reference 标签中心 y=48/98/148/198，Script 标签中心 y=270/322/374，每个输出保留文件名一行、元数据一行，长 basename 在232px标签宽内采用11px等宽字体，允许局部两行而不裁剪路径。

dock 上半部是一行 Eval 完整收据，底部 table 为三条脚本行；列宽按名称248、次数56、均值96、P95 96、成功率112、剩余内距64统一，header 和 body 使用同一 colgroup。没有冗余 P95 条形图再抄一遍相同表格。小于 1000px 的容器才转为上轨/下舞台，轨道使用独立纵滚且保留每匣足够摘要高度；图保留最小672px在本舞台横滚。触控时预览由焦点/短按选择提供，hover 不是唯一读取通路；页面根宽不允许被长文件名撑开。

## 5. Dual-Theme Surface Polarity & Filled Cubic-Bezier Ribbon Craft

Deep studio 的体积来自冷底、实体匣顶内高光与窄环境光：Dark 匣 inset 0 1px 0 rgba(202,222,255,.09)、0 5px 14px rgba(0,6,18,.18)，选中匣加1px钛蓝半透明描边；Light 下影降到 .06，舞台必须变成真正的白/淡蓝面而非 dark 模式套透明蒙版。匣角9px、观测屏16px、dock仅底边12px，三个容器不共享万能圆角。玻璃折射 IOR/位移在此方案都为禁用；本版用 solid instrument surface，没有后台采样和双层毛玻璃。

桑基轮廓使用填充的两条三次贝塞尔边界来定义丝带，例如 <path data-branch="studio-evidence" d="M 320,180 C 362,180 380,265 424,265 L 424,277 C 380,277 362,192 320,192 Z">。入口半透明冰蓝经灰蓝 hub 转为各支语义色，linearGradient id 必须 studio- 前缀且6个panel互不冲突。边缘 stroke-width 0.8，绝不超过24，更不能用 stroke-width=132 的圆管冒充分岔。选中支提高填充 alpha 0.28→0.58，未选中支降至0.12但仍可辨；标签不跟着一起变到不可读。

Reference 分组显示 navigation-evidence-contract.md 62% · 2.4k tok、interaction-layering.md 28% · 1.6k tok、appearance-ledger.md 19% · 1.4k tok、remotion-video.md 0 命中 · 冷门冗余告警。这里文件覆盖允许一会话命中多个，不能把三数强制凑成100%，也不能让 Token 单位与脚本次数共享同一个面积尺度。冷文件的闭合 data-branch 路径设为退化零宽，视觉联系另用不流动的0.8px虚线库存引线；警报标签可点击，但没有正流量和闪烁颗粒。Script 分组用次数决定带宽，成功率独立作为标签而非分流份额。

## 6. Apple Native Spring Physics & Animated Flow Particles

左匣轻提240ms，右屏拉出520ms，退出旧样本280ms；空间变换使用 cubic-bezier(0.22, 1.35, 0.36, 1)。进入 panel 从 translateX(18px) scale(.985) 走向原位，只给屏幕内容微弹，轨道和屏幕外框完全静止。旧 panel 暂留为背景160ms再淡出，避免白闪；过渡中只允许当前panel接收操作。连续切样本时撤销未完成的交叉淡入，以最近一次选择为准，不堆积定时器。

全高舞台允许比纸页更清晰的光粒：每条活跃支路1–2枚半径2px微粒、柔光半径4px，独立 centerline 的 animateMotion 周期2.8s/3.6s错相，合计不超过14粒。流带内部的脉冲高光用细 stroke-dashoffset，主填充路径保持不动。粒子不越出带边、不进入0命中节点、不把 P95 480ms 当作播放速度；播放节奏是视觉扫描辅助，不宣称实时吞吐量。

当 prefers-reduced-motion 生效时，六匣的升降和右屏缩放停用，选中态仅由实体边光和100ms淡入表达；所有光粒/流光冻结为静态路径。页面隐藏或未选中panel的动画必须暂停。键盘可顺序走过6个样本与当前7个出口，focus ring 至少2px、与蓝底有3:1边界对比；常规文字需4.5:1，不能靠高亮粒子替代可读标签。

## 7. Production Data Inventory (Zero S1-S12 Jargon) & Exact DOM Topology

数据证据先于 UI：本次只读 inspector 对 /Users/lee/Development/AIDash/aidata 检查 L1_collect、L2_normalize、L3_merge、L4_serve/queries/retro/skill_roi_diagnostics.sql、L5_apps/digest/skills_roi_snapshot.py；细粒度 reference_hits/script_latency/eval_effect 均报告 needs_l1_collection。所以上述规格数不是实时查出的历史数据，数据适配层须标记 owner_spec_example；生产 source_as_of、coverage_status 和窗口信息只从 canonical Snapshot 保留。原 fact_turn.tool_calls 仅是工具名 JSON，不具有可用于绘图的逐脚本耗时/文件路径。依赖上游 aidata-metric-extension 的采集→建模→SQL→Snapshot 工作完成后才能发布真实监控值。

六个技能对象保持独立 scripts、references、eval、bifurcation_routes 属性，不将 my-designer 的数据填到 team-lead 或 linear-board。30d调用、活跃会话按同一窗口取值；L0文件Token与L1平均连带Token是不同粒度，Cache 96.8% 为Owner视觉样例，未知时应显示「Cache 待采集」。均值/P95缺数据就保留「待采集」而不是0ms，未完整覆盖30d不能自动贴僵尸标签，库存未确认不能用缺记录判冷门；archive 已由Owner明确给出0/0/逃逸3，展示输入必须保留该事实样例。

选中的设计技能意图为 UI 探索画廊48%、实现后截图回溯34%、规范审计18%，hub 标 SKILL.md (L0 入口 · 1.8k tok)。三个脚本表行完整命名 design_evidence.py—46次、P95 310ms、98.5%；design_catalog.py—39次、P95 480ms、100%；verify_design_cases.py—18次、P95 190ms、100%；avg各自待采集。Eval 明细显示 eval-cases.json 用例数与本周新增、通过率、拦截和逃逸 [1 IMPL_BUG / 1 SPEC_GAP]。其他技能的真实分岔若无给定路径就保留两组空结构和「Reference / Script 待采集」，归档样本只画静态库存关联，禁止给零调用画出48/34/18活跃意图。

DOM 的 content 直系顺序限定为 main.topology-sankey-studio-split > section.content > nav.studio-top-bar、div.sankey-studio-grid、footer.studio-status-lip。grid 内左侧 aside.skill-drawer-rail 包含6个 article[data-skill-row]（button[data-skill-trigger]、.studio-metric-lines、[data-hover-brief]），右侧 section.sankey-full-stage 包含6个 article[data-bifurcation-panel]（.studio-screen-heading、figure.studio-flow-screen、.studio-eval-script-dock）。不额外生成隐藏行内抽屉，也不把右侧6个article顺排成6张图；它们是同位互斥面。父子角色树与 v01 的 article内联详情、v03 的上图下格、v04 的警报棚都不同，不以换 class 名伪装独立架构。

## 8. Explicit Anti-Patterns & Verification Targets

观测室一票否决项：左轨跟随右图展开上下跳动；右屏只占38%或变成底部drawer；hover改变selectedSkill造成视觉追鼠；浅色模式仍然是黑屏；7个出口压成一个笼统Reference节点；脚本P95和成功率没有单位；只画粗stroke管线不闭合；为了强光效果把背景持续闪烁；用假归档成功toast改动真实文件。保留正常展开/收起与路径选择，禁止内嵌 gallery 主题按钮、内部测试select、沙盒免责声明、ruler格线、zebra caustics、无意义学术编号及raw翻译键。

Writer 针对本版执行 WebKit 1280×800 双主题截屏：初始 my-designer、hover archive、选中 archive、返回 my-designer 并锁定 design_catalog.py。输出6匣 rect 前后差值，所有 x/y/width/height 漂移≤1px；右舞台测 x=504±4、width=712±4、高688±4；hover带 opacity>0 且高度≥14px，卡 lift=-4px。MutationObserver 累计 removedElements=0，切换后只有一个panel非inert，按钮aria值匹配，Tab不落进隐形panel。静态验证6个hover、6个panel、每个有效path含两次C与末尾Z、stroke-width<=24；表格header/body列对齐误差≤1px、长文件名与数字不省略、root无水平溢出。Reduced Motion、失焦、连续点击与Esc再跑同序列；由独立Reviewer根据截图判IMPL_BUG或SPEC_GAP，本Stage1不代签生产或视觉通过。
