---
title: "Swift: Basics"
layout: post
tags: [iOS, Swift, Note]
categories: [iOS, Swift]
published: ture
---
# Swift 学习

如果你想学习swift语言，那么[官方文档](https://swift.org/documentation/)无疑是最好的选择。或者你可以浏览[中文版](https://github.com/numbbbbb/the-swift-programming-language-in-chinese)，这是Swift认可的版本，但是我还是建议选择官方版本，毕竟里面的英文真的不难。这里我只是根据Stanford的课程，列出一些需要强调的部分，可能没有章法。


**所有代码来自于[官方文档](https://swift.org/documentation/)和[Stanford](http://web.stanford.edu/class/cs193p/cgi-bin/drupal/)**

## Type Safety and Type Inference

Swift是**强类型**（type-safe）的语言，所以必须声明类型并保证类型一致。

编译器会在编译时进行类型检查。

但这不意味着需要声明类型。在swift中，更多的时候不需要声明类型（从编
程的风格上，swift希望声明越少越好），因为swift有**类型推断**（type-inference）。

```
let pi = 3.14159
// pi is inferred to be of type Double

let meaningOfLife = 42
// meaningOfLife is inferred to be of type Int

let capitalOfChina = "Beijing"
// capitalOfChina is inferred to be of type String
```

如上，swift会将数字推断为`Int`或者是`Double`类型，将字符串推断为`String`类型。

## Numeric Literals

### 整数

```
let decimalInteger = 17
let binaryInteger = 0b10001       // 17 in binary notation.     0b为二进制前缀
let octalInteger = 0o21           // 17 in octal notation       0o为八进制前缀
let hexadecimalInteger = 0x11     // 17 in hexadecimal notation 0x为十六进制前缀
```

**Note**

**四个变量都是Int类型，在赋值的时候都会被转为十进制，输出为十进制。**

### 浮点数


```
let decimalDouble = 12.1875     // 12.1875，一般表示法
let exponentDouble = 1.21875e1  // 12.1875，e为10的次方，e1为10的1次方
let hexadecimalDouble = 0xC.3p0 // 12.1875，0x为16进制前缀，p为2的次方，p0为2的0次方
```

### 额外信息

可以在数字上添加额外的`0`或是`_`来保证可读性。

```
let paddedDouble = 000123.456
let oneMillion = 1_000_000
let justOverOneMillion = 1_000_000.000_000_1
```

## Type Alias

`typealias AudioSample = UInt16`可以定义一个新的类型，和C语言中的`#define`一致。

## Optional

optional应该是swift中最重要的特点之一，在swift中，不存在指针，每一个变量都有其类型（type safe）。

但是可以设定某一个变量为optional，那么该变量有两种可能性，一种为`nil`，即没有被赋值。一种为某个特定的值，该值符合该变量的类型。`var x: String?`就是一个optional的String类型，现在`x`为`nil`。它可以被赋值，但需要是`String`类型。

> There is a value, and it equals x

> There isn’t a value at all

**Note**
    
**optional is enum**

``` 
enum Optional<T> {
    case None
    case Some<T>
}
```

### Optional can be "chained"

optional可以被链式调用

```
var display: UILabel?
if let label = display {
    if let text = label.text {
        let x = text.hashValue
    }
}
```

可以被如下调用，使代码简洁。

```
if let x = dispaly?.text?.hashValue {}
```

### ?? 操作

` display.text = s ?? "" `表示如果s为nil，则使用后面的值，即`""`

### Implicitly Unwrapped Optionals

如果当确定某个值在设定后不会变回nil，那么可以`!`替代`?`。（Sometimes it is clear from a program’s structure that an optional will *always* have a value, after that value is first set. ）

`!`所修饰的变量，依然是optional，但是可以不添加`？`来访问，但如果该值为`nil`，那么就会产生runtime error。Crash掉程序。

**Note ： 在开发过程中，主要在outlet上，会设定变量为`!`。当类实例生成的时候，这些outlet通常都是有值的情况。但需要注意，在prepareSegue的时候，这些outlet并没有被第一次设定值，所以一些updateUI操作会失效（涉及到outlet时），这时我们只需要在updateUI时添加`?`，当outlet未设置时跳过该操作即可（需要在outlet的`didSet`中设置updateUI，即可完成UI更新）**

**在确定该值在程序中一直不为nil，应该尽量使用!，这样会更容易debug。**

## Tuples

tuple是一种类型（type），所以可以被函数返回。

tuple可以包含很多参数。但每个参数也具有类型。

你可以对面每一个参数命名，然后使用名字访问他们

```
let x: (w: String, i: Int, v: Double) = ("hello", 5, 0.85)
print(x.w) // print hello
print(x.i) // print 5
print(x.v) // print 0.85
let (wrd, num, val) = x
```

### Tuple 比较

现在可以比较两个tuple并返回一个Bool值。但tuple中包含的元素少于7个。如果大于等于7，则需要自己实现。

``` 
(1, "zebra") < (2, "apple")   // true because 1 is less than 2
(3, "apple") < (3, "bird")    // true because 3 is equal to 3, and "apple" is less than "bird"
(4, "dog") == (4, "dog")      // true because 4 is equal to 4, and "dog" is equal to "dog"
```

比较方法是按顺序比较，如果第一个相等，则比较下一个。



## Range

**Range是结构体，包含两个变量startIndex和endIndex**
    
`...`（包含最后一个）和`..<`（不包含最后一个）是Range的一种语法，可以快速创建一个Range。

String的Range不是Range<Int>，而是Range<String.index>。

## Data Structures in Swift

Classes, Structures and Enumerations.

###相同点

* Declaration syntax.
* Properties and Functions.
* Initializers(not enum).

###不同点

* 只有`class`可继承。
* **Value Type**(struct, enum) vs. **Reference Type**.

#### Value(struct and enum)

* 传参时为拷贝(copy)。
* 赋值时为拷贝(copy)。
* 当为`let`时不可改变(Immutable)。
* 作为函数参数时，默认为constants。
* 必须加上`mutating`才可以改变。

#### Reference(class)

* Stored in the heap and reference counted(automatically).
* 设为`let`依旧可以调用方法和改变其properties。（表示该let指向的对象不会发生改变）
* 作为参数时，只是传递该实例。

#### Choose

Struct更多作为架构类型(fundamental types)，更轻量，更少东西。


### Types and Instances can have methods/properties

## Properties

### Property Observers

`willSet`和`didSet`分别有`newValue`和`oldValue`，作为改变前后的值。当某个值影响UI时，可以在这其中去改变UI。

### Lazy Initialization

`lazy`会让property不会马上初始化，而是等到被访问时才初始化。

lazy property可以调用self的方法作为初始化，也可以使用所有已初始化的property，同时可以设定一些设置并初始化(clouse)方法。

## Other Class

### NSObject

Base class for all OC classes
有些很好的功能，当需要使用的时候，继承`NSObject`。

### NSNumber

在OC中用来包含数字成为一个对象(object)，从而使其可以成为数组。
但在Swift中并不需要这样的处理。

可以通过其中的`intValue`，`DoubleValue`等，赋值给Swift的`Int`或`Double`。成为Swift的类型。

### NSDate

用来表示日期和时间，在实际使用的时候，需要注意设置其地点(local)，风格(style)等，来使app本地化。

### NSData

将数据打包(bag of bits)，用来存储，传递数据等。

 








