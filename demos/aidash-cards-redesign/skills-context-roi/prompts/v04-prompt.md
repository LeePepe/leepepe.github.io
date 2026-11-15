# v04 · 先治冷枝的红黑榜抽屉 (topology-governance-triage-drawers)

## 1. Visual Metaphor, Palette & Anti-Clone Spatial Lock

先画一张有裁决顺序的治理账页，不先画一个炫目的总流量仪表。上层两张半开警报卷宗明确回答「哪个技能现在需要处理」，下层四张健康主力卷宗回答「哪些可以放心继续用」，底缘是需要时才抽出的证据盘。平台 web，沿 macOS 检查器的可逆阅读惯例；设计锁定 VS-008 的编辑式分区 × CL-002 的赤陶/酒墨治理变奏，X 为风险优先、Y 为警报棚与双栏主力棚、Z 为半开警报和上抽证据盘。没有左侧master rail，也没有顶半屏通用workspace chart；不要把 v03 网格简单换成红色。

Light 总底 #FBF9F5、健康棚 #F1EEE7、卷宗 #FFFEFA、深酒墨 #35272C，辅助墨 #766970；Dark 总底 #171516、卷宗 #292226、健康棚 #211D20、选中证据盘 #332930、文字 #F5EBEE。品牌性标题用酒红 #9D4057，非语义的分区线用陶灰 #B9A8A1。琥珀、珊瑚、翡翠和紫色只服务健康分类，不把所有健康卡染成整块绿色。主标题24px系统serif、问题标题16px system-ui semibold、技能名13px、指标11px等宽；上层角14px、下层角8px，账页用左对齐语句、留白与短横线而非徽章墙。仅本版Writer手写 v04.html，triage-/flagship-是其私有样式词汇，禁止引入其余候选的布局CSS。

## 2. Single P0 Focus, Semantic Status Colors & Initial Showcase State

唯一 P0 是「确认哪条治理建议应进入待核对清单」，不是展示某个综合ROI分数。初始上棚左为 archive-deck-helper 的「🧟 30d 零调用 · 建议归档」，右为 my-designer 的「⚠️ remotion-video.md 0 命中冷门冗余」，两张都呈半开状态，露出实际问题和动作入口；底证据盘先收起，以保留四张主力完整正面。右警报附 P95 480ms 的已知脚本读数，但称「复核耗时」而非凭空宣称违反某个未设定SLO。首次点右警报就应看见完整分岔与评测/脚本收据。

archive 的边签为 #8B5CF6，逃逸标为 #F43F5E，并正面保留「7d 0 次 · 30d 0 次 · 逃逸 3」；my-designer 的问题脊为 #F59E0B，不将它错误归到健康下棚。下棚只放team-lead、m2-dispatcher、linear-board、design-studio，四张用 #10B981 与「主力健康」；这纠正了旧domain/T5列举把my-designer放到下棚的冲突，以R5 Designer B明确两警报+四健康的划分为准。警报强度由左签与标题表达，卡正文保持中性可读，不用红底+白字铺满252px卷宗。

六个正面均有四类指标：①7d/30d调用、活跃会话、30d零调用判定；②L0 (SKILL.md) Token、L1平均连带Token、Cache 96.8%；③scripts/*.py次数、平均/P95 ms、成功率%；④eval-cases.json用例数(+本周新增)、通过率、拦截和逃逸及归因。my-designer展示例可写42/156次、28会话、1.8k/+3.4k tok、Eval24(+4本周)、100%通过、拦截19/逃逸2 [1 IMPL_BUG / 1 SPEC_GAP]。其余未批准的数据保留「待采集」字段，归档技能的0调用也不能推导出0Token、0ms或100%通过率；警报卷宗不是只放一行大字然后省掉指标。

## 3. Hover Brief Preview ([data-hover-brief]) & Click-to-Pull-Out Bifurcation Drawer ([data-bifurcation-panel]) Contract

[data-skill-row] 的每张卷宗都拥有一个 [data-hover-brief] 与明确 button[data-skill-trigger]。hover使卷宗translateY(-4px)，在下边缝露出单行诊断；archive文案「治理快览：30d 零调用 · 逃逸3 · 建议核对归档」，my-designer文案「治理快览：remotion-video.md 0 命中 · design_catalog.py P95 480ms」。四张主力以自己最高命中Reference/Script及建议生成，缺数据写「治理快览：主力健康 · 资产明细待采集」。简介既不遮动作按钮，也不替换常驻问题说明；focus-within和touch选择同样能读到。

主卷宗点击负责打开底部证据盘，治理动作按钮负责自身状态，事件必须stopPropagation避免「标记」误触展开。archive的主动作是「标记待核对」，my-designer是「查看冷分支」，旁边小动作「复核脚本」定位design_catalog.py表行。标记动作将当前skill的治理建议写到独立localStorage键aidash-r5-b-v04-governance的待核对集合，显示「已标记待核对 · 尚未归档」与可撤销入口；刷新后还能恢复这项真实本地标记。没有生产归档API时绝不模拟文件已删除、Skill已归档或Linear issue已创建；不请求网络、不更改真实技能目录。再次点击可撤销，存储失败则给「未保存标记 · 请重试」，不能报成功。

底盘预置6个article[data-bifurcation-panel]，打开哪一技能就呈现其自身Prompt→SKILL.md→Reference/Script结构与Eval收据；同一trigger再点收回，另一个trigger改变active panel。盘从收起64px上抽到396px，覆盖下棚健康卡但不挡上棚两警报，关闭后下棚原位恢复。被覆盖底卡不可接收Tab，当前证据盘内按钮与上棚可操作；Esc解除支路锁定后再收盘并回原trigger。全流程removedElements = 0，保持6个卷宗和6个证据article在原父节点，禁止删掉被标记卡、替换SVG、innerHTML重建或通过router换一个虚构治理页面。

## 4. Measured 1280x800 Viewport Geometry & Spatial Bounding Boxes

以1280×800 CSS px作验收靶。content横区x=64..1216，triage-board-header=(64,28,1152,44)，governance-alert-shelf=(64,88,1152,252)。两警报卷宗各568×252，中缝16px，archive在x64，my-designer在x648。每张padding16，顶标题24px、问题说明28px、2×2指标格92px、治理动作32px、hover缝18px，剩余26px用于组间间隔；这些是可用高度账，不得将252px大半拿去做装饰图标。

flagship-two-col-shelf=(64,356,1152,316)，二列568px、行高150px、行缝16px。team-lead/m2-dispatcher在y356，linear-board/design-studio在y522，结束y672。每个主力正面标题22px，四类指标逐行14px、Eval归因14px、hover18px，内距14px；健康卡不另塞小图或4个浮夸进度环。下棚四张是独立可抽的卷宗而非正文table，也不要改成6张等大bento卡。

triage-bifurcation-dock收起时位于(64,688,1152,64)，前44px是选中技能/「展开证据」/关闭入口，后20px给窗口与覆盖提示；展开时同一外框的top从688到356、height从64到396、bottom持续锁定752。展开内容标题(84,368,1112,28)，分岔SVG(84,404,1112,224)，Eval与脚本收据(84,640,1112,96)。这是覆盖下棚的单证据盘，不是把整体网页撑到1100px再声称一屏可见。初始无任何覆盖时必须看见全部6个技能正面。

图viewBox=0 0 1112 224，左意图区0..220、L0枢纽300..488、分流空间488..748、出口文字756..1108。入口中心y=42/102/162，Reference四出口在14/45/76/107，Script三出口在138/169/200；文件名与数字两行排，单位整段保留。盘底table将名称、次数、avg、P95、成功率依次用共享列宽420/104/160/160/180与88px内距配齐，三脚本行各20px，上方Eval收据24px；窄屏可在盘内滚表但不能把header和row分成不同grid。<1000px时上棚和下棚分别改单列、证据盘变自然流展开，禁止保留桌面绝对position造成内容遮挡；根宽不横溢，touch target≥44px。

## 5. Dual-Theme Surface Polarity & Filled Cubic-Bezier Ribbon Craft

治理账页是实心内容，不用backdrop-filter、折射滤镜或发光雾盖住数字。警报卷宗顶部只留一条半开缝和轻内高光，Light用inset 0 1px 0 rgba(255,255,255,.9)及0 4px 12px rgba(72,38,44,.05)，Dark则inset白.06、下影黑.16。上警报/下主力/证据盘通过不同亮度与角尺度分层；主动作可以有酒墨实底，但全屏不超过一个高强调治理CTA。语义亮色仅用于图形，字用深翡翠/深琥珀保证4.5:1；Dark的浅字对深红底同样需测，不靠颜色名宣称通过。

证据盘的光带像审阅线索分成两束，而不是监控中心的蓝色电路。合法闭合样例为 <path data-branch="triage-navigation-review" d="M 488,97 C 588,97 650,70 744,70 L 744,81 C 650,81 588,108 488,108 Z">，用于有正命中的普通Reference支路；cold节点不套这条正宽样例。fill来自triage-前缀的暖灰→琥珀/酒墨linearGradient，stroke-width=.75，所有有效branch都满足M C L C Z和stroke-width<=24，不用大笔刷stroke画管子。意图的3条细束汇入SKILL.md后，右侧按Reference与Script两组标头分岔。

文件组保留navigation-evidence-contract.md (62% · 2.4k tok)、interaction-layering.md (28% · 1.6k tok)、appearance-ledger.md (19% · 1.4k tok)、remotion-video.md (0 命中 · 冷门冗余告警)。前三个覆盖是可重叠的命中，不把62/28/19当作总计100%的独立分流；脚本次数也不与Token使用一个宽度分母。remotion的data-branch路径退化为零宽，另用无粒子的虚线库存线与警报签连接，hover或选择让标签更亮但不生成流量。archive没有调用时同样是静态库存/待采集结构，不能给它画满颜色的活跃路径。

## 6. Apple Native Spring Physics & Animated Flow Particles

动作像抽一层审阅托盘：卡hover250ms上提4px，底盘上抽500ms、收回420ms，空间曲线取 cubic-bezier(0.22, 1.35, 0.36, 1)。top和height同时以同一时间线维持bottom=752px，内容从translateY(10px)跟进但不缩放文字，浅阴影在盘接近打开时渐显。警报卷宗不旋转、健康棚不跳动、标记待核对仅让签名颜色/文案变化，不以弹走整张卡表示删除。

暖灰流带的动态比studio收敛：仅当前选中有效Reference/Script支路各1颗1.5px光点、周期4.2s，脉冲由独立的细centerline stroke-dashoffset实现，主路径fill不闪烁。冷门文件、归档skill和缺失流量边完全静止；治理警报使用稳态珊瑚/琥珀，不持续呼吸去强迫注意。P95读数不决定粒子速度，标记行为不修改任何调用计数或缓存命中率。

prefers-reduced-motion下托盘瞬时到位或100ms淡显，停止全部位移过冲/粒子；存储标记的成功和失败照样有明确文字反馈。连续选择不同证据盘不排队动画，最新选择替换active dataset；pointerleave只结束预览不收盘。使用2px focus-visible边框，盘关闭后先取消inert再归还焦点，避免焦点落在遮盖的健康按钮或底盘零高度内容。页面隐藏时暂停已选分支光点。

## 7. Production Data Inventory (Zero S1-S12 Jargon) & Exact DOM Topology

治理是否有依据取决于上游物理链路：L1_collect/raw保留路径与事件、L2_normalize清洗、L3_merge事实/库存、L4_serve的SQL诊断、L5_apps canonical skills_roi_snapshot.py产出JSON供AIDash读取。本次检查/Users/lee/Development/AIDash/aidata的inspect_aidata_pipeline.py返回reference_hits、script_latency、eval_effect=needs_l1_collection；所以本轮Owner提供的0命中、0调用及逃逸只是已批准展示样例，不能被当成本次查证的实时治理判决。保存标记只是本地阅读清单，不声称完成生产归档；实际采集与生产绑定留给上游aidata-metric-extension任务，leaf Designer不改代码或数据库。

数据层将Owner输入与observed值分开记录provenance，production保持coverage_status、window、source_as_of。判30d僵尸需有完整窗口+skill库存，判0命中冷Reference需有文件库存+路径采集覆盖，不能把null当0。旧fact_turn.tool_calls工具名字数组不足以证明某具体.py的P95，Eval库存总数也不等于执行通过率。cache的展示数96.8%只是规格样例，不将archive的未知cache贴成高命中；已知逃逸3不能擅自拆成1 IMPL_BUG+2 SPEC_GAP，未给分解则显示「归因待核对」。

设计技能的具体路径是UI探索画廊48%/实现后截图回溯34%/规范审计18%进入SKILL.md (L0 入口 · 1.8k tok)，然后到四份已知Reference和三个已知脚本：design_evidence.py (46次 · P95 310ms · 98.5%)、design_catalog.py (39次 · P95 480ms · 100%)、verify_design_cases.py (18次 · P95 190ms · 100%)，均值各待采集。卷宗详情提供eval-cases.json用例总数、本周新增、通过率、拦截/逃逸与已知[1 IMPL_BUG / 1 SPEC_GAP]。另五个技能各持自身bifurcation_routes/scripts/references/eval，不把设计技能文件借给健康主力；缺实际资产时照样打开完整两组分岔框架，说明路径待采集而不编造文件名。

根树按main.topology-governance-triage-drawers > section.content建立，直系子项依次header.triage-board-header、section.governance-alert-shelf、div.flagship-two-col-shelf、section.triage-bifurcation-dock。alert shelf仅有2个article[data-skill-row]，flagship shelf仅有4个article[data-skill-row]；六个article都含trigger、四类摘要和hover brief。dock内持6个article[data-bifurcation-panel]，各具.triage-evidence-flow与.triage-script-eval-receipt，外部shell统管展开几何。没有额外overview-crown、skill-drawer-rail或inline-pocket-stack，故结构与同组其他候选由真实父子角色和位置辨识，非顶级class名作假。

## 8. Explicit Anti-Patterns & Verification Targets

本版不得把my-designer从警报棚偷塞进翡翠主力棚；不得把archive删掉来掩盖30d僵尸；不得将「标记待核对」伪装成真正归档；不得因为P95 480ms就凭空编出服务阈值或更高耗时；不得在初始态用底盘盖住四主力。彩色签、完整四类数字和一键入口要同时成立，不能只剩大号骷髅图标。所有长Reference、脚本名、调用数、百分比和归因都不省略；不要无效href="#"、沙盒声明、内部state select、双份theme/gallery控件、ruler/caustic条纹、Active / Matte调试bar或抽象学术编号。

Stage2以headless WebKit先测1280×800双主题初始矩形：2警报各568×252、4主力各568×150、dock闭态64px且最下≤752px；hover任一卡的brief opacity>0、高≥18px，lift=-4px。然后点my-designer看dock高396±4px/top356±4px、完整7出口及脚本/Eval表；点cold分支和复核脚本确认定位正确，点archive确认不制造活跃流量；关闭后4主力rect相对初始漂移≤1px。标记→刷新→撤销验证localStorage真实持久与可逆，测试存储异常不报假成功，计数和文件完全未改。MutationObserver在整序列包括主题切换累计removedElements=0；检查6个hover/6个panel、有效path闭合C/L/C/Z、stroke<=24、冷边没有粒子、数字不截断、header/row对齐、根无水平溢出与键盘/Reduced Motion正常。Writer提供截图和记录，后续独立Reviewer执行Visual Traceback；本交接仅完成Stage1设计，不代为发布或归档生产资产。
