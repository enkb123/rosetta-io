+++
title = ''
draft = false
+++

# json_object_array

Create and output a JSON array of objects

## Python

```python {filename="json_object_array.py"}
import json
import sys


args = sys.argv[1:]

my_array = [{arg.upper(): len(arg)} for arg in args]

print(json.dumps(my_array))
```

## Ruby

```ruby {filename="json_object_array.rb"}
require 'json'

my_strings = ARGV

my_array = my_strings.map { |string| {string.upcase => string.length} }

puts JSON.generate(my_array)
```

## Nodejs

```javascript {filename="json_object_array.mjs"}
const args = process.argv.slice(2)

const myArray = args.map((arg) => ({ [arg.toUpperCase()]: arg.length }))

console.log(JSON.stringify(myArray))
```

## Deno

```javascript {filename="json_object_array.mjs"}
const args = Deno.args

const myArray = args.map((arg) => ({ [arg.toUpperCase()]: arg.length }))

console.log(JSON.stringify(myArray))
```

## Php

```php {filename="json_object_array.php"}
<?php
$args = array_slice($argv, 1);

$myArray = array_map(function($arg) {
    return [strtoupper($arg) => strlen($arg)];
}, $args);

echo json_encode($myArray);
```

## R

```r {filename="json_object_array.R"}
library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

myArray <- list()
for (arg in args) {
    string_length <- list()
    string_length[[toupper(arg)]] <- nchar(arg)
    myArray[[length(myArray)+1]] <- string_length
}

cat(toJSON(myArray, auto_unbox=TRUE))
```

## Perl

```perl {filename="json_object_array.pl"}
use strict;
use warnings;
use JSON;

print JSON->new
    ->canonical(1)
    ->encode([map { { uc($_) => length($_) } } @ARGV]);
```

## Java

```java {filename="JsonObjectArray.java"}
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

## Bash 3

```bash {filename="json_object_array.sh"}
json_objects=()

for arg in "$@"; do
    upper_arg=$(tr '[:lower:]' '[:upper:]' <<< "$arg")
    length=${#arg}
    json_objects+=("$(jo "$upper_arg"="$length")")
done

jo -a "${json_objects[@]}"
```

## Bash 5

```bash {filename="json_object_array.sh"}
json_objects=()

for arg in "$@"; do
    json_objects+=("$(jo "${arg^^}"="${#arg}")")
done

jo -a "${json_objects[@]}"
```

## Lua

```lua {filename="json_object_array.lua"}
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

```csharp {filename="JsonObjectArray.cs"}
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

```go {filename="json_object_array.go"}
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

```swift {filename="json_object_array.swift"}
import Foundation

let args = CommandLine.arguments.dropFirst()

let myArray = args.map { [$0.uppercased(): $0.count] }

let jsonData = try JSONSerialization.data(withJSONObject: myArray)
print(String(data: jsonData, encoding: .utf8)!)
```

## Raku

```raku {filename="json_object_array.raku"}
use v6;
use JSON::Fast;

say to-json(@*ARGS.map: { uc($_) => $_.chars });
```

## Rust

```rust {filename="json_object_array.rs"}
//cargo-deps: json="0.12.4"

use json::{object, JsonValue};
use std::env;

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

