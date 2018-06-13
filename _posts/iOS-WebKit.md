---
layout: post
title:  "WebKit"
categories: iOS
author: LeePepe
---

# WebKit

WebKit提供了一整套网页浏览的class，包括显示内容，运行JS，管理历史记录等。

WebKit是苹果专门开发用来进行替代iOS中UIWebView和MAC中WebView，所以最好之后都适用WKWebView而不是UIWebView

    WebKit是线程不安全的，当调用该框架的函数时，必须回到主线程。

## WKWebView

进入WebView
