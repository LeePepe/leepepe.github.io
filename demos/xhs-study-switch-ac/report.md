# TIA-457 制图与发布研究报告

访问日：2026-11-15（UTC+8）。本页公开内容来自固定版本的公开源码静态检查与本地网关探针；最高置信度为 MEDIUM，单一来源不升级为 HIGH。SVG 成功尝试使用了不同 token budget，样本很小，不是吞吐量 benchmark。

## 结论

推荐链路是：真实文章 → 离线原创 PNG → 人工检查事实、素材与 AI 标识 → 用户在官方创作者平台手动操作。此 Goal 未登录、上传、保存草稿或发布。未来 Bridge/Playwright 只是在得到明确授权与条款核验后的条件选项；人工确认不自动使第三方自动化合规。

长按明确是 **ON／打开空调**，不是 toggle。24℃是文章里的示例，不是已验证配置；“99%”是原文修辞，不是测量。离开书房、睡眠与离家时的收尾是作者描述的家庭行为，不是本页提供的可部署自动化或接线教程。

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
