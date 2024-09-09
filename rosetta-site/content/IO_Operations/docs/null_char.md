+++
title = ''
draft = false
+++

# null_char

Test outputing a null character

## Python

`null_char.py`

```python
print("Hello World \0")
```

## Ruby

`null_char.rb`

```ruby
puts "Hello World \0"
```

## Nodejs

`null_char.mjs`

```javascript
// Script to write null character to stdout
console.log("Hello World \0")
```

## Deno

`null_char.mjs`

```javascript
// Script to write null character to stdout
console.log("Hello World \0")
```

## Php

`null_char.php`

```php
<?php
// Write null character to stdout

// echo function does not add a new line so adding it here manually
// for consistency with other langauges
echo "Hello World \0\n";
```

## R

`null_char.R`

```r
#' Write the null character to stdout

# R character strings don't support the null character
# so we convert the strings to raw vectors
text_raw <- charToRaw("Hello World ")
null_char_raw <- as.raw(0)
new_line_raw <- charToRaw("\n")
raw_vector <- c(text_raw, null_char_raw, new_line_raw)

# Write to a temporary binary file
writeBin(raw_vector, "temp_binary_file.bin")

# Read file to stdout, intern=FALSE so output is not captured as a character vector
system("cat temp_binary_file.bin", intern = FALSE)

# Delete the temp file
unlink("temp_binary_file.bin")
```

## Perl

`null_char.pl`

```perl
use strict;
use warnings;

print "Hello World \0\n"
```

## Java

`NullChar.java`

```java
public class NullChar {
  public static void main(String[] args) {
    System.out.println("Hello World \0");
  }
}
```

## Bash 3

`null_char.sh`

```bash
printf "Hello World \0\n"
```

## Bash 5

`null_char.sh`

```bash
printf "Hello World \0\n"
```

## Lua

`null_char.lua`

```lua
print("Hello World \0")
```

## C#

`NullChar.cs`

```csharp
class NullChar {
  public static void Main(string[] args) {
    Console.WriteLine("Hello World \0");
  }
}
```

## Go

`null_char.go`

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello World \x00")
}
```

## Swift

`null_char.swift`

```swift
print("Hello World \0")
```

## Raku

`null_char.raku`

```raku
use v6;

print "Hello World \0\n";
```

## Rust

`null_char.rs`

```rust
fn main() {
    println!("Hello World \0");
}
```

