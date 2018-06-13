---
layout: post
title:  "Swift:Subscript"
categories: iOS
author: LeePepe
---


#Subscript

通过`subscript`来定义其接收的下标`[]`参数、返回值和定义。

* 参数可以是变量也可以是不定个数变量，但不可以是in-out参数或有默认值。
* 定义的方式和computed properties一致，名称为`subscript`，可以包含`get`和`set`。
* 可以定义多个`subscript`，在调用的时候根据参数类型自动选择。