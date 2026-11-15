# TIA-457 制图与发布研究摘要

访问日：2026-11-15（UTC+8）。本页是公开脱敏摘要，证据最高置信度为 MEDIUM；模型、网关与平台条款会随版本变化。

## 已测能力

- Magpie `/v1/models`：HTTP 200。
- Raven local GPT-5.3-codex SVG：HTTP 200，10.24s；GPT-4.1 vision：HTTP 200，4.27s。
- Gemini 4 Argon bounded SVG：HTTP 200，20.5s，valid XML；一次较长 SVG 响应截断，保留为迭代 caveat。
- Copilot CLI builtin `image_generation`：两张原创无字背景，实测 1024×1536；模型由工具结果披露为 not disclosed。未购买新订阅。
- Cursor Claude Opus 4.8 / Fable 5.2：HTTP 429 quota，未购买 credits。
- `gpt-image-1` / `dall-e-3` image endpoints：网关 HTTP 404；Raven 的 `gpt-image-2.5-flare` 出现在模型列表，但 responses 返回 HTTP 400 `model_not_supported`。

## 推荐发布边界

离线原创 PNG → 人工检查 → 用户在官方创作者平台手动操作。没有登录、Cookie、上传、保存草稿或发布。第三方 Bridge/Playwright 草稿流不是默认合规方案；未来若经明确授权评估，应使用专用受保护 profile，人工重新打开草稿并核对内容。AI 背景应按适用规定与平台要求主动标识。

## 来源

- [中国政府网：生成合成内容标识办法](https://www.gov.cn/zhengce/zhengceku/202503/content_7014286.htm)
- [Playwright persistent context](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context)
- `bozhouDev/xhs-article-to-images`、`Ming-H/xhs-image-generator`、`chang-zy/xiaohongshu-skill`、`autoclaw-cc/xiaohongshu-skills`、`xpzouying/xiaohongshu-mcp` 的 pinned source URLs 见研究 handoff；静态源码检查不等于 live draft 成功或平台授权。
- Ming-H 的分页实现需正确的 frontmatter 边界；否则前两个 `---` 可能吞掉中间内容，不能把它宣传成可靠的普通 Markdown 自动分页器。
- 官方创作者协议 URL（https://agree.xiaohongshu.com/h5/terms/ZXXY20260422001/-1）仅作为待人工核对入口；当前页面是前端壳，未把索引片段当作已验证官方原文。AI 内容创作与无人值守账号操作是不同风险边界。
