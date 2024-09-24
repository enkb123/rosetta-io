+++
title = ''
draft = false
+++

# decode

Decode a base64 string

## Python

```python {filename="decode.py"}
import base64
import sys

encoded_string = sys.argv[1]

decoded_string = base64.b64decode(encoded_string).decode()

print(decoded_string)
```

## Ruby

```ruby {filename="decode.rb"}
require 'base64'

encoded_string = ARGV[0]

puts Base64.decode64(encoded_string)
```

## Nodejs

```javascript {filename="decode.mjs"}
const encodedString = process.argv[2]

const decodedString = atob(encodedString)

console.log(decodedString)
```

## Deno

```javascript {filename="decode.mjs"}
const encodedString = Deno.args[0]

const decodedString = atob(encodedString)

console.log(decodedString)
```

## Php

```php {filename="decode.php"}
<?php

$encodedString = $argv[1];

echo base64_decode($encodedString);
```

## R

```r {filename="decode.R"}
library(base64enc)

args <- commandArgs(trailingOnly = TRUE)

decoded_string <- rawToChar(base64decode(args))

cat(decoded_string)
```

## Perl

```perl {filename="decode.pl"}
use strict;
use warnings;
use MIME::Base64;

print decode_base64($ARGV[0]);
```

## Java

```java {filename="Decode.java"}
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

```bash {filename="decode.sh"}
encoded_string="$1"

if [ -z "$encoded_string" ]; then
  echo "Usage: $0 <encoded_string>"
  exit 1
fi

base64 -d <<< "$encoded_string"
```

## Bash 5

```bash {filename="decode.sh"}
encoded_string="$1"

base64 -d <<< "$encoded_string"
```

## Lua

```lua {filename="decode.lua"}
local base64 = require("base64")
print(base64.decode(arg[1]))
```

## C#

```csharp {filename="Decode.cs"}
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

```go {filename="decode.go"}
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

```swift {filename="decode.swift"}
import Foundation

let encodedString = CommandLine.arguments[1]
let data = Data(base64Encoded: encodedString)
print(String(data: data!, encoding: .utf8)!)
```

## Raku

```raku {filename="decode.raku"}
use v6;
use MIME::Base64;

say MIME::Base64.decode-str(@*ARGS[0]);
```

## Rust

```rust {filename="decode.rs"}
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

