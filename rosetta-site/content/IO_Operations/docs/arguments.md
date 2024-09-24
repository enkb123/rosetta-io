+++
title = ''
draft = false
+++

# arguments

Read command line arguments

## Python

```python {filename="arguments.py"}
import sys

print("1st argument: " + sys.argv[1])
print("2nd argument: " + sys.argv[2])
```

## Ruby

```ruby {filename="arguments.rb"}
puts "1st argument: #{ARGV[0]}"
puts "2nd argument: #{ARGV[1]}"
```

## Nodejs

```javascript {filename="arguments.mjs"}
console.log("1st argument:", process.argv[2])
console.log("2nd argument:", process.argv[3])
```

## Deno

```javascript {filename="arguments.mjs"}
console.log("1st argument:", Deno.args[0])
console.log("2nd argument:", Deno.args[1])
```

## Php

```php {filename="arguments.php"}
<?php

echo "1st argument: ", $argv[1], "\n";
echo "2nd argument: ", $argv[2], "\n";
```

## R

```r {filename="arguments.R"}
args <- commandArgs(trailingOnly = TRUE)

cat("1st argument:", args[1], "\n")
cat("2nd argument:", args[2], "\n")
```

## Perl

```perl {filename="arguments.pl"}
use strict;
use warnings;

print "1st argument: ", $ARGV[0], "\n";
print "2nd argument: ", $ARGV[1], "\n";
```

## Java

```java {filename="Arguments.java"}
class Main{
    public static void main(String[] args){
        System.out.println("1st argument: " + args[0]);
        System.out.println("2nd argument: " + args[1]);
    }
}
```

## Bash 3

```bash {filename="arguments.sh"}
echo "1st argument: $1"
echo "2nd argument: $2"
```

## Bash 5

```bash {filename="arguments.sh"}
echo "1st argument: $1"
echo "2nd argument: $2"
```

## Lua

```lua {filename="arguments.lua"}
print("1st argument: "..arg[1])
print("2nd argument: "..arg[2])
```

## C#

```csharp {filename="Arguments.cs"}
class Arguments
{
  public static void Main(string[] args)
  {
    Console.WriteLine($"1st argument: {args[0]}");
    Console.WriteLine($"2nd argument: {args[1]}");
  }
}
```

## Go

```go {filename="arguments.go"}
package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("1st argument: " + os.Args[1])
	fmt.Println("2nd argument: " + os.Args[2])
}
```

## Swift

```swift {filename="arguments.swift"}
import Foundation

let args = CommandLine.arguments

print("1st argument: \(args[1])")
print("2nd argument: \(args[2])")
```

## Raku

```raku {filename="arguments.raku"}
use v6;

say "1st argument: " ~ @*ARGS[0];
say "2nd argument: " ~ @*ARGS[1];
```

## Rust

```rust {filename="arguments.rs"}
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    println!("1st argument: {}", args[1]);
    println!("2nd argument: {}", args[2]);
}
```

