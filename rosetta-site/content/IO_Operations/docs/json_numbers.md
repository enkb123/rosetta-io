+++
title = ''
draft = false
+++

# json_numbers

Create and output a JSON array of numbers

## Python

```python {filename="json_numbers.py"}
import json
import sys


my_strings = sys.argv[1:]

string_lengths = [len(string) for string in my_strings]

print(json.dumps(string_lengths))
```

## Ruby

```ruby {filename="json_numbers.rb"}
require 'json'

my_strings = ARGV

string_lengths = my_strings.map(&:length)

puts JSON.generate(string_lengths)
```

## Nodejs

```javascript {filename="json_numbers.mjs"}
const myStrings = process.argv.slice(2)

const stringLengths = myStrings.map((string) => string.length)

const jsonString = JSON.stringify(stringLengths)

console.log(jsonString)
```

## Deno

```javascript {filename="json_numbers.mjs"}
const myStrings = Deno.args

const stringLengths = myStrings.map((string) => string.length)

const jsonString = JSON.stringify(stringLengths)

console.log(jsonString)
```

## Php

```php {filename="json_numbers.php"}
<?php

$myStrings = array_slice($argv, 1);

$stringLengths = array_map('strlen', $myStrings);

echo json_encode($stringLengths);
```

## R

```r {filename="json_numbers.R"}
library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

string_lengths <- sapply(args, nchar)

cat(toJSON(string_lengths))
```

## Perl

```perl {filename="json_numbers.pl"}
use strict;
use warnings;
use JSON;

print encode_json([map { length } @ARGV]);
```

## Java

```java {filename="JsonNumbers.java"}
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

```bash {filename="json_numbers.sh"}
lengths=()

for arg in "$@"; do
  lengths+=("${#arg}")
done

jo -a "${lengths[@]}"
```

## Bash 5

```bash {filename="json_numbers.sh"}
lengths=()

for arg in "$@"; do
  lengths+=("${#arg}")
done

jo -a "${lengths[@]}"
```

## Lua

```lua {filename="json_numbers.lua"}
local cjson = require("dkjson")

local lengths = {}
for i = 1, #arg do
    table.insert(lengths, string.len(arg[i]))
end

print(cjson.encode(lengths))
```

## C#

```csharp {filename="JsonNumbers.cs"}
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

```go {filename="json_numbers.go"}
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

```swift {filename="json_numbers.swift"}
import Foundation

let myStrings = CommandLine.arguments.dropFirst()

let stringLengths = myStrings.map { $0.count }

let jsonData = try JSONSerialization.data(withJSONObject: stringLengths)
print(String(data: jsonData, encoding: .utf8)!)
```

## Raku

```raku {filename="json_numbers.raku"}
use v6;

use JSON::Fast;

say to-json(@*ARGS.map(*.chars));
```

## Rust

```rust {filename="json_numbers.rs"}
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

