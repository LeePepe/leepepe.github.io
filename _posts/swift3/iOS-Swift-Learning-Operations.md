---
title: "Swift:Operations"
layout: post
tags: [iOS, Swift, Note]
categories: [iOS, Swift]
published: ture
---

在Swift中，绝大多数的操作都比较常见，这里会说明一些特别操作

## Assignment Operator

赋值语句和其他语言用法一直。

* 对Value Type，所做的是值拷贝传递。
* 对Reference Type，所做的是对象指针的拷贝，即引用拷贝。
* 对Truple对象，赋值的右值同样需要是同类型的Truple，同时每个值的拷贝符合上述两点

**赋值操作并不返回任何值，所以不可以有连续赋值或将赋值操作作为boolean值放到条件判断中。也包括`+=`等操作**

## Remainder Operator

`%`操作符在Swift中，不仅仅可以对正整数进行操作，同时可以浮点数和负数。

```
-9 % 4 // equals -1
```

```
8 % 2.5 // equals 0.5
```

对于负数而言，会忽略掉第二个值的符号，因为倍数本身可以带符号，如-2倍。

## Unary Operator

`-`前缀并且和变量之间没有空格时，会得到变量的相反数。

`+`:有-就有+，没什么乱用，并不会改变值。

## Comparsion Operators

`===`和`!==`判断引用是否指向同一个实例

## Nil Coalescing Operator

`a ?? b`操作用来表示当`a`为nil的时候，返回`b`，否则返回`a`的值。

需要`b`和`a`包含的值类型一致。

## Range Operators

`...`（包含最后一个）和`..<`（不包含最后一个）。


