+++
title = encode
draft = true
+++

# encode

Test that a string can be encoded as base64

## Python

`encode.py`

```python
"""Script to encode a string as Base64"""
import base64
import sys

test_string = sys.argv[1]

# Encode string argument as bytes, encode as base64 then decode as string
encoded_string = base64.b64encode(test_string.encode()).decode()

# Print as a string, not bytes
print(encoded_string)
```

## Ruby

`encode.rb`

```ruby
# Script to encode a string as Base64
# Note that Line feeds are added to every 60 encoded characters
require 'base64'


test_string = ARGV[0]

# Encode string argument as string
encoded_string = Base64.encode64(test_string)

puts encoded_string
```

## Nodejs

`encode.mjs`

```javascript
// Script to encode a string as Base64

const testString = process.argv[2] // Get the Base64-encoded string from command-line arguments

const encodedString = btoa(testString)

console.log(encodedString)
```

## Deno

`encode.mjs`

```javascript
// Script to encode a string as Base64

const testString = Deno.args[0] // Get the Base64-encoded string from command-line arguments

const encodedString = btoa(testString)

console.log(encodedString)
```

## Php

`encode.php`

```php
<?php
// Script to encode a string as Base64

$stringToEncode = $argv[1];

// Encode the string as Base64
$encodedString = base64_encode($stringToEncode);

echo $encodedString . "\n";
```

## R

`encode.R`

```r
#' Script to encode text as Base64

library(base64enc)

# Get the command-line arguments (strings)
args <- commandArgs(trailingOnly = TRUE)

# Convert string to raw bytes then encode as base64
encoded_string <- base64encode(charToRaw(args))

cat(encoded_string, fill = TRUE)
```

## Perl

`encode.pl`

```perl
use strict;
use warnings;
use MIME::Base64;

print encode_base64($ARGV[0], ''), "\n";
```

## Java

`Encode.java`

```java
//Script to encode a string as Base64

import java.util.Base64;

public class Encode {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java Encode.java <test_string>");
            System.exit(1);
        }

        String testString = args[0];
        String encodedString = Base64.getEncoder().encodeToString(testString.getBytes());



        // Print the encoded string
        System.out.println(encodedString);
    }
}
```

## Bash 3

`encode.sh`

```bash
#!/bin/bash

# Script to encode a string as Base64

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
#!/bin/bash

# Script to encode a string as Base64

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
-- Lua script to encode a string as Base64
local base64 = require("base64")
print(base64.encode(arg[1]))
```

## C#

`Encode.cs`

```csharp
//Script to encode a string as Base64

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
//Script to encode a string as Base64

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
#!/usr/bin/swift
//Script to encode a string as Base64
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
    let test_string = env::args().nth(1).expect("Expected one argument");
    let encoded_string = base64::encode(test_string);

    println!("{}", encoded_string);
}
```

