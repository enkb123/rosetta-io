+++
title = ''
draft = false
+++

# encode

Encode a string as base64

## Python

`encode.py`

```python
import base64
import sys

test_string = sys.argv[1]

encoded_string = base64.b64encode(test_string.encode()).decode()

print(encoded_string)
```

## Ruby

`encode.rb`

```ruby
require 'base64'

test_string = ARGV[0]

encoded_string = Base64.encode64(test_string)

puts encoded_string
```

## Nodejs

`encode.mjs`

```javascript
const testString = process.argv[2]

const encodedString = btoa(testString)

console.log(encodedString)
```

## Deno

`encode.mjs`

```javascript
const testString = Deno.args[0]

const encodedString = btoa(testString)

console.log(encodedString)
```

## Php

`encode.php`

```php
<?php

$stringToEncode = $argv[1];

$encodedString = base64_encode($stringToEncode);

echo $encodedString;
```

## R

`encode.R`

```r
library(base64enc)

args <- commandArgs(trailingOnly = TRUE)

encoded_string <- base64encode(charToRaw(args))

cat(encoded_string)
```

## Perl

`encode.pl`

```perl
use strict;
use warnings;
use MIME::Base64;

print encode_base64($ARGV[0], '');
```

## Java

`Encode.java`

```java
import java.util.Base64;

public class Encode {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java Encode.java <test_string>");
            System.exit(1);
        }

        String testString = args[0];
        String encodedString = Base64.getEncoder().encodeToString(testString.getBytes());

        System.out.println(encodedString);
    }
}
```

## Bash 3

`encode.sh`

```bash
test_string="$1"

if [ -z "$test_string" ]; then
  echo "Usage: $0 <test_string>"
  exit 1
fi

echo -n "$test_string" | base64
```

## Bash 5

`encode.sh`

```bash
test_string="$1"

if [ -z "$test_string" ]; then
  echo "Usage: $0 <test_string>"
  exit 1
fi

echo -n "$test_string" | base64
```

## Lua

`encode.lua`

```lua
local base64 = require("base64")
print(base64.encode(arg[1]))
```

## C#

`Encode.cs`

```csharp
using System;

class Encode{
    public static void Main(string[] args){
        string testString = args[0];
        string encodedString = Convert.ToBase64String(System.Text.Encoding.UTF8.GetBytes(testString));
        Console.WriteLine(encodedString);
    }
}
```

## Go

`encode.go`

```go
package main

import (
	"encoding/base64"
	"fmt"
	"os"
)

func main() {
	fmt.Println(base64.StdEncoding.EncodeToString([]byte(os.Args[1])))
}
```

## Swift

`encode.swift`

```swift
import Foundation

guard CommandLine.arguments.count == 2 else {
    print("Usage: swift script.swift <test_string>")
    exit(1)
}

let data = CommandLine.arguments[1].data(using: .utf8)!
print(data.base64EncodedString())
```

## Raku

`encode.raku`

```raku
use v6;
use MIME::Base64;

say MIME::Base64.encode-str(@*ARGS[0]);
```

## Rust

`encode.rs`

```rust
//cargo-deps: base64="0.13"

use std::env;
extern crate base64;

fn main() {
    let test_string = env::args().nth(1).unwrap();
    let encoded_string = base64::encode(test_string);

    println!("{}", encoded_string);
}
```

