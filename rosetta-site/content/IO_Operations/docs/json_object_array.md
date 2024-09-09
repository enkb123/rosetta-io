+++
title = ''
draft = true
+++

# json_object_array

Test that a JSON array made of objects is parsed correctly

## Python

`json_object_array.py`

```python
"""Script writes an array of objects to stdout"""
import json
import sys


args = sys.argv[1:]

# Make a list of dictionaries from the given args, one dict per arg
my_array = [{arg.upper(): len(arg)} for arg in args]

# Cast to JSON and print to stdout
print(json.dumps(my_array))
```

## Ruby

`json_object_array.rb`

```ruby
# Script outputs arrays of objects as JSON
require 'json'

my_strings = ARGV

# Make a list of dictionaries from the given arguments, one dict per arg
my_array = my_strings.map { |string| {string.upcase => string.length} }

# Cast to JSON and print to stdout
puts JSON.generate(my_array)
```

## Nodejs

`json_object_array.mjs`

```javascript
// Script writes an array of objects to stdout

const args = process.argv.slice(2)

// Make a list of dictionaries from the given args, one dict per arg
const myArray = args.map((arg) => ({ [arg.toUpperCase()]: arg.length }))

console.log(JSON.stringify(myArray))
```

## Deno

`json_object_array.mjs`

```javascript
// Script writes an array of objects to stdout

const args = Deno.args

// Make a list of dictionaries from the given args, one dict per arg
const myArray = args.map((arg) => ({ [arg.toUpperCase()]: arg.length }))

console.log(JSON.stringify(myArray))
```

## Php

`json_object_array.php`

```php
<?php
// Script writes an array of objects to stdout

// Get the command-line arguments into an array
$args = array_slice($argv, 1);

// Create an array of dictionaries (associative arrays), one per argument
$myArray = array_map(function($arg) {
    return [strtoupper($arg) => strlen($arg)];
}, $args);

// Encode the array as JSON and print to stdout
echo json_encode($myArray) . "\n";
```

## R

`json_object_array.R`

```r
# Script writes a JSON array of objects to stdout
library(jsonlite)

# Get the command-line arguments
args <- commandArgs(trailingOnly = TRUE)

# Create an array of named lists from the given args, one list per arg
myArray <- list()
for (arg in args) {
    string_length <- list()
    string_length[[toupper(arg)]] <- nchar(arg)
    myArray[[length(myArray)+1]] <- string_length
}

# Convert the array to a JSON array and print to stdout
cat(toJSON(myArray, auto_unbox=TRUE))
```

## Perl

`json_object_array.pl`

```perl
# Script outputs arrays of objects as JSON
use strict;
use warnings;
use JSON;

print JSON->new
    ->canonical(1)
    ->encode([map { { uc($_) => length($_) } } @ARGV]);
```

## Java

`JsonObjectArray.java`

```java
// Script outputs arrays of objects as JSON

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;

public class JsonObjectArray {
    public static void main(String[] args) throws Exception{
        if (args.length == 0) {
            System.out.println("Usage: java JsonObjectArray <string1> <string2> ...");
            System.exit(1);
        }

        ObjectMapper objectMapper = new ObjectMapper();
        ArrayNode arrayNode = objectMapper.createArrayNode();

        for (String string : args) {
            ObjectNode obj = objectMapper.createObjectNode();
            obj.put(string.toUpperCase(), string.length());
            arrayNode.add(obj);
        }

        String jsonArrayString = objectMapper.writeValueAsString(arrayNode);
        System.out.println(jsonArrayString);
    }
}
```

## Lua

`json_object_array.lua`

```lua
-- Lua script to transform string arguments into an array of dictionaries and output as JSON

local cjson = require("dkjson")

local my_array = {}

for i = 1, #arg do
    local string = arg[i]
    table.insert(my_array, {
        [arg[i]:upper()] = arg[i]:len()
    })
end

print(cjson.encode(my_array))
```

## C#

`JsonObjectArray.cs`

```csharp
// Script outputs arrays of objects as JSON
using System;
using System.Collections.Generic;
using System.Text;
using System.Text.Json;

class JsonObjectArray
{
    public static void Main(string[] args){
        var jsonObjects = args.Select(str => new Dictionary<string, object> {
            { str.ToUpper(), str.Length }
        }).ToList();
        string jsonArrayString = JsonSerializer.Serialize(jsonObjects);
        Console.WriteLine(jsonArrayString);
    }
}
```

## Go

`json_object_array.go`

```go
// Script outputs arrays of objects as JSON

package main

import (
	"encoding/json"
	"fmt"
	"os"
	"strings"
)

func main() {
	args := os.Args[1:]

	var arrayNode []map[string]interface{}

	for _, str := range args {
		obj := make(map[string]interface{})
		obj[strings.ToUpper(str)] = len(str)
		arrayNode = append(arrayNode, obj)
	}

	jsonArrayBytes, _ := json.Marshal(arrayNode)

	fmt.Println(string(jsonArrayBytes))
}
```

## Swift

`json_object_array.swift`

```swift
//Script writes an array of objects to stdout
import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: swift script.swift <arg1> [<arg2> ...]")
    exit(1)
}

let args = CommandLine.arguments.dropFirst()

let myArray = args.map { [$0.uppercased(): $0.count] }

let jsonData = try JSONSerialization.data(withJSONObject: myArray)
print(String(data: jsonData, encoding: .utf8)!)
```

## Raku

`json_object_array.raku`

```raku
# Script outputs arrays of objects as JSON
use v6;
use JSON::Fast;

say to-json(@*ARGS.map: { uc($_) => $_.chars });
```

## Rust

`json_object_array.rs`

```rust
//cargo-deps: json="0.12.4"

// Script outputs arrays of objects as JSON
use json::JsonValue;
use std::env;
use json::object;

extern crate json;
fn main() {
    let args = env::args().skip(1);
    let json_array = JsonValue::Array(
        args.into_iter()
            .map(|string| {
                object! {
                    string.to_uppercase().as_str() => string.len()
                }
            })
            .collect(),
    );

    println!("{}", json_array.dump());
}
```

