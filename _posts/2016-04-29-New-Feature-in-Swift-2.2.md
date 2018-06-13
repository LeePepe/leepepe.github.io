---
layout: post
tags: [iOS, swift]
categories: [iOS, swift]
published: ture
date:   2016-04-29 00:00:00 +0800
title: "Swift 2.2 New Feature"
---


2.2为swift开源后第一个官方版本，主要修改了部分语法，为3.0做准备。

原博客地址: [https://swift.org/blog/swift-2-2-new-features/](https://swift.org/blog/swift-2-2-new-features/)
 
## Compile-time	Swift version checks

```swift
#if swift(>=3.0)
print("Running Swift 3.0 or later")
#else
print("Running Swift 2.2 or earlier")
#endif
```

与`#available`不同，该检查在编译期间完成而不是运行期间。

## Compile-time checked selectors

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    navigationItem.rightBarButtonItem =
        UIBarButtonItem(barButtonSystemItem: .Add, target: self,
                        action: "addNewFireflyRefernce")
}

func addNewFireflyReference() {
    gratuitousReferences.append("We should start dealing in black-market beagles.")
}
```

在之前的版本中，app会crash，因为无法找到`addNewFireflyRefernce()`-缺少一个‘e’。但是在编译期间，函数名只是一个字符串所以无法报错。
现在通过`#selector`可以在编译时报错。

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    navigationItem.rightBarButtonItem =
        UIBarButtonItem(barButtonSystemItem: .Add, target: self,
                        action: #selector(addNewFireflyRefernce))
}

func addNewFireflyReference() {
    gratuitousReferences.append("Curse your sudden but inevitable betrayal!")
}
```

## More keywords as argument labels

swift有很多的保留字，在2.2后，可以使用部分保留字作为参数名称（外名），除了`let`，`var`，`inout`。

``` swift
func visitCity(name: String, in state: String) {
    print("I'm going to visit \(name) in \(state)")
}

visitCity("Nashville", in: "Tennessee")
```

## Tuple comparison is built-in

现在swift可以比较两个tuple了，在2.2中最多可以比较有不超过6个的tuple。比较的方式是比较对应元素的内容。如果所有都匹配那么则判断true。

    tuple只是比较内容，并不比较内容

```swift 
let singer = (first: "Taylor", last: "Swift")
let bird = (name: "Taylor", breed: "Swift")

if singer == bird {
    print("This explains why she sings so well.")
} else {
    print("No match.")
}

"This explains why she sings so well."
```


## Tuple splat syntax is deprecated

现在不可以将所有的参数打包成一个tuple传入到一个函数中。

```swift 
func describePerson(name: String, age: Int) {
    print("\(name) is \(age) years old")
}

let person = ("Malcolm Reynolds", age: 49)
describePerson(person)
```

这样的方式现在被禁止了。

## C-style `for` loops are deprecated

C风格的for循环被废除（感觉swift要和`;`对着干）

``` swift
for var i = 0; i < 10; i++ {
    print(i)
}

改成

for i in 0 ..< 10 {
    print(i)
}
```

递减循环改变

```swift
for var i = 10; i > 0; i-- {
    print(i)
}

改成

for i in (1...10).reverse() {
    print(i)
}
```

非+1循环改变

```swift
for var i = 0; i < 10; i += 2 {
    print(i)
}

改成

for i in 0.stride(to: 10, by: 2) {
    print(i)
}
```

## `++` and `--` are deprecated

（swift这是要疯啊，好吧其实还好因为这基本用不上。。。）

```swift
i++
i--
++i
--i
i = i++
```
这些都不可以用了

## `var` parameters are deprecated

现在`var`不可以用来修饰一个参数，这很符合原本swift的习惯。当需要改变时，要么连同函数外的参数一起改变，要么为let不可改变并定义一个新的变量。

``` swift
一起改变
func greet(inout name: String) {
    name = name.uppercaseString
    print("Hello, \(name)!")
}

var name = "Taylor"
greet(&name)
print("After function, name is \(name)")

定义一个新的变量
func greet(name: String) {
    let uppercaseName = name.uppercaseString
    print("Hello, \(uppercaseName)!")
}
```

## Renamed debug identifiers

将调试变量更改名字

```swift
func visitCity(name: String, in state: String) {
    // old - deprecated!
    print("This is on line \(__LINE__) of \(__FUNCTION__)")

    print("I'm going to visit \(name) in \(state)")

    // new - shiny!
    print("This is on line \(#line) of \(#function)")
}
```



