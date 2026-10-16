---
layout: post
title: "NativeDesignKit：Button、Toggle、TextField 设计评审"
date: 2026-10-16
categories: design swiftui
permalink: /design/native-components-design-review/
---

这一轮只聚焦 Button、Toggle、TextField，按 Apple HIG 与 Finesse 的单组件方法完成设计、真实 SwiftUI 截图、独立审查和修正。

[打开三组件评审：改前／改后与真实交互录像](/native-design-kit/components-20261016/)

图库包含每个组件的 iPhone 和 macOS 明暗对比、大字体中文、状态板、最小中性上下文，以及三段 iPhone 实际交互录像。截图和录像均对应源码 `a870b9c`；[上一版完整图库](/native-design-kit/a7ca241/) 继续保留。

Button 保留原生操作层级与角色，修正加载对齐及浮动 Glass 的内容间距；Toggle 使用原生开关并让长标签自然增长；TextField 保留持久标签和原生编辑，空提交时将原因与修正提示显示在键盘上方。

独立 reviewer 对本轮源码与所示静态呈现给出有范围限制的通过结论。工程检查、具体发现与修正，以及未覆盖的桌面键盘、hover、Glass、系统无障碍设置和最低系统版本等均在图库内单独列出。macOS 截图为原生宿主位图并使用 bordered fallback，不能作为实时 Glass 或完整桌面交互的证据；独立 reviewer 另完成录像抽帧复核，未发现新的组件阻断问题；连续播放的动效和精确响应时间尚未验收。

[代码 PR #14](https://github.com/LeePepe/shared-design-system/pull/14)。当前不合并、不启用自动合并、不发布库版本；等待这批组件的视觉反馈后再决定后续范围。
