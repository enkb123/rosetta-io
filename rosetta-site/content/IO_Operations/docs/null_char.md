+++
title = ''
draft = false
+++

# null_char

Output a null character

See https://en.wikipedia.org/wiki/Null_character


## Python

```python {filename="null_char.py"}
print("Hello World \0")
```

## Ruby

```ruby {filename="null_char.rb"}
puts "Hello World \0"
```

## Nodejs

```javascript {filename="null_char.mjs"}
console.log("Hello World \0")
```

## Deno

```javascript {filename="null_char.mjs"}
console.log("Hello World \0")
```

## Php

```php {filename="null_char.php"}
<?php

echo "Hello World \0";
```

## R

```r {filename="null_char.R"}
temp_file <- tempfile()

writeBin(c(charToRaw("Hello World "), as.raw(0), charToRaw("\n")), temp_file)

system(paste("cat", temp_file))

unlink(temp_file)
```

## Perl

```perl {filename="null_char.pl"}
use strict;
use warnings;

print "Hello World \0"
```

## Java

```java {filename="NullChar.java"}
public class NullChar {
  public static void main(String[] args) {
    System.out.println("Hello World \0");
  }
}
```

## Bash 3

```bash {filename="null_char.sh"}
printf "Hello World \0"
```

## Bash 5

```bash {filename="null_char.sh"}
printf "Hello World \0"
```

## Lua

```lua {filename="null_char.lua"}
print("Hello World \0")
```

## C#

```csharp {filename="NullChar.cs"}
class NullChar {
  public static void Main(string[] args) {
    Console.WriteLine("Hello World \0");
  }
}
```

## Go

```go {filename="null_char.go"}
package main

import "fmt"

func main() {
	fmt.Println("Hello World \x00")
}
```

## Swift

```swift {filename="null_char.swift"}
print("Hello World \0")
```

## Raku

```raku {filename="null_char.raku"}
use v6;

say "Hello World \0";
```

## Rust

```rust {filename="null_char.rs"}
fn main() {
    println!("Hello World \0");
}
```

