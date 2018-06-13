---
title: "Swift: String"
layout: post
tags: [iOS, Swift, Note, String]
categories: [iOS, Swift]
published: ture
---

## String

`String`在Swift中被定义为`Struct`，所以包含构造函数，成员函数，成员变量等。

`String`为完全Unicode编码。

同时拷贝为值拷贝。


### 初始化

```
var emptyString = ""
var anotherEmptyString = String()
```

通过`isEmpty`判断是否为空

### Strings Are Value Type

String是**value type**，也就是当拷贝的时候，是值拷贝，包括在传参数时，也是为值拷贝传递。

### String Interpolation

```
let multiplier = 3
let message = "\(multiplier) times 2.5 is \(Double(multiplier) * 2.5)"
// message is "3 times 2.5 is 7.5"
```

通过这种方式可以产生混合其他变量的String。

### Character

`String`含有一个property为`characters`，可以通过`for-in`来遍历。

`var characters: String.CharacterView { get } `

因为Swift中String可以保存各种类型的编码，所以如果需要遍历，需要根据上述方法，来保证遍历的是每一个字符。

`String([Character])`和`Array(String)`分别可以`String`和`[Character]`。

#### Count

在`characters`属性中，包含一个`count`属性，计算`String`中包含的显示出的字符个数。

```
var word = "cafe"
print("the number of characters in \(word) is \(word.characters.count)")
// Prints "the number of characters in cafe is 4"
 
word += "\u{301}"    // COMBINING ACUTE ACCENT, U+0301
 
print("the number of characters in \(word) is \(word.characters.count)")
// Prints "the number of characters in café is 4"
```

**Note：在Swift中，因为是基于Unicode编码，在每次计算`count`时，需要遍历整个`String`，所以在处理长句子时需要注意。**


### 比较

字符串`String`和`Character`比较是根据Extended grapheme clusters，包括显示相同和语义一致。

###方法

#### 遍历

因为`String`中计算`count`时，根据显示字符计算，所以`String`下标类型为`String.Index`，而不是`Int`。

`startIndex`：第一个字符
`endIndex`：最后一个字符的后一个位置
`predecessor()`：某个下标前一个位置
`successor()`：某个下标后一个位置
`advancedBy(_:)`：某一个下标向后n个位置（负数向前）
`characters.indices`：所有下标数组，用`for-in`遍历

#### 插入删除

`insert(_:atIndex:)`：插入字符到字符串特定位置

`insertContentsOf(_:at:)`：插入另一个字符串。

```swift
welcome.insertContentsOf(" there".characters, at: welcome.endIndex.predecessor())
// welcome now equals "hello there!"
```

`removeAtIndex(_:)`：删除某个字符

`removeRange(_:)`：删除字符串，参数为`Range`。

```swift
let range = welcome.endIndex.advancedBy(-6)..<welcome.endIndex
welcome.removeRange(range)
// welcome now equals "hello
```

#### Prefix and Suffix Equality

`hasPrefix(_:)`：判断字符串是否包含某个前缀。
`hasSuffix(_:)`：判断字符串是否包含某个后缀。

