+++
title = ''
draft = false
+++

# json_control_chars

Test that control characters and emojis are output in valid JSON.

## Python

```python {filename="json_control_chars.py"}
import json
import sys

test_string = sys.argv[1]

print(json.dumps(test_string))
```

## Ruby

```ruby {filename="json_control_chars.rb"}
require 'json'

test_string = ARGV[0]

puts JSON.generate(test_string)
```

## Nodejs

```javascript {filename="json_control_chars.mjs"}
const myString = process.argv[2]

console.log(JSON.stringify(myString))
```

## Deno

```javascript {filename="json_control_chars.mjs"}
const myString = Deno.args[0]

console.log(JSON.stringify(myString))
```

## Php

```php {filename="json_control_chars.php"}
<?php

$testString = $argv[1];

echo json_encode($testString);
```

## R

```r {filename="json_control_chars.R"}
library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

cat(toJSON(args, auto_unbox = TRUE))
```

## Perl

```perl {filename="json_control_chars.pl"}
use strict;
use warnings;
use JSON;

print JSON->new->encode($ARGV[0]);
```

## Java

```java {filename="JsonControlChars.java"}
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

```bash {filename="json_control_chars.sh"}
echo -n "$1" | jq -R -s .
```

## Bash 5

```bash {filename="json_control_chars.sh"}
echo -n "$1" | jq -R -s .
```

## Lua

```lua {filename="json_control_chars.lua"}
local cjson = require("dkjson")

print(cjson.encode(arg[1]))
```

## C#

```csharp {filename="JsonControlChars.cs"}
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

```go {filename="json_control_chars.go"}
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

```swift {filename="json_control_chars.swift"}
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

```raku {filename="json_control_chars.raku"}
use v6;

use JSON::Fast;

say to-json(@*ARGS[0]);
```

## Rust

```rust {filename="json_control_chars.rs"}
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

