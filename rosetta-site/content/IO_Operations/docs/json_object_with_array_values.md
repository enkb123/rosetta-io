+++
title = ''
draft = false
+++

# json_object_with_array_values

Create and output a JSON object with arrays of strings as values

## Python

```python {filename="json_object_with_array_values.py"}
import json
import sys

my_strings = sys.argv[1:]

string_letters_dict = {string: [s.upper() for s in string] for string in my_strings}

print(json.dumps(string_letters_dict))
```

## Ruby

```ruby {filename="json_object_with_array_values.rb"}
require 'json'

my_strings = ARGV

string_letters_dict = my_strings.to_h { |string| [string, string.upcase.chars] }

puts JSON.generate(string_letters_dict)
```

## Nodejs

```javascript {filename="json_object_with_array_values.mjs"}
const myStrings = process.argv.slice(2)

const stringLettersDict = {}

for (const string of myStrings) {
    const uppercaseLetters = [...string].map((s) => s.toUpperCase())
    stringLettersDict[string] = uppercaseLetters
}

console.log(JSON.stringify(stringLettersDict))
```

## Deno

```javascript {filename="json_object_with_array_values.mjs"}
const myStrings = Deno.args

const stringLettersDict = {}

for (const string of myStrings) {
    const uppercaseLetters = [...string].map((s) => s.toUpperCase())
    stringLettersDict[string] = uppercaseLetters
}

console.log(JSON.stringify(stringLettersDict))
```

## Php

```php {filename="json_object_with_array_values.php"}
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

```r {filename="json_object_with_array_values.R"}
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

```perl {filename="json_object_with_array_values.pl"}
use strict;
use warnings;
use JSON;

print JSON->new
    ->canonical(1)
    ->encode({ map { $_ => [split //, uc($_)] } @ARGV });
```

## Java

```java {filename="JsonObjectWithArrayValues.java"}
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;

public class JsonObjectWithArrayValues {
    public static void main(String[] args) throws Exception {
        var objectMapper = new ObjectMapper();

        var jsonObject = objectMapper.createObjectNode();

        for (String str : args) {
            var lettersArray = objectMapper.createArrayNode();
            str.toUpperCase().chars().forEach(c -> lettersArray.add(String.valueOf((char) c)));
            jsonObject.set(str, lettersArray);
        }

        String jsonString = objectMapper.writeValueAsString(jsonObject);
        System.out.println(jsonString);
    }
}
```

## Bash 3

```bash {filename="json_object_with_array_values.sh"}
json_object='{}'

for arg in "$@"; do
    upper_chars=$(<<<"$arg" tr '[:lower:]' '[:upper:]' | fold -w1)

    json_array=$(jo -a ${upper_chars[@]})

    # merge this object with the current object
    json_object="$(<<<"$json_object" jo -f - "$arg"="$json_array")"
done

echo "$json_object"
```

## Bash 5

```bash {filename="json_object_with_array_values.sh"}
json_object='{}'

for arg in "$@"; do
    upper_chars=$(fold -w1 <<<"${arg^^}")

    json_array=$(jo -a ${upper_chars[@]})

    # merge this object with the current object
    json_object="$(<<<"$json_object" jo -f - "$arg"="$json_array")"
done

echo "$json_object"
```

## Lua

```lua {filename="json_object_with_array_values.lua"}
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

```csharp {filename="JsonObjectWithArrayValues.cs"}
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

```go {filename="json_object_with_array_values.go"}
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

```swift {filename="json_object_with_array_values.swift"}
import Foundation

let myStrings = CommandLine.arguments.dropFirst()

let stringLettersDict = Dictionary(
  uniqueKeysWithValues: myStrings.map {
    ($0, $0.map { String($0).uppercased() })
  })

let jsonData = try JSONSerialization.data(withJSONObject: stringLettersDict)
print(String(data: jsonData, encoding: .utf8)!)
```

## Raku

```raku {filename="json_object_with_array_values.raku"}
use v6;
use JSON::Fast;

my %data = @*ARGS.map: { $_ => [ .uc.comb ] };
say to-json(%data);
```

## Rust

```rust {filename="json_object_with_array_values.rs"}
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

