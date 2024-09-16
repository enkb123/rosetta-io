+++
title = ''
draft = false
+++

# json_array

Test that JSON array is parsed correctly

## Python

`json_array.py`

```python
import json
import sys

my_strings = sys.argv[1:]

print(json.dumps(my_strings))
```

## Ruby

`json_array.rb`

```ruby
require 'json'

my_strings = ARGV

puts JSON.generate(my_strings)
```

## Nodejs

`json_array.mjs`

```javascript
const myStrings = process.argv.slice(2)

console.log(JSON.stringify(myStrings))
```

## Deno

`json_array.mjs`

```javascript
const myStrings = Deno.args

console.log(JSON.stringify(myStrings))
```

## Php

`json_array.php`

```php
<?php

$myStrings = array_slice($argv, 1);

echo json_encode($myStrings);
```

## R

`json_array.R`

```r
library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

cat(toJSON(args))
```

## Perl

`json_array.pl`

```perl
use strict;
use warnings;
use JSON;

print encode_json(\@ARGV);
```

## Java

`JsonArray.java`

```java
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

## Lua

`json_array.lua`

```lua
local cjson = require("dkjson")

local args = {}
for i = 1, #arg do
    table.insert(args, arg[i])
end

print(cjson.encode(args))
```

## C#

`JsonArray.cs`

```csharp
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

`json_array.go`

```go
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

`json_array.swift`

```swift
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

`json_array.raku`

```raku
use v6;

use JSON::Fast;

say to-json(@*ARGS);
```

## Rust

`json_array.rs`

```rust
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

