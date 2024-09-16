+++
title = ''
draft = false
+++

# json_object_with_array_values

Test that a JSON object with arrays as values is parsed correctly

## Python

`json_object_with_array_values.py`

```python
import json
import sys

my_strings = sys.argv[1:]

string_letters_dict = {string: [s.upper() for s in string] for string in my_strings}

print(json.dumps(string_letters_dict))
```

## Ruby

`json_object_with_array_values.rb`

```ruby
require 'json'

my_strings = ARGV

string_letters_dict = my_strings.to_h { |string| [string, string.upcase.chars] }

puts JSON.generate(string_letters_dict)
```

## Nodejs

`json_object_with_array_values.mjs`

```javascript
const myStrings = process.argv.slice(2)

const stringLettersDict = {}

for (const string of myStrings) {
    const uppercaseLetters = [...string].map((s) => s.toUpperCase())
    stringLettersDict[string] = uppercaseLetters
}

console.log(JSON.stringify(stringLettersDict))
```

## Deno

`json_object_with_array_values.mjs`

```javascript
const myStrings = Deno.args

const stringLettersDict = {}

for (const string of myStrings) {
    const uppercaseLetters = [...string].map((s) => s.toUpperCase())
    stringLettersDict[string] = uppercaseLetters
}

console.log(JSON.stringify(stringLettersDict))
```

## Php

`json_object_with_array_values.php`

```php
<?php
$myStrings = array_slice($argv, 1);

$stringLettersDict = array_combine(
    $myStrings, array_map(
        fn($str) => str_split(strtoupper($str)), $myStrings
    )
);

echo json_encode($stringLettersDict);
```

## R

`json_object_with_array_values.R`

```r
library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

string_letters <- list()
for (string in args) {
  letters <- toupper(strsplit(string, split="")[[1]])
  string_letters[[string]] <- letters
}

cat(toJSON(string_letters))
```

## Perl

`json_object_with_array_values.pl`

```perl
use strict;
use warnings;
use JSON;

print JSON->new
    ->canonical(1)
    ->encode({ map { $_ => [split //, uc($_)] } @ARGV });
```

## Java

`JsonObjectWithArrayValues.java`

```java
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;

import java.util.Arrays;

public class JsonObjectWithArrayValues {
    public static void main(String[] args) throws Exception{
        if (args.length == 0) {
            System.out.println("Usage: java JsonFromStrings <string1> <string2> ...");
            System.exit(1);
        }

        ObjectMapper objectMapper = new ObjectMapper();

        ObjectNode jsonObject = objectMapper.createObjectNode();

        Arrays.stream(args).forEach(str -> {
            ArrayNode lettersArray = objectMapper.createArrayNode();
            str.toUpperCase().chars().forEach(c -> lettersArray.add(String.valueOf((char) c)));
            jsonObject.set(str, lettersArray);
        });

        String jsonString = objectMapper.writeValueAsString(jsonObject);
        System.out.println(jsonString);
    }
}
```

## Lua

`json_object_with_array_values.lua`

```lua
local cjson = require("dkjson")

local string_letters_dict = {}

for i = 1, #arg do
    local string = arg[i]
    local letters = {}

    for letter in string:gmatch(".") do
        table.insert(letters, letter:upper())
    end
    string_letters_dict[string] = letters
end

print(cjson.encode(string_letters_dict))
```

## C#

`JsonObjectWithArrayValues.cs`

```csharp
using System;
using System.Collections.Generic;
using System.Text;
using System.Text.Json;

class JsonObjectWithArrayValues{
    public static void Main(string[] args){
        var jsonObject = args.ToDictionary(
            str => str,
            str => str.ToUpper().Select(c => c.ToString()).ToList()
        );

        string jsonString = JsonSerializer.Serialize(jsonObject);
        Console.WriteLine(jsonString);
    }
}
```

## Go

`json_object_with_array_values.go`

```go
package main

import (
	"encoding/json"
	"fmt"
	"os"
	"strings"
)

func main() {
	args := os.Args[1:]

	jsonObject := make(map[string][]string)

	for _, str := range args {
		var lettersArray []string
		for _, char := range strings.ToUpper(str) {
			lettersArray = append(lettersArray, string(char))
		}
		jsonObject[str] = lettersArray
	}

	jsonObjectBytes, _ := json.Marshal(jsonObject)

	fmt.Println(string(jsonObjectBytes))
}
```

## Swift

`json_object_with_array_values.swift`

```swift
import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: swift script.swift <arg1> [<arg2> ...]")
    exit(1)
}

let myStrings = CommandLine.arguments.dropFirst()

let stringLettersDict = Dictionary(uniqueKeysWithValues: myStrings.map {
    ($0, $0.map { String($0).uppercased() })
})

let jsonData = try JSONSerialization.data(withJSONObject: stringLettersDict)
print(String(data: jsonData, encoding: .utf8)!)
```

## Raku

`json_object_with_array_values.raku`

```raku
use v6;
use JSON::Fast;

my %data = @*ARGS.map: { $_ => [ .uc.comb ] };
say to-json(%data);
```

## Rust

`json_object_with_array_values.rs`

```rust
//cargo-deps: json="0.12.4"

use json::JsonValue;
use std::env;

extern crate json;
fn main() {
    let args: Vec<String> = env::args().skip(1).collect();

    let mut json_object = JsonValue::new_object();

    for arg in args {
        let letters_array: JsonValue = arg
            .to_uppercase()
            .chars()
            .map(|c| c.to_string().into())
            .collect::<Vec<JsonValue>>()
            .into();

        json_object[arg] = letters_array;
    }

    println!("{}", json_object.dump());
}
```

