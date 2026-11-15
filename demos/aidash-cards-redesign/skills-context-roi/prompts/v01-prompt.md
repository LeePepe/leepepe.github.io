# v01 · 内嵌航路账 (topology-skill-accordion-manifold)

## 1. Visual Metaphor & Archetype Lock

从 macOS System Settings 的 inset grouped list 提取连续账面，从 Things 3 提取选中项的安静层次：六条 Skill 共享一张纸，展开的流图是纸面里原有的折页，不是第七张卡。平台锁定 desktop，维度 component / chart-dataviz / motion-interaction / layout-navigation；VS-005、CL-006 冷纸 remix、X=整行选取 / Y=单开手风琴 / Z=下沉流图。候选 AppTheme=InsetRouteBook；不是最终产品主题冻结。

标题20px，Skill13px semibold，指标12px/14px，文件名用 SF Mono12px，中文 PingFang SC。只用这四级。24×24 inline SVG 以1.5px currentColor画分岔箭头和档案盒；提示为「点击 Skill 查看意图与文件去向」。不画仪表环，不给每列再套小卡。

## 2. Single P0 Focus & Initial Showcase State

唯一 P0 是 my-designer 行与紧贴其下的完整意图→入口→文件/脚本流。首屏第一行 aria-expanded=true，另外五行折页关闭；六个名称、四组读数和僵尸徽章同时可见。初次选中 navigation-evidence-contract.md，详情带显示「命中 62% · 2.4k tok」。标题「Skills 效能与上下文」不额外复制总分或调用排行榜。

## 3. P1 / P2 Progressive Folding & Permanent DOM Contract

每个 skill-row-unit 由一个跨五列的原生 button 与一个 manifold-sheet 组成，button 的子项为 span、code 和数字，不嵌套其他控件。P1四组指标始终在行上；P2是本行的流图及分支详情。六个折页、全部路径和文本从初始 HTML 常驻。点击另一行先取消前行选中再展开目标，点击本行收回；折页高度使用固定260px壳的 grid 0fr/1fr，单开稳定后总高度不超过600px。切换时用两壳同步占用同一个260px预算，而非旧260加新260。

必须 removedElements = 0、零 innerHTML rebuild；更新已有 Text.data、class、dataset、aria 属性即可，不能用元素 textContent 清掉子节点。关闭的内页在动效结束后 inert/aria-hidden，打开前解除；快速反复点击只跟随最新 selectedSkill，取消过时结算。Enter/Space与点击相同，Escape收页且焦点回触发器。路径hover为临时预览，离开恢复已点击的分支；点击或键盘确认固定选择，aria-pressed同步，详情不是只能hover看见。

## 4. Measured Layout & 1280x800 Viewport Geometry

在1280x800内 main x32/y24、1216×752、padding24，content1168×704。垂直为 masthead48 + gap12 + accordion600 + gap12 + governance32 =704；accordion六行56px共336，单个展开页260，剩余4px内边缘。首屏最下方僵尸行不能被展开页挤出。表内左右16px后1136px；五列宽160/192/220/258/258，四个gap12，合计1136。header与六行复用同一列变量。每列最多三行14px行高，数字不省略。

折页横向使用1136×260画布：Prompt区x0..180、L0枢纽x316..452、右侧标签x728..1136；七个出口各28px高，y24起按28px排列，末端到220，详情y228..256。文件名字允许在连字符处换行，标签由HTML覆盖SVG，不随viewBox缩字。曲带必须是closed cubic-Bezier：如 d="M 452,106 C 556,106 640,28 728,28 L 728,38 C 640,38 556,120 452,120 Z"，渐变填充、描边0.75px，stroke-width <= 24。输入三条从Prompt到L0；输出四条reference及三条script分组，不用直角折线。每个28px出口按钮和路径辅助命中区均 >= 28x28px，薄带的视觉宽度不等于鼠标靶宽。

## 5. Dual-Theme Surface Polarity & Alluvial / Paper-Pocket Craft

InsetRouteBook light：canvas #F5F7FA、paper #FFFFFF、well #EDF2F8、ink #172333、muted #526174、accent #2857A4；dark：#111923 / #1D2938 / #15202D / #F3F6FB / #B5C2D4 / #9DBFFF。纸面无backdrop-filter，Liquid Glass参数明确 blur0、IOR不启用、displacement0；图的半透明渐变是墨色而非玻璃。井边 inset 0 1px 3px #16345812，选中行只加2px左侧色标。光色占比低于10%，正文4.5:1、焦点边3:1。

reference带用蓝→靛，script带用蓝→青；选择提高fill-opacity .22→.52而不改变宽度或暗示次数变化。零命中文件保持灰色库存关联、无脉冲，徽章「0 命中 · 冷门冗余告警」。归档建议为只读说明，无真实删除/归档按钮。主题由外层data-theme提供，否则随系统；减透明模式保持同样的实心纸层。

## 6. Apple Native Spring Physics & Flow Animation

内折页以460ms cubic-bezier(0.22, 1.35, 0.36, 1)开合，内纸translateY(-4px)→0，禁止拉伸文字。曲线中心轨配置1.25px圆点沿C路径1800ms移动，三条输入错开160ms；分支光点只是读取方向提示，不表达实时任务。隐藏折页暂停动画。hover选中在100ms内响应，详情opacity150ms退进但节点不变。

prefers-reduced-motion时折页1ms结算、位移取消、所有flow pulse停住，仍保留静态方向箭头和选中色。焦点环2px/offset2。大图不获得自动焦点，用户可以Tab到七个出口，再Shift+Tab回行；Escape不触发任何宿主App命令。

## 7. Production Data Inventory & Exact DOM Topology

内嵌账只消费r4/domain.md的六行库存，列的解释依次为调用频次与僵尸识别、上下文Token开销、脚本调用效率、Eval效果；第五个真实指标是选取后展示的Prompt→L0→L1与Scripts路线。L0注明SKILL.md入口Token，L1是references/*.md平均连带Token；Cache读作KV Cache命中率，会话列为活跃会话数。以下每个单元格都需可见，不以抽象评分替代：

| 账页 Skill | ① 调用与会话 | ② 上下文 | ③ scripts/*.py 效率 | ④ Eval · eval-cases.json 账目 |
|---|---|---|---|---|
| my-designer | 7d 42 次 · 30d 156 次 · 28 会话 | L0 1.8k tok · L1 +3.4k tok · Cache 96.8% | design_evidence.py 46次 · 均值 140ms · P95 310ms · 成功率 99.1% | 24 用例 (+4 本周) · 100% 通过 · 拦截 19 / 逃逸 2 |
| team-lead | 7d 68 次 · 30d 240 次 · 41 会话 | L0 2.1k tok · L1 +2.8k tok · Cache 97.4% | goal-queue.py 64次 · ci-monitor.py 38次 · 均值 — · P95 420ms · 成功率 99.5% | 32 用例 (+6 本周) · 100% 通过 · 拦截 27 / 逃逸 1 |
| design-studio | 7d 19 次 · 30d 74 次 · 16 会话 | L0 1.5k tok · L1 +2.2k tok · Cache 95.9% | design_catalog.py 39次 · 均值 — · P95 480ms · 成功率 100% | 18 用例 (+2 本周) · 100% 通过 · 拦截 11 / 逃逸 0 |
| m2-dispatcher | 7d 51 次 · 30d 188 次 · 35 会话 | L0 1.6k tok · L1 +1.9k tok · Cache 97.1% | herdr-dispatch.sh 52次 · 均值 — · P95 260ms · 成功率 99.2% | 20 用例 (+3 本周) · 100% 通过 · 拦截 15 / 逃逸 1 |
| linear-board | 7d 33 次 · 30d 112 次 · 22 会话 | L0 1.4k tok · L1 +1.5k tok · Cache 96.5% | linear-bot-bridge.py 44次 · 均值 — · P95 350ms · 成功率 98.8% | 16 用例 (+2 本周) · 100% 通过 · 拦截 9 / 逃逸 0 |
| archive-deck-helper | 7d 0 次 · 30d 0 次 · 0 会话 · 30d 零调用 · 建议归档 | L0 2.6k tok · L1 +4.8k tok · Cache 0.0% | render_legacy.py 0次 · 均值 — · P95 0ms · 成功率 — | 4 用例 (+0 本周) · 75% 通过 · 拦截 0 / 逃逸 3 |

my-designer路线必须全文：Prompt「UI 探索画廊 48%」「实现后截图回溯 34%」「规范审计 18%」→「SKILL.md (L0 入口 · 1.8k tok)」→reference组 navigation-evidence-contract.md（62% · 2.4k tok）、interaction-layering.md（28% · 1.6k tok）、appearance-ledger.md（19% · 1.4k tok）、remotion-video.md（0 命中 · 冷门冗余告警 · 3.1k tok）；script组 design_evidence.py（46次 · P95 310ms · 98.5%）、design_catalog.py（39次 · P95 480ms · 100%）、verify_design_cases.py（18次 · P95 190ms · 100%）。详情还显示均值140ms这一已给出的行级读数及「拦截 19 次 · 逃逸 2 次 [1 IMPL_BUG / 1 SPEC_GAP]」。99.1%是批准的行汇总，98.5%是分支脚本读数，明确标注不同范围，不互相覆盖。

命中率的分母为该Skill调用，references可同时读取，不把62+28+19归一化到100；Token与调用次数也不做守恒。未提供其余Skill的意图比例、文件清单和均值，不猜测：其永久折页保留本人SKILL.md、已知脚本节点及「意图分类未记录」「引用明细未记录」。已知脚本用同样闭合C曲带连接；无意图来源数值时入口引导为无权重关联线。僵尸页为「30d 零调用 · 无读取路径」，P95 0ms保留库存展示、详情说明「未运行」，不画成功脉冲。

```html
<main class="inset-route-book topology-skill-accordion-manifold">
  <section class="content">
    <header class="roi-masthead"><h1></h1><p></p></header>
    <div class="skill-accordion-card">
      <article class="skill-row-unit" data-skill-row data-skill="my-designer"><button data-skill-trigger aria-controls="v01-my-designer-route"><span class="skill-name"></span><span class="call-cell"></span><span class="context-cell"></span><span class="script-cell"></span><span class="eval-cell"></span></button><section id="v01-my-designer-route" class="manifold-sheet" data-bifurcation-panel><figure class="inset-flow-map"><svg></svg><nav class="route-endpoints"></nav></figure><dl class="branch-detail-strip"></dl></section></article>
      <article class="skill-row-unit" data-skill-row data-skill="team-lead"></article>
      <article class="skill-row-unit" data-skill-row data-skill="design-studio"></article>
      <article class="skill-row-unit" data-skill-row data-skill="m2-dispatcher"></article>
      <article class="skill-row-unit" data-skill-row data-skill="linear-board"></article>
      <article class="skill-row-unit" data-skill-row data-skill="archive-deck-helper"></article>
    </div>
    <footer class="zombie-governance-bar"><span></span></footer>
  </section>
</main>
```

代码骨架省略的五个article必须各自静态写齐五列button、不同id的折页与本行已知数据，不得运行时复制my-designer流。本文件仅Stage 1候选，Writer负责具体HTML；不连接私有遥测或磁盘归档。

## 8. Explicit Anti-Patterns & Verification Targets

内嵌版禁旧S1–S12代码及S1、S2、S3、S4、S5、S6、S7、S8、S9、S10、S11、S12上屏；禁stroke-width > 24的大管、innerHTML replacement、replaceChildren、remove、.caustic-veil、.ruler、Active-Matte、<select>测试开关和sandbox disclaimers。content直子类禁止hero、fold-panel、secondary。标题中的参考风格不许可复制另案DOM或把图做成静态插画。

后续WebKit须查1280x800双主题首屏、六行完整读数和28px靶区；逐行展开并重新收回，记录同一DOM identity及removedElements = 0。七个出口逐一hover/点击/键盘验证详情，冷门项不发光，逃逸归因完整，无numeric truncation或页级横向溢出。以各文件prompt SHA绑定实现；此处未执行像素测试，不能把设计约束当作已通过证据。
