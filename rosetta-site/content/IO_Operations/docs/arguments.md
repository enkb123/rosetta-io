+++
title = ''
draft = false
+++

# arguments

Test that args can be passed to script

## Python

`arguments.py`

```python
import sys

print(sys.argv[1].lower())
```

## Ruby

`arguments.rb`

```ruby
puts ARGV[0].downcase
```

## Nodejs

`arguments.mjs`

```javascript
console.log(process.argv[2].toLowerCase())
```

## Deno

`arguments.mjs`

```javascript
console.log(Deno.args[0].toLowerCase())
```

## Php

`arguments.php`

```php
<?php

echo strtolower($argv[1]);
```

## R

`arguments.R`

```r
cat(tolower(commandArgs(trailingOnly = TRUE)))
```

## Perl

`arguments.pl`

```perl
use strict;
use warnings;
print lc($ARGV[0]);
```

## Java

`Arguments.java`

```java
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
use v6;

my $arg = @*ARGS[0];
say $arg.lc;
```

## Rust

`arguments.rs`

```rust
use std::env;

fn main() {
    let user = env::args().nth(1).unwrap();
    println!("{}", user.to_lowercase());
}
```

