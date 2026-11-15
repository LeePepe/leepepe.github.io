# TIA-457 制图与发布研究报告

访问日：2026-11-15（UTC+8）。本页公开内容来自固定版本的公开源码静态检查与本地网关探针；最高置信度为 MEDIUM，单一来源不升级为 HIGH。SVG 成功尝试使用了不同 token budget，样本很小，不是吞吐量 benchmark。

## 结论

推荐链路是：真实文章 → 离线原创 PNG → 人工检查事实、素材与 AI 标识 → 用户在官方创作者平台手动操作。此 Goal 未登录、上传、保存草稿或发布。未来 Bridge/Playwright 只是在得到明确授权与条款核验后的条件选项；人工确认不自动使第三方自动化合规。

长按明确是 **ON／打开空调**，不是 toggle。24℃是文章里的示例，不是已验证配置；“99%”是原文修辞，不是测量。离开书房、睡眠与离家时的收尾是作者描述的家庭行为，不是本页提供的可部署自动化或接线教程。

## T3 · 钦定四幕正文与卡片对齐（不重做 T1 实测）

当前样张为 **A5 / B5 / C5，共 15 张**，配套三份独立口语稿。基于已落盘的钦定四幕唯一源文章，用 `build_site.py` 生成并核对 [完整 Blog 故事](/thoughts/study-switch-long-press-ac/)，再重排卡片。

每套图和每份正文都对齐钦定四幕原话：
1. **【装修搁置：这七七八八的东西也太多了】** 装修那会儿想装台 NAS 玩全屋智能，被 HA 和 Node-RED 七七八八的配置、实体和节点劝退搁置。
2. **【25 年 AI 破局：搭好骨架，实测自己抠】** AI 能直接帮写 YAML 配置、完成初步的 Node-RED 流程，真正的实机测试、延迟调节和边界排障还得自己动手一点点来。
3. **【买多了的无线开关：随手放书房当测试键】** 为睡觉时「一键入眠」（顺手关灯、关窗帘）买开关不小心买多了，随手放书房桌边，从 Node-RED 里随便连了一条流当测试键。
4. **【夏天的神来之笔：闲置长按 → 盲开空调】** 夏天只剩一个空调遥控器，米家 App 每次都要「掏手机 → 解锁 → 打开米家 App → 找到书房 → 点开空调」，干脆在 Node-RED 里把闲置「长按」接上书房空调（闲置长按 -> 盲开空调）——因为每次坐进书房，其实只需要「开」就行，长按一下听见「滴」声出风，零心智负担。

夏天未指定年份，不虚构 AI 厂商、硬件型号、实际温度或操作耗时。T1 的研究表、固定引用、两张原始 AI 背景和 GPT/Gemini 对比探针保留；这次更新故事和排版，没有再次生图或执行平台发帖。

## 本机能力矩阵

| 能力/路径 | 观测 | 输出结论 | 版本与范围限制 |
|---|---|---|---|
| Magpie `/v1/models` | HTTP 200 | 模型列表可见 | 可见不代表每个能力可用 |
| Raven GPT-5.3-codex SVG | HTTP 200，10.24s | SVG 可渲染 | 单次小样本 |
| Raven GPT-4.1 vision | HTTP 200，4.27s | 可做视觉检查 | 单次小样本 |
| Gemini 4 Argon bounded SVG | HTTP 200，20.5s，valid XML | bounded SVG 可渲染 | 初始长响应曾截断；不同 token budget，不是吞吐 benchmark |
| Copilot builtin image_generation | 两张 1024×1536 原创无字背景 | 可作为 Style B 氛围素材 | backend model 未披露；无新订阅，成本未测 |
| `gpt-image-1`/`dall-e-3` image endpoints | 网关 HTTP 404 | 当前不可用 | models 列表与 image API 不等价 |
| `gpt-image-2.5-flare` | models 可见；responses HTTP 400 `model_not_supported` | 不可用作图像 API | 不购买 credits |
| Cursor Claude Opus 4.8 / Fable 5.2 | HTTP 429 quota | 未使用 | 不购买 credits |

## 开源图文与投递工具矩阵

| 项目（固定来源） | 观察到的能力 | 风险/限制 | 来源 |
|---|---|---|---|
| `bozhouDev/xhs-article-to-images` | 8 套 skins；HTML/Playwright，1080×1440 | agent-authored HTML，不是全自动 Markdown parser；版式限制是编辑建议 | [README](https://github.com/bozhouDev/xhs-article-to-images/blob/79d2ccce32ff44236bf504a39b850637acacd950/README.md#L27-L33) · [render](https://github.com/bozhouDev/xhs-article-to-images/blob/79d2ccce32ff44236bf504a39b850637acacd950/scripts/render.cjs#L56-L80) |
| `Ming-H/xhs-image-generator` | `---` 分页与 Python Playwright | 固定 1080×1440；`--dpi` 未作用于 render；frontmatter 边界不正确时，前两个 `---` 可能吞掉中间内容，不是可靠普通 Markdown 自动分页 | [README](https://github.com/Ming-H/xhs-image-generator/blob/90858abb685bb12c8b1fa47d957683a04a19b76a/README.md#L3-L9) · [generator](https://github.com/Ming-H/xhs-image-generator/blob/90858abb685bb12c8b1fa47d957683a04a19b76a/generator.py#L171-L215) |
| `chang-zy/xiaohongshu-skill` | `fill-publish` / `save-draft` / `click-publish` via local Bridge | 静态源码观察；save-draft 没有证明重新打开草稿读回；不是官方 API 授权证明 | [CLI](https://github.com/chang-zy/xiaohongshu-skill/blob/8404b73e9640594db11da111234758c73f36cb0f/scripts/cli.py#L1316-L1343) · [publish](https://github.com/chang-zy/xiaohongshu-skill/blob/8404b73e9640594db11da111234758c73f36cb0f/scripts/xhs/publish.py#L264-L324) |
| `autoclaw-cc/xiaohongshu-skills` | 类似 Bridge 草稿/发布操作 | 静态源码观察；不等于成功 live draft 或合规 | [publish](https://github.com/autoclaw-cc/xiaohongshu-skills/blob/b043748282a57e347c52f517dfb59819121134ab/scripts/xhs/publish.py#L305-L326) |
| `xpzouying/xiaohongshu-mcp` | publish_content 注册 | Popularity 不是安全证据；未在本 Goal 安装或运行 | [source](https://github.com/xpzouying/xiaohongshu-mcp/blob/bb6fa2e208719ee634fec37881be29d3aa4699b3/mcp_server.go#L240-L264) |
| `jobsonlook/xhs-mcp` | search/read/comments 侧接口 | 不把它当作 publishing/draft MCP | [source](https://github.com/jobsonlook/xhs-mcp/blob/d62c82aa9b0cd1524094361cebfe59c83a16960d/xhs_mcp/__main__.py#L99-L107) |
| `xpi0/xiaohongshu-mcp` | GitHub API 404 | 仅说明该公开 identity 当前不可访问，不证明历史不存在 | [API result](https://api.github.com/repos/xpi0/xiaohongshu-mcp) |

## 风险边界

- **官方与社区证据分开**：中国政府网《生成合成内容标识办法》Article 10 是可引用的主来源；AI 背景应按适用规定与平台要求主动标识。官方创作者协议 URL 目前返回前端壳，未把索引片段当作已核实全文：[协议入口](https://agree.xiaohongshu.com/h5/terms/ZXXY20260422001/-1)。
- **不把 folklore 当规则**：无独立官方证据证明“无头必封”“首行缩进必判搬运”“每天安全 N 篇”“图片文字必须 ≤40%”或“每段必须 ≤3 行”。本页的 ≤40%、≤3 行、无首行缩进是编辑偏好/风险控制建议，不是官方强制规则；没有 safe daily posting guarantee。
- **AI 内容 ≠ 无人值守账号操作**：生成背景与通过第三方工具登录、模拟交互、上传或发帖是不同边界。当前建议人工使用官方平台，人工核对标题、正文、正式话题与 AI disclosure。
- 不采集 Cookie，不开远程调试，不绕过验证码，不做签名/API 规避。Playwright persistent context 未来若经授权应使用专用受保护 profile，不使用日常默认 profile：[官方文档](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context)。

## Genjutsu 与素材说明

Genjutsu 在本机证据中是 native SwiftUI UI/动效设计 skill 路由，不是 Web 栅格生图 API，也不是本组 PNG 的生成模型。Style B 的两个原始背景是通用无字书房/按键意象；最终 PNG 由 HTML/CSS/SVG + Playwright 叠字导出。Style A 与 Style C 使用原创 inline SVG 和 HTML 字形，不使用 AI 图。

## 可复现的十五卡导出

在此目录运行 `npm run render`、`npm run test:cards`；已有本地静态服务器时运行 `npm run test:gallery -- http://127.0.0.1:8769/demos/xhs-study-switch-ac/`。Playwright 通过普通模块解析或 `PLAYWRIGHT_MODULE` / `NODE_PATH` 指定的已有安装加载，不要求额外订阅。

- `cards.cjs` 独立定义 A5 / B5 / C5 的构图；每块文字在创建时指定坐标、宽高、字体、字号与行高。原始图片由脚本按字节编码为 data URI，不依赖浏览器相对 URL。
- 导出先等待字体、所有图片 decode 和两帧稳定布局，再检查整批卡片。任一卡失败，不开始覆盖 PNG；截图目标是固定 1080×1440、scale 1 的 `.slide`。
- `card_geometry.cjs` 检查所有真实文字框、逐字 DOM Range 边界、安全区、字号、scroll 裁剪与跨段落重叠。CJK 字体的 ascent / negative leading 可以超出 CSS 行盒；这些实际 Range 仍必须在安全区，不能与别的文字块重叠。标题额外保留 16px 字体下降部空间，不改变字号、行高或文字起点。同段落的行/字 Range 不被错误视作独立段落；背景 SVG 与图片单独记录，不豁免文字碰撞。
- B 的每页必须有已解码且可见的原图。可见面积用实际 DOM 命中采样给出保守下界（渐变区域也按遮挡计算），不是仅检查一个可能为空的 `every()`。B2/B3/B4/B5 使用 contain 保护完整场景，B4保留椭圆窗口；B5的宽舞台有纸色留边。椭圆、圆角与遮罩仍可能遮住边缘，必须另看像素。
- `story_checks.cjs` 检查四段因果链、2025 年 AI 初步骨架与人工实机工作、睡前剩余测试键、米家五步、闲置长按绑定及 ON/关停语义；逐套检查真实可见文字，并逐份检查复制稿。旧短故事和缺少人工测试/测试键的回归样本会失败。导出也先检查已更新的 Blog；`STORY_SOURCE_PATH` / `STORY_INDEX_PATH` 可指定本机唯一源文章及其索引供测试，不把私有路径写入代码。
- `card-geometry.json` 默认记录全部十五卡的实际框、逐字 Range、计算字体、浏览器实际平台字体、图片自然尺寸、裁切与可见区域，并记录 Blog 和可选唯一源的 SHA-256。`CARD_GEOMETRY_PATH` 可改到私有回执；`CARD_OUTPUT_DIR` 可改 PNG 输出目录；`GALLERY_RECEIPT_DIR` 可改画廊截图目录；`GALLERY_URL` 可改测试服务器。

自动几何、尺寸与回归测试不能证明审美质量，也不能代替独立逐图视觉核对；本地导出不表示已向小红书上传或完成网站发布。
