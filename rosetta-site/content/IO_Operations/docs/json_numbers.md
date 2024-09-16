+++
title = ''
draft = false
+++

# json_numbers

Test that JSON list of numbers is parsed correctly

## Python

`json_numbers.py`

```python
import json
import sys


my_strings = sys.argv[1:]

string_lengths = [len(string) for string in my_strings]

print(json.dumps(string_lengths))
```

## Ruby

`json_numbers.rb`

```ruby
require 'json'

my_strings = ARGV

string_lengths = my_strings.map(&:length)

puts JSON.generate(string_lengths)
```

## Nodejs

`json_numbers.mjs`

```javascript
const myStrings = process.argv.slice(2)

const stringLengths = myStrings.map((string) => string.length)

const jsonString = JSON.stringify(stringLengths)

console.log(jsonString)
```

## Deno

`json_numbers.mjs`

```javascript
const myStrings = Deno.args

const stringLengths = myStrings.map((string) => string.length)

const jsonString = JSON.stringify(stringLengths)

console.log(jsonString)
```

## Php

`json_numbers.php`

```php
<?php

$myStrings = array_slice($argv, 1);

$stringLengths = array_map('strlen', $myStrings);

echo json_encode($stringLengths);
```

## R

`json_numbers.R`

```r
library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

string_lengths <- sapply(args, nchar)

cat(toJSON(string_lengths))
```

## Perl

`json_numbers.pl`

```perl
use strict;
use warnings;
use JSON;

print encode_json([map { length } @ARGV]);
```

## Java

`JsonNumbers.java`

```java
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;

public class JsonNumbers {
    public static void main(String[] args) throws Exception{
        if (args.length == 0) {
            System.out.println("Usage: java JsonNumbers <string1> <string2> ...");
            System.exit(1);
        }
        ObjectMapper objectMapper = new ObjectMapper();
        ArrayNode arrayNode = objectMapper.createArrayNode();

        for (String str : args) {
            arrayNode.add(str.length());
        }

        String jsonArrayString = objectMapper.writeValueAsString(arrayNode);
        System.out.println(jsonArrayString);
    }
}
```

## Bash 3

`json_numbers.sh`

```bash
#!/bin/bash

lengths=()

for arg in "$@"; do
  lengths+=("${#arg}")
done

jo -a "${lengths[@]}"
```

## Bash 5

`json_numbers.sh`

```bash
#!/bin/bash

lengths=()

for arg in "$@"; do
  lengths+=("${#arg}")
done

jo -a "${lengths[@]}"
```

## Lua

`json_numbers.lua`

```lua
local cjson = require("dkjson")

local lengths = {}
for i = 1, #arg do
    table.insert(lengths, string.len(arg[i]))
end

print(cjson.encode(lengths))
```

## C#

`JsonNumbers.cs`

```csharp
using System;
using System.Collections.Generic;
using System.Text;
using System.Text.Json;

class JsonNumbers
{
    public static void Main(string[] args)
    {
        var numbers = args.Select(arg => arg.Length).ToArray();

        string jsonArrayString = JsonSerializer.Serialize(numbers);
        Console.WriteLine(jsonArrayString);
    }
}
```

## Go

`json_numbers.go`

```go
package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	args := os.Args[1:]

	var lengths []int

	for _, arg := range args {
		lengths = append(lengths, len(arg))
	}

	jsonArrayBytes, _ := json.Marshal(lengths)

	fmt.Println(string(jsonArrayBytes))
}
```

## Swift

`json_numbers.swift`

```swift
import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: swift script.swift <arg1> [<arg2> ...]")
    exit(1)
}

let myStrings = CommandLine.arguments.dropFirst()

let stringLengths = myStrings.map { $0.count }

let jsonData = try JSONSerialization.data(withJSONObject: stringLengths)
print(String(data: jsonData, encoding: .utf8)!)
```

## Raku

`json_numbers.raku`

```raku
use v6;

use JSON::Fast;

say to-json(@*ARGS.map(*.chars));
```

## Rust

`json_numbers.rs`

```rust
//cargo-deps: json="0.12.4"

use json::JsonValue;
use std::env;

extern crate json;

fn main() {
    let args = env::args().skip(1);

    let json_array: JsonValue = args
        .map(|arg| arg.len().into())
        .collect::<Vec<JsonValue>>()
        .into();

    println!("{}", json_array.dump());
}
```

