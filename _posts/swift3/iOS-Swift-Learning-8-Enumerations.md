---
title: "Swift: Enumeration"
layout: post
tags: [iOS, Swift, Note]
categories: [iOS, Swift]
published: ture
---

枚举类型是一组相同类的相关值。

在iOS中，很多变量都被定义为枚举类型Enumeration。Style，State等。

Enumeration最大的好处便是其可以在`switch`语句中，根据不同的`case`进行不同的操作。

```
enum CompassPoint {
    case North
    case South
    case East
    case West
} 
```

或

```
enum Planet {
    case Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
}
```


## Associated Values

对于`enum`中的值，可以提供多个Associated Values，这个值可以`switch`中使用。

```
enum Barcode {
    case UPCA(Int, Int, Int, Int)
    case QRCode(String)
}
var productBarcode = Barcode.UPCA(8, 85909, 51226, 3)

productBarcode = .QRCode("ABCDEFGHIJKLMNOP")
 
switch productBarcode {
case let .UPCA(numberSystem, manufacturer, product, check):
    print("UPC-A: \(numberSystem), \(manufacturer), \(product), \(check).")
case .QRCode(let productCode):
    print("QR code: \(productCode).")
}
// Prints "QR code: ABCDEFGHIJKLMNOP.
```

如果所有的Associated Values都是`let`，那么可以将`let`前置。

## Raw Values

Raw Values即枚举类型的默认值，不同于C语言，swift并没有定义默认的`Int`值，但可以自定义默认值。

```
enum ASCIIControlCharacter: Character {
    case Tab = "\t"
    case LineFeed = "\n"
    case CarriageReturn = "\r"
}
```

通过这样的方式将`enum`的默认值定义为`Character`类型，同时给每个`case`定义了相应的值。

### Implicitly Assigned Raw Values

定义了Raw Values的类型后，swift可以提供默认值：

*  `Int`类型会按照先后顺序提供逐一增加的默认值，如果第一个`case`没有定义值，那么会定义成`0`。
*  `String`类型可以按照`case`的名称提供相应的字符串Raw Values值。

```
enum Planet: Int {
    case Mercury = 1, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
}
```


### Initializing from a Raw Value

可以通过Raw Value进行enum类型的初始化。

但为failable initializer，因为Raw Value可能在`enum`中并没有定义。

```
let positionToFind = 11
if let somePlanet = Planet(rawValue: positionToFind) {
    switch somePlanet {
    case .Earth:
        print("Mostly harmless")
    default:
        print("Not a safe place for humans")
    }
} else {
    print("There isn't a planet at position \(positionToFind)")
}
// Prints "There isn't a planet at position 11
```

## Recursive Enumerations

通过`indirect`关键字，可以将另一个`enum`实例作为associated value添加到`case`中。

```
enum ArithmeticExpression {
    case Number(Int)
    indirect case Addition(ArithmeticExpression, ArithmeticExpression)
    indirect case Multiplication(ArithmeticExpression, ArithmeticExpression)
}
```
