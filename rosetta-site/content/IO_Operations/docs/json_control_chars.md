+++
title = ''
draft = false
+++

# json_control_chars

Test that control characters and emojis are output in valid JSON
note: control character "\0" is used by C (and Python) to end strings and so we can't
pass it as argument in the test string because it will raise "invalid argument" error


## Python

`json_control_chars.py`

```python
import json
import sys

test_string = sys.argv[1]

print(json.dumps(test_string))
```

## Ruby

`json_control_chars.rb`

```ruby
require 'json'

test_string = ARGV[0]

puts JSON.generate(test_string)
```

## Nodejs

`json_control_chars.mjs`

```javascript
const myString = process.argv[2]

console.log(JSON.stringify(myString))
```

## Deno

`json_control_chars.mjs`

```javascript
const myString = Deno.args[0]

console.log(JSON.stringify(myString))
```

## Php

`json_control_chars.php`

```php
<?php

$testString = $argv[1];

echo json_encode($testString);
```

## R

`json_control_chars.R`

```r
library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

cat(toJSON(args, auto_unbox = TRUE))
```

## Perl

`json_control_chars.pl`

```perl
use strict;
use warnings;
use JSON;

print JSON->new->encode($ARGV[0]);
```

## Java

`JsonControlChars.java`

```java
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonControlChars {
    public static void main(String[] args) throws JsonProcessingException{
        if (args.length == 0) {
            System.out.println("Usage: java JsonControlChars <test_string>");
            System.exit(1);
        }

        String testString = args[0];
        ObjectMapper objectMapper = new ObjectMapper();

        String jsonString = objectMapper.writeValueAsString(testString);
        System.out.println(jsonString);

    }
}
```

## Bash 3

`json_control_chars.sh`

```bash
echo -n "$1" | jq -R -s .
```

## Bash 5

`json_control_chars.sh`

```bash
echo -n "$1" | jq -R -s .
```

## Lua

`json_control_chars.lua`

```lua
local cjson = require("dkjson")

print(cjson.encode(arg[1]))
```

## C#

`JsonControlChars.cs`

```csharp
using System;
using System.Text.Json;

class JsonControlChars{
    public static void Main(string[] args){
        string testString = args[0];
        string jsonString = JsonSerializer.Serialize(testString);

        Console.WriteLine(jsonString);
    }
}
```

## Go

`json_control_chars.go`

```go
package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	testString := os.Args[1]

	jsonString, _ := json.Marshal(testString)

	fmt.Println(string(jsonString))
}
```

## Swift

`json_control_chars.swift`

```swift
import Foundation

guard CommandLine.arguments.count == 2 else {
    print("Usage: swift JsonControlChars.swift <test_string>")
    exit(1)
}

let testString = CommandLine.arguments[1]

let jsonData = try JSONEncoder().encode(testString)
print(String(data: jsonData, encoding: .utf8)!)
```

## Raku

`json_control_chars.raku`

```raku
use v6;

use JSON::Fast;

say to-json(@*ARGS[0]);
```

## Rust

`json_control_chars.rs`

```rust
//cargo-deps: json="0.12.4"

use json::JsonValue;
use std::env;

extern crate json;

fn main() {
    let test_string = env::args().nth(1).unwrap();

    let json_value: JsonValue = test_string.into();

    println!("{}", json_value.dump());
}
```

