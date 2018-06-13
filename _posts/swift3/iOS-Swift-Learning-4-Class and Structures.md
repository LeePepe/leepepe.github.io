---
title: "Swift: Class and Structures"
layout: post
tags: [iOS, Swift, Note, Data Structure]
categories: [iOS, Swift]
published: ture
---

## Comparing Classes and Structures

`class`和`struct`是最常见的两种结构体：

* 定义变量来存储值。
* 定义函数。
* 定义下标访问。
* 定义构造函数。
* 在外部扩展功能。
* 调用`protocol`来实现标准化功能。

`class`还具有其他功能：

* 继承。
* 类型捕获(Type Casting)。
* 析构函数来释放资源。
* 引用计数可以使多个引用指向一个实例。

### Definition Syntax

`class`和`struct`定义的方式十分接近： 

```
struct Resolution {
    var width = 0
    var height = 0
}
class VideoMode {
    var resolution = Resolution()
    var interlaced = false
    var frameRate = 0.0
    var name: String?
}
```

可以看到`Resolution`中定义了两个属性，`width`和`height`，他们的默认值都是`0`，根据type inference，类型都为`Int`。

在`VideoMode`中的四个属性，第一个`resolution`被定义成一个`Resolution`实例，这也是类和结构体构造新实例的方法。

`name`被定义为`String?`，因为为optional，所以有默认值`nil`。

### Accessing Properties

通过`.`来访问其中的属性或函数。

```
let somVideoMode = VideoMode()
someVideoMode.resolution.width = 1280
print("The width of someVideoMode is now \(someVideoMode.resolution.width)")
// Prints "The width of someVideoMode is now 1280"
```

### Memberwise Initializers for StructureTypes

结构体自动提供包含所有properties为参数的构造函数。

这样就可以构造出不同属性值的实例。

`let vga = Resolution(width: 640, height: 480)`

## Structures and Enumerations Are Value Types

Value

* 作为参数时，**拷贝**到函数中。
* **拷贝**到其他变量时。
* 当设为`let`时，不可改变。
* 函数参数默认都为`let`
* 函数必须设置关键字`mutating`才可以改变结构体或枚举类型。


## Classes Are Reference Types

* 存储在heap中并且ARC。
* 设为`let`时，也可以改变其中的properties或调用methods。

### Identity Operators

通过`===`和`!==`判断两个reference是否指向同一个实例。

> 当自定义类或者结构体的时候，有义务定义在什么情况下，两个类是相等的（`==`）和不等的（`!=`）

## Choosing Between Classes and Structures

`class`为引用传递，`struct`为值传递，这是两者最重要的区别。

在选择的时候：

* `struct`只包含少量的属性或数据。
* 在进行复制或作为参数时，你更希望是拷贝传递而不是引用传递。
* 在`struct`中的所有属性，都要符合值拷贝的特性，而不要出现引用拷贝的property。
* 不需要进行继承。

## Assignment and Copy Behavior for Strings, Arrays, and Dictionaries

`String`，`Array`和`Dictionary`都是值拷贝。

但OC中`NSString`，`NSArray`，`NSDictionary`是类，所以为引用拷贝。

> swift对所有的值拷贝都有特殊处理，他只会在真正需要用到拷贝内容的时候，再进行拷贝。保证最优效果。




