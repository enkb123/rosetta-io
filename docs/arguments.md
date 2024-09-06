+++
title = arguments
draft = true
+++

# arguments

Test that args can be passed to script

## Python

`arguments.py`

```python
"""Script reads command line arguments and writes to stdout"""
import sys

print(sys.argv[1].lower())
```

## Ruby

`arguments.rb`

```ruby
# Script to read an argument and print as lowercase in stdout

puts ARGV[0].downcase
```

## Nodejs

`arguments.mjs`

```javascript
// Script to read command line argument and write to stdout

console.log(process.argv[2].toLowerCase())
```

## Deno

`arguments.mjs`

```javascript
// Script to read command line argument and write to stdout

console.log(Deno.args[0].toLowerCase())
```

## Php

`arguments.php`

```php
<?php
// Read command line arguments and write to stdout
echo strtolower($argv[1]) . "\n";
```

## R

`arguments.R`

```r
#' Script reads command line arguments and writes to stdout in lowercase

cat(tolower(commandArgs(trailingOnly = TRUE)), fill = TRUE)
```

## Perl

`arguments.pl`

```perl
# Script to read an argument and print as lowercase in stdout
use strict;
use warnings;
print lc($ARGV[0]), "\n";
```

## Java

`Arguments.java`

```java
// Script to read an argument and print as lowercase in stdout

class Main{
    public static void main(String[] args){
        String user = args[0];
        System.out.println(user.toLowerCase());
    }
}
```

## Bash 3

`arguments.sh`

```bash
#!/bin/bash

# Script to read an argument and print as lowercase in stdout
file_path="$1"

if [ -z "$file_path" ]; then
  echo "Usage: $0 <file_path>"
  exit 1
fi

tr '[:upper:]' '[:lower:]' <<< "$file_path"
```

## Bash 5

`arguments.sh`

```bash
#!/bin/bash

# Script to read an argument and print as lowercase in stdout
file_path="$1"

if [ -z "$file_path" ]; then
  echo "Usage: $0 <file_path>"
  exit 1
fi

echo "${file_path,,}"
```

## Lua

`arguments.lua`

```lua
--Script to read an argument and print as lowercase in stdout

print(arg[1]:lower())
```

## C#

`Arguments.cs`

```csharp
class Arguments
{
  public static void Main(string[] args)
  {
    Console.WriteLine(args[0].ToLower());
  }
}
```

## Go

`arguments.go`

```go
// Script to read an argument and print as lowercase in stdout

package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Println(strings.ToLower(os.Args[1]))
}
```

## Swift

`arguments.swift`

```swift
#!/usr/bin/swift

import Foundation

let args = CommandLine.arguments

guard args.count > 1 else {
    print("Usage: \(args[0]) <argument>");
    exit(1)
}

print(args[1].lowercased())
```

## Raku

`arguments.raku`

```raku
# Script to read an argument and print as lowercase in stdout
use v6;

my $arg = @*ARGS[0];
say $arg.lc;
```

## Rust

`arguments.rs`

```rust
// Script to read an argument and print as lowercase in stdout

use std::env;

fn main() {
    let user = env::args().nth(1).expect("Expected one argument");
    println!("{}", user.to_lowercase());
}
```

