+++
title = ''
draft = false
+++

# decode

Test that base64 can be decoded as a string

## Python

`decode.py`

```python
import base64
import sys

encoded_string = sys.argv[1]

decoded_string = base64.b64decode(encoded_string).decode()

print(decoded_string)
```

## Ruby

`decode.rb`

```ruby
require 'base64'

encoded_string = ARGV[0]

decoded_string = Base64.decode64(encoded_string)

puts decoded_string
```

## Nodejs

`decode.mjs`

```javascript
const encodedString = process.argv[2]

const decodedString = atob(encodedString)

console.log(decodedString)
```

## Deno

`decode.mjs`

```javascript
const encodedString = Deno.args[0]

const decodedString = atob(encodedString)

console.log(decodedString)
```

## Php

`decode.php`

```php
<?php

$encodedString = $argv[1];

$decodedString = base64_decode($encodedString);

echo $decodedString;
```

## R

`decode.R`

```r
library(base64enc)

args <- commandArgs(trailingOnly = TRUE)

decoded_string <- rawToChar(base64decode(args))

cat(decoded_string)
```

## Perl

`decode.pl`

```perl
use strict;
use warnings;
use MIME::Base64;

print decode_base64($ARGV[0]);
```

## Java

`Decode.java`

```java
import java.util.Base64;

public class Decode {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java Decode.java <encoded_string>");
            System.exit(1);
        }

        String encodedString = args[0];
        byte[] decodedBytes = Base64.getDecoder().decode(encodedString);
        String decodedString = new String(decodedBytes);

        System.out.println(decodedString);
    }
}
```

## Bash 3

`decode.sh`

```bash
encoded_string="$1"

if [ -z "$encoded_string" ]; then
  echo "Usage: $0 <encoded_string>"
  exit 1
fi

base64 -d <<< "$encoded_string"
```

## Bash 5

`decode.sh`

```bash
encoded_string="$1"

if [ -z "$encoded_string" ]; then
  echo "Usage: $0 <encoded_string>"
  exit 1
fi

base64 -d <<< "$encoded_string"
```

## Lua

`decode.lua`

```lua
local base64 = require("base64")
print(base64.decode(arg[1]))
```

## C#

`Decode.cs`

```csharp
using System;

class Decode{
    public static void Main(string[] args){
        string encodedString = args[0];

        byte[] decodedBytes = Convert.FromBase64String(encodedString);
        string decodedString = System.Text.Encoding.UTF8.GetString(decodedBytes);

        Console.WriteLine(decodedString);
    }
}
```

## Go

`decode.go`

```go
package main

import (
	"encoding/base64"
	"fmt"
	"os"
)

func main() {
	decodedBytes, _ := base64.StdEncoding.DecodeString(os.Args[1])

	fmt.Println(string(decodedBytes))
}
```

## Swift

`decode.swift`

```swift
import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: \(CommandLine.arguments[0]) <encoded_string>")
    exit(1)
}

let encodedString = CommandLine.arguments[1]
let data = Data(base64Encoded: encodedString)
print(String(data: data!, encoding: .utf8)!)
```

## Raku

`decode.raku`

```raku
use v6;
use MIME::Base64;

say MIME::Base64.decode-str(@*ARGS[0]);
```

## Rust

`decode.rs`

```rust
//cargo-deps: base64="0.13"

extern crate base64;
use base64::decode;
use std::env;

fn main() {
    let encoded_string = env::args().nth(1).unwrap();
    let decoded_bytes = decode(encoded_string).unwrap();
    let decoded_string = String::from_utf8(decoded_bytes).unwrap();
    println!("{}", decoded_string);
}
```

