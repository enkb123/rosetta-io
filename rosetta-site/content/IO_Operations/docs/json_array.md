+++
title = ''
draft = false
+++

# json_array

Create and output a JSON array of strings

## Python

```python {filename="json_array.py"}
import json
import sys

my_strings = sys.argv[1:]

print(json.dumps(my_strings))
```

## Ruby

```ruby {filename="json_array.rb"}
require 'json'

my_strings = ARGV

puts JSON.generate(my_strings)
```

## Nodejs

```javascript {filename="json_array.mjs"}
const myStrings = process.argv.slice(2)

console.log(JSON.stringify(myStrings))
```

## Deno

```javascript {filename="json_array.mjs"}
const myStrings = Deno.args

console.log(JSON.stringify(myStrings))
```

## Php

```php {filename="json_array.php"}
<?php

$myStrings = array_slice($argv, 1);

echo json_encode($myStrings);
```

## R

```r {filename="json_array.R"}
library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

cat(toJSON(args))
```

## Perl

```perl {filename="json_array.pl"}
use strict;
use warnings;
use JSON;

print encode_json(\@ARGV);
```

## Java

```java {filename="JsonArray.java"}
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;

public class JsonArray {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java JsonArray <string1> <string2> ...");
            System.exit(1);
        }

        ObjectMapper objectMapper = new ObjectMapper();
        ArrayNode arrayNode = objectMapper.createArrayNode();

        for (String arg : args) {
            arrayNode.add(arg);
        }

        String jsonArrayString = arrayNode.toString();

        System.out.println(jsonArrayString);
    }
}
```

## Bash 3

```bash {filename="json_array.sh"}
jo -a "$@"
```

## Bash 5

```bash {filename="json_array.sh"}
jo -a "$@"
```

## Lua

```lua {filename="json_array.lua"}
local cjson = require("dkjson")

local args = {}
for i = 1, #arg do
    table.insert(args, arg[i])
end

print(cjson.encode(args))
```

## C#

```csharp {filename="JsonArray.cs"}
using System;
using System.Text.Json;

class JsonArray{
    public static void Main(string[] args){
        string[] inputArray = args;

        string jsonString = JsonSerializer.Serialize(inputArray);

        Console.WriteLine(jsonString);
    }
}
```

## Go

```go {filename="json_array.go"}
package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	args := os.Args[1:]

	var jsonArray []string

	for _, arg := range args {
		jsonArray = append(jsonArray, arg)
	}

	jsonArrayBytes, _ := json.Marshal(jsonArray)

	fmt.Println(string(jsonArrayBytes))
}
```

## Swift

```swift {filename="json_array.swift"}
import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: swift script.swift <arg1> [<arg2> ...]")
    exit(1)
}

let myStrings = Array(CommandLine.arguments.dropFirst())
let jsonData = try JSONSerialization.data(withJSONObject: myStrings)
print(String(data: jsonData, encoding: .utf8)!)
```

## Raku

```raku {filename="json_array.raku"}
use v6;

use JSON::Fast;

say to-json(@*ARGS);
```

## Rust

```rust {filename="json_array.rs"}
//cargo-deps: json="0.12.4"

use json::JsonValue;
use std::env;
extern crate json;

fn main() {
    let substrings: Vec<String> = env::args().skip(1).collect();
    let json_array: JsonValue = substrings.into();
    println!("{}", json_array.dump());
}
```

