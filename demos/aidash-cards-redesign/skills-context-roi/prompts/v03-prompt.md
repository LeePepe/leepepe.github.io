# v03 · 光流冠层与六枚技能舱 (topology-top-flow-bento-drawers)

## 1. Visual Metaphor, Palette & Anti-Clone Spatial Lock

构图像一张俯视的分析桌：上方一整片光流冠层提供路径方向，下方六枚宽扁技能舱按2列3行排列。眼睛先看流向，再用手指指认某舱，最后才抽出该舱的深度页。平台为 web 单屏交互，借 macOS 的 hover/焦点习惯；方向坐标是 VS-007 的数据桌 × CL-008 的淡雾/靛青变奏，X 为总览到选中、Y 为上图下格、Z 为顶层功能镜片和实体磁贴。这里没有任何常驻左侧轨道，也不接受六个全宽纵列作为替代。

Light 画布 #F5F7FB，磁贴实面 #FFFFFF，分区衬底 #EDF2F9，正文 #182339；Dark 画布 #0F1420，舱面 #1B2437，图场 #141D2E，明字 #EDF4FF。非状态路由色用发光青绿 #2DD4BF 与靛青 #818CF8；琥珀只保留给真正的冷分支。只在 flow-crown-header 的功能薄层使用淡雾玻璃，卡面与图纸都是不透正文材质；不能把六个内容卡都刷 backdrop-filter 变成一片浑浊。标题 23px system-ui semibold，技能名13px、指标11px等宽、辅注11px；轮廓偏圆润的18px舱角区别于纸版12px与观测室9px。专属 Writer 独立实现 v03.html，选择 crown-/bento- 前缀而非通用共享.card样式。

## 2. Single P0 Focus, Semantic Status Colors & Initial Showcase State

唯一 P0 是「指向一枚技能舱，立刻看见它在顶部的披露路径」。初始状态是全仓结构总览：6个SKILL.md库存枢纽可见，my-designer 的已给定展示路径作为清晰的示范束，其他技能没有批准流量的地方保持待采集轮廓；深度页不遮挡底部网格。图的上下文注明当前可读数据范围，不能将 my-designer 48/34/18 的意图占比伪装成全仓汇总。P1 为每个舱的4类指标摘要，P2 为点选后出现的深度收据；总体印象是一个上图/下舱的双层桌，不是六张独立图表。

my-designer 左上舱以 #F59E0B 的角灯和「L1 偏高 · remotion-video.md 0 命中」提醒；team-lead 右上、design-studio 左中、m2-dispatcher 右中、linear-board 左下均以 #10B981「主力健康」标识；archive-deck-helper 右下用 #8B5CF6 的库存封签和 #F43F5E 的逃逸角标，完整写「🧟 30d 零调用 · 建议归档」「7d 0 次 · 30d 0 次 · 逃逸 3」。青绿/靛青是图场路由光，不改变这三个健康语义类别。色灯、文案、SVG形状三者共用状态，不能单靠颜色区分僵尸与健康。

舱面仍要显示调用7d/30d与活跃会话、L0 (SKILL.md) Token/L1 平均连带 Token/Cache 96.8%、scripts/*.py 次数/均值/P95 ms/成功率、eval-cases.json 用例数(+本周新增)/通过率/拦截与逃逸。my-designer 可按Owner展示例排入42/156次、28会话、L0 1.8k/L1 +3.4k tok，Eval24(+4本周)、100%通过、拦截19/逃逸2，归因[1 IMPL_BUG / 1 SPEC_GAP]。未知的健康技能数据只填待采集，照样保留摘要槽位；archive的L0/L1、Cache、脚本平均耗时和Eval通过率也不能从0调用推断为0或100%。四类摘要有真实字段和值状态，不是四个只写名词的装饰标签。

## 3. Hover Brief Preview ([data-hover-brief]) & Click-to-Pull-Out Bifurcation Drawer ([data-bifurcation-panel]) Contract

每个 article.skill-bento-pod[data-skill-row] 内有 [data-hover-brief] 与 button[data-skill-trigger]。pointerenter 将 .bento-face 舱体正面抬至 translateY(-4px)、底部18px简介亮起，同时在冠层将与 hoveredSkill 对应的 [data-branch] 填充增亮；pointerleave 移除暂态高亮并恢复此前 selectedSkill，不覆盖用户的点击锁定。my-designer 简介用「快览：navigation-evidence-contract.md 62% · 冷门 0 命中 · P95 310ms」，archive用「快览：30d 零调用 · 逃逸3 · 归档前核对依赖」。其他舱以本技能最高频资产命名；没采集路径就显示「快览：主力健康 · Reference / Script 明细待采集」，不能借用设计技能的资产假装命中。

点击舱触发两处互锁变化：顶图由总览滑入该skill的常驻 article[data-bifurcation-panel]，下方拉出其常驻 .bento-depth-sheet[data-skill-detail]。六个panel始终属于 top-workspace-flow-stage，六个detail sheet始终属于各自pod，不搬DOM。深度页以网格内的覆盖抽屉出现，不再插入第七张tile；页面保留上方流向区域，底网格被收据暂时覆盖，盖住的兄弟舱设置inert。收据标题给选中技能、可见关闭按钮与四类摘要锚点，点击顶部库存hub仍可在六技能间切换，关闭则返回完整2×3视图和原trigger焦点。

三种读态清楚区分 overview、hoverPreview(skill)、focused(skill)。没有鼠标的设备先触发真实选择，不用依赖hover解锁详情；键盘focus在舱上也高亮冠层并显简介，Enter/Space才提交focused。点击[data-branch]固定该文件/脚本并更新本skill收据，click cold reference不会触发删除。Esc先取消支路锁定，再关深度页回总览。所有状态只改dataset、文本节点和样式，SVG defs、分支、表格与sheet常驻，removedElements = 0；主题切换也不重新挂载页面。

## 4. Measured 1280x800 Viewport Geometry & Spatial Bounding Boxes

1280×800 的内容横向区间为64..1216。flow-crown-header 置于(64,24,1152,44)；top-workspace-flow-stage 为(64,84,1152,284)，下方bento-skill-pod-grid 为(64,382,1152,374)。网格列宽568px、中缝16px，行高118px、两道10px行缝；六舱左上坐标为(64,382)/(648,382)、(64,510)/(648,510)、(64,638)/(648,638)，最下结束756px，governance-bar在y=768..790。上图下格的几何占比由这些实测框约束，不套44%/56%口号后任意改高度。

每舱12px内距，顶部16px技能名和状态，接下来四条12px指标行，Eval归因再给独立12px附行，最后18pxhover缝；16+48+12+18+24=118px，按border-box计量。metric区域跨度544px，允许11px/12px字体下的脚本次/均/P95/成功率一行；长Eval归因不得挤到右角灯下。名称不跨出568px边界，脚本名完整保留在简介/详细收据，正面均值与P95有单位。最下方舱hover抬起不会越出图框或压到footer。

冠层内的标题/范围条为y=96..120，SVG图纸为(84,128,1112,224)，viewBox=0 0 1112 224。overview以六个L0库存hub表示整个技能清册，只有已批准的my-designer样例连出活跃束；focused视图采用左意图区x=0..224、L0 hub x=304..476、曲线走廊x=476..744、文件标签x=756..1108，右出口中心y=14/45/76/107/138/169/200，三个左入口中心y=42/102/162。每条输出文件名与元数据分两条11px/12px行，宽352px可完整排下navigation-evidence-contract.md；不能把7节点压成3个彩点。

深度收据的展开框在content坐标内固定为(80,426,1120,316)，动画只从y+20到原位。它覆盖下部舱体，但不遮冠层；标题32px、四摘要24px、脚本表/冷分支说明212px、关闭回执24px和内距共316px。关闭时这6个sheet都是零可见面积且inert，不影响网格算行。外层 article.skill-bento-pod 保持 position:static、无transform且不裁剪后代，.bento-depth-sheet 以 position:relative 的 section.content 为绝对定位包含块；hover的transform仅施加到其兄弟 .bento-face，避免磁贴变换把全宽sheet锁进568px局部坐标。底层pod保持原坐标供回归比对，选中项通过sheet标题重新建立阅读锚，不强行让被覆盖原卡还可点。窗口变窄至<1000px改为单列舱、整页纵滚；展开sheet改为卡下自然流详情而非桌面绝对覆盖，图表最低1000px宽只在figure内部横滚，root不可横溢。手机触控控件至少44px。

## 5. Dual-Theme Surface Polarity & Filled Cubic-Bezier Ribbon Craft

雾玻璃仅用于顶栏的功能镜片：背景采用透明度0.72的浅/深中性薄层、blur 14px、saturate(120%)，1px内高光，不叠第二个采样玻璃。若实现光学折射，Blink可用IOR1.5、12px bevel、最大6px位移的弱镜片，WebKit退化为soft radial rim和实体浅雾底，不能宣称CSS blur等价原生光学。prefers-reduced-transparency下顶栏变全实面。下方磁贴全部solid，只在边缘有青绿/靛青轻量环境光，不能透出另一磁贴或整幅流图。

顶图要像薄光带展开成纸扇，而不是荧光水管。一个合法示例是 <path data-branch="crown-navigation" d="M 476,94 C 566,94 660,9 744,9 L 744,20 C 660,20 566,105 476,105 Z">；fill为crown-唯一渐变从teal到indigo，边stroke-width=0.6，阴影光晕alpha≤.12。各有效支路都含M、两段C、L与Z闭合；禁止把stroke-width放大到24以上，实际薄边≤1px。左侧UI探索画廊48%、截图回溯34%、规范审计18%的三束先入SKILL.md，再向文件组和脚本组分出，不绕过hub直达右端。

navigation-evidence-contract.md (62% · 2.4k tok)、interaction-layering.md (28% · 1.6k tok)、appearance-ledger.md (19% · 1.4k tok) 作为文件覆盖指标并列，明确同一会话可多次披露所以不要求占比守恒；scripts的执行次数拥有另一局部带宽标尺。remotion-video.md (0 命中 · 冷门冗余告警) 则保留零宽闭合branch和淡虚线库存关联，无活跃填充、无光粒。top总览不能给未知技能画同样粗的正流量，美术库存连接必须标成待采集而不假装真实访问轨迹。

## 6. Apple Native Spring Physics & Animated Flow Particles

该版节奏分为「感知联动」和「提交抽出」：hover抬舱220ms，冠层支路增亮120ms，点击的top focus切换460ms，收据上滑500ms，都在空间动画使用 cubic-bezier(0.22, 1.35, 0.36, 1)。投影从0 3px 10px变0 10px 22px，hover绝不旋转tile；selection收据从translateY(20px)与scale(.99)回原位，透明度另用ease。未选中舱不用整体缩小来制造舞台聚焦，因为那会改变实际网格几何。

冠层每束允许一颗2px微光和10px衰减尾迹，沿单独的cubic centerline在3.4s内走完；teal入口脉冲到L0后再沿indigo出口光带流出，错相是美术节奏而非声称某次真实调用。hover只改亮度、不突然加速。未知/冷分支粒子数为0，archive图保持安静库存状态；summary覆盖率、Cache和P95均为静态值，不通过粒子速度去暗示实时变化。

prefers-reduced-motion 减少动效模式停止所有animateMotion与dashoffset，取消升起、缩放和弹簧高低变化，改为100ms显隐并保留状态边线。离屏冠层暂停loop。快速从左上hover到右下不改变focusedSkill，关闭详情后清理hover残留但保留键盘原焦点。focus ring不被舱的overflow裁切，背景grid inert与当前sheet/顶部hub之间形成明确键盘通路，不制造无法退出的焦点陷阱。

## 7. Production Data Inventory (Zero S1-S12 Jargon) & Exact DOM Topology

冠层数据必须从模型契约驱动，而不是凭SVG造一张漂亮伪图。本轮在真实~/Development/AIDash/aidata通过inspect_aidata_pipeline.py查看物理L1–L5，reference_hits、script_latency、eval_effect都为needs_l1_collection；总览可诚实展示库存结构与Owner样例，不能声称已有全仓路径遥测。上游扩展蓝图的fact_skill_ref_read/fact_skill_script_exec/dim_skill_inventory仍属待实现合同；L4聚合再由L5 canonical skills_roi_snapshot.py输出到AIDash，Writer不得绕到UI把这些采集缺口写死。

载荷的必要维度为skills六对象、calls_7d/calls_30d/active_sessions_30d/is_zombie_30d、l0_tokens/l1_avg_attached_tokens/kv_cache_hit_pct、script调用次数/均值/P95/成功率、eval用例总数/weekly_delta/pass_rate/intercepted/escaped/escape_breakdown、references命中与Token、bifurcation_routes和scope。Owner数字单独标provenance=owner_spec_example；source_as_of、coverage_status、window从生产Snapshot原样带到范围说明。缺失用待采集，零仅表示已证实零；Cache示例96.8%不应成为每个技能的强制真实值。活跃会话是30d去重会话，Reference覆盖也需同窗分母，不能拿指针hover计入调用次数。

my-designer的意图/文件样例只属于该技能，SKILL.md hub标L0入口1.8k tok；脚本名单完整为design_evidence.py 46次 · P95 310ms · 98.5%，design_catalog.py 39次 · P95 480ms · 100%，verify_design_cases.py 18次 · P95 190ms · 100%，各avg待采集。其Eval样例24用例(+4本周)、100%通过、拦截19/逃逸2 [1 IMPL_BUG / 1 SPEC_GAP]。其他技能点开时必须看到自身的Prompt→L0→Reference/Script分岔结构，未获真实具体文件就显示路径待采集槽位，而不是偷偷复制这7个输出；归档样本0/0与逃逸3不等于该技能没有库存文件。

content直接孩子按此树固定：main.topology-top-flow-bento-drawers > section.content > header.flow-crown-header、figure.top-workspace-flow-stage、section.bento-skill-pod-grid、footer.bento-governance-bar。figure内一个.overview-crown和6个article[data-bifurcation-panel]共用一块图场；grid内严格6个article.skill-bento-pod[data-skill-row]，各含.bento-face、button[data-skill-trigger]、[data-hover-brief]与自己的.bento-depth-sheet[data-skill-detail]。deep sheet不是另一个data-bifurcation-panel，完整分岔始终驻顶，详细Eval/Script收据才在底部抽出。各候选的结构签名须按角色和父子关系区分，本版2×3网格是真实CSS grid而不是用六行改名字。

## 8. Explicit Anti-Patterns & Verification Targets

冠层版本拒绝：把上图换成小小logo；用6份相同my-designer路径冒充全仓；hover抬舱却不联动上图；hover直接打开底部详情；grid实际是3列2行；drawer在打开时物理挪走card或SVG；玻璃内容采样玻璃chrome；全页teal/amber渐变淹没语义；数字省略与文件名截断；点击关闭后sheet仍挡住grid。页面没有测试state select、sandbox文案、重复gallery controls、ruler、caustic斑马纹、Active/Matte面板或内部学术编号。

WebKit 1280×800以Light/Dark各拍overview、hover my-designer、click my-designer并选remotion冷支、切archive再关闭四组状态，另存测量记录。第一屏6个tile必须为两列三行，x为64/648±4、y为382/510/638±4；top图高284±4，hover简介至少18px且opacity>0、.bento-face 的Y变换=-4px、外层pod坐标不变，对应branch亮度实际变化。click后选中panel可见、图scope只属该skill、sheet占1120×316±4且不遮top；close后6个tile的rect恢复原值。观察childList移除总量removedElements=0、冷branch无正宽填充与粒子、完整有效路径含C/L/C/Z且stroke<=24。核验每舱五类指标入口与数值/待采集区分、7个已知输出标签可读、Eval拦截逃逸归因齐全，Reduced Motion和键盘Esc/Tab正常。B4截图审查是后续Reviewer职责，本prompt不伪造任何已完成的HTML或视觉验收。
