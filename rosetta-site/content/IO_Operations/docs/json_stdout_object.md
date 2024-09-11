+++
title = ''
draft = false
+++

# json_stdout_object

Test that JSON object is parsed correctly

## Python

`json_stdout_object.py`

```python
"""Script reads string args and transforms into python dict"""
import json
import sys


my_strings = sys.argv[1:]

# Make a dict with each string as a key and it's length as the value
string_length_dict = {string: len(string) for string in my_strings}

# Cast to JSON and print to stdout
print(json.dumps(string_length_dict))
```

## Ruby

`json_stdout_object.rb`

```ruby
# Script reads string args and transforms into python dict
require 'json'

my_strings = ARGV

# Make a dict with each string as a key and it's length as the value
string_length_dict = my_strings.to_h { |string| [string, string.length] }

# Cast to JSON and print to stdout
puts JSON.generate(string_length_dict)
```

## Nodejs

`json_stdout_object.mjs`

```javascript
// Script reads string args and transforms into python dict

const myStrings = process.argv.slice(2)

// Make a dict with each string as a key and it's length as the value
const stringLengthDict = {}

for (const string of myStrings) {
  stringLengthDict[string] = string.length
}

console.log(JSON.stringify(stringLengthDict))
```

## Deno

`json_stdout_object.mjs`

```javascript
// Script reads string args and transforms into python dict

const myStrings = Deno.args

// Make a dict with each string as a key and it's length as the value
const stringLengthDict = {}

for (const string of myStrings) {
  stringLengthDict[string] = string.length
}

console.log(JSON.stringify(stringLengthDict))
```

## Php

`json_stdout_object.php`

```php
<?php
// Script reads string args and transforms into python dict

// Get the command-line arguments into an array
$myStrings = array_slice($argv, 1);

// Create an associative array (dictionary) with each string as a key and its length as the value
$stringLengthDict = array_combine($myStrings, array_map('strlen', $myStrings));

// Encode the dictionary as JSON and print to stdout
echo json_encode($stringLengthDict);
```

## R

`json_stdout_object.R`

```r
#' Script reads string arguments and transforms to JSON object

library(jsonlite)

# Get the command-line arguments (strings)
args <- commandArgs(trailingOnly = TRUE)

# Create a named list with each string as a key and its length as an atomic vector
string_length <- list()
for (string in args) {
  string_length[[string]] <- nchar(string)
}

# Convert list to JSON and print to stdout
# `auto_unbox`flag marks atomic vectors as singletons with 1 element so that the
# value won't turn into an array when encoded into JSON
cat(toJSON(string_length, auto_unbox = TRUE))
```

## Perl

`json_stdout_object.pl`

```perl
# Script reads string args and transforms into python dict
use strict;
use warnings;
use JSON;

print encode_json({ map { $_ => length } @ARGV });
```

## Java

`JsonStdoutObject.java`

```java
// Script reads string args and transforms into python dict

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

import java.util.HashMap;
import java.util.Map;

public class JsonStdoutObject {
    public static void main(String[] args) throws Exception{
        if (args.length == 0) {
            System.out.println("Usage: java JsonStdoutObject <string1> <string2> ...");
            System.exit(1);
        }

        ObjectMapper objectMapper = new ObjectMapper();

        ObjectNode jsonObject = objectMapper.createObjectNode();

        Map<String, Integer> stringLengthDict = new HashMap<>();
        for (String string : args) {
            jsonObject.put(string, string.length());
        }
        String jsonString = objectMapper.writeValueAsString(jsonObject);
        System.out.println(jsonString);
    }
}
```

## Bash 3

`json_stdout_object.sh`

```bash
#!/bin/bash

json_object='{}'

for arg in "$@"; do
    length=${#arg}
    json_object=$(<<<"$json_object" jo -f - "$arg=$length")
done

echo "$json_object"
```

## Bash 5

`json_stdout_object.sh`

```bash
#!/bin/bash

json_object='{}'

for arg in "$@"; do
    length=${#arg}
    json_object=$(<<<"$json_object" jo -f - "$arg=$length")
done

echo "$json_object"
```

## Lua

`json_stdout_object.lua`

```lua
-- Lua script to transform string arguments into a Lua table and output as JSON

local cjson = require("dkjson")

local dict = {}

for i = 1, #arg do
    dict[arg[i]] = arg[i]:len()
end

print(cjson.encode(dict))
```

## C#

`JsonStdoutObject.cs`

```csharp
// Script reads string args and transforms into python dict

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

`json_stdout_object.go`

```go
// Script reads string args and transforms into python dict

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

`json_stdout_object.swift`

```swift
//Script reads string args and transforms into python dict
import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: swift script.swift <arg1> [<arg2> ...]")
    exit(1)
}

let myStrings = CommandLine.arguments.dropFirst()
let stringLengthDict = Dictionary(uniqueKeysWithValues: myStrings.map { ($0, $0.count) })

let jsonData = try JSONSerialization.data(withJSONObject: stringLengthDict)
print(String(data: jsonData, encoding: .utf8)!)
```

## Raku

`json_stdout_object.raku`

```raku
# Script reads string args and transforms into python dict
use v6;
use JSON::Fast;

my %data = @*ARGS.map: { $_ => .chars };
say to-json(%data);
```

## Rust

`json_stdout_object.rs`

```rust
//cargo-deps: json="0.12.4"

// Script reads string args and transforms into dict

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

