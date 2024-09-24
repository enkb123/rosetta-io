+++
title = ''
draft = false
+++

# json_stdout_object

Create and output a JSON object

## Python

```python {filename="json_stdout_object.py"}
import json
import sys

my_strings = sys.argv[1:]

string_length_dict = {string: len(string) for string in my_strings}

print(json.dumps(string_length_dict))
```

## Ruby

```ruby {filename="json_stdout_object.rb"}
require 'json'

my_strings = ARGV

string_length_dict = my_strings.to_h { |string| [string, string.length] }

puts JSON.generate(string_length_dict)
```

## Nodejs

```javascript {filename="json_stdout_object.mjs"}
const myStrings = process.argv.slice(2)

const stringLengthDict = {}

for (const string of myStrings) {
  stringLengthDict[string] = string.length
}

console.log(JSON.stringify(stringLengthDict))
```

## Deno

```javascript {filename="json_stdout_object.mjs"}
const myStrings = Deno.args

const stringLengthDict = {}

for (const string of myStrings) {
  stringLengthDict[string] = string.length
}

console.log(JSON.stringify(stringLengthDict))
```

## Php

```php {filename="json_stdout_object.php"}
<?php
$myStrings = array_slice($argv, 1);

$stringLengthDict = array_combine($myStrings, array_map('strlen', $myStrings));

echo json_encode($stringLengthDict);
```

## R

```r {filename="json_stdout_object.R"}
library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

string_length <- list()
for (string in args) {
  string_length[[string]] <- nchar(string)
}

cat(toJSON(string_length, auto_unbox = TRUE))
```

## Perl

```perl {filename="json_stdout_object.pl"}
use strict;
use warnings;
use JSON;

print encode_json({ map { $_ => length } @ARGV });
```

## Java

```java {filename="JsonStdoutObject.java"}
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

public class JsonStdoutObject {
    public static void main(String[] args) throws Exception{
        var objectMapper = new ObjectMapper();

        var jsonObject = objectMapper.createObjectNode();

        for (String string : args) {
            jsonObject.put(string, string.length());
        }

        var jsonString = objectMapper.writeValueAsString(jsonObject);
        System.out.println(jsonString);
    }
}
```

## Bash 3

```bash {filename="json_stdout_object.sh"}
json_object='{}'

for arg in "$@"; do
    length=${#arg}
    json_object=$(<<<"$json_object" jo -f - "$arg=$length")
done

echo "$json_object"
```

## Bash 5

```bash {filename="json_stdout_object.sh"}
json_object='{}'

for arg in "$@"; do
    length=${#arg}
    json_object=$(<<<"$json_object" jo -f - "$arg=$length")
done

echo "$json_object"
```

## Lua

```lua {filename="json_stdout_object.lua"}
local cjson = require("dkjson")

local dict = {}

for i = 1, #arg do
    dict[arg[i]] = arg[i]:len()
end

print(cjson.encode(dict))
```

## C#

```csharp {filename="JsonStdoutObject.cs"}
using System;
using System.Collections.Generic;
using System.Text;
using System.Text.Json;

class JsonStdoutObject{
    public static void Main(string[] args){
        Dictionary<string, int> stringLengthDict = new Dictionary<string, int>();

        foreach (string str in args){
            stringLengthDict[str] = str.Length;
        }

        string jsonString = JsonSerializer.Serialize(stringLengthDict);
        Console.WriteLine(jsonString);
    }
}
```

## Go

```go {filename="json_stdout_object.go"}
package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	args := os.Args[1:]

	stringLengthMap := make(map[string]int)

	for _, arg := range args {
		stringLengthMap[arg] = len(arg)
	}

	jsonObjectBytes, _ := json.Marshal(stringLengthMap)
	fmt.Println(string(jsonObjectBytes))
}
```

## Swift

```swift {filename="json_stdout_object.swift"}
import Foundation

let myStrings = CommandLine.arguments.dropFirst()
let stringLengthDict = Dictionary(uniqueKeysWithValues: myStrings.map { ($0, $0.count) })

let jsonData = try JSONSerialization.data(withJSONObject: stringLengthDict)
print(String(data: jsonData, encoding: .utf8)!)
```

## Raku

```raku {filename="json_stdout_object.raku"}
use v6;
use JSON::Fast;

my %data = @*ARGS.map: { $_ => .chars };
say to-json(%data);
```

## Rust

```rust {filename="json_stdout_object.rs"}
//cargo-deps: json="0.12.4"

use json::JsonValue;
use std::env;

extern crate json;
fn main() {
    let args = env::args().skip(1);
    let mut json_object = JsonValue::new_object();

    for arg in args {
        json_object[arg] = arg.len().into();
    }

    println!("{}", json_object.dump());
}
```

