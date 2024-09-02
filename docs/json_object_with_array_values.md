# json_object_with_array_values

Test that a JSON object with arrays as values is parsed correctly

## Python

`json_object_with_array_values.py`

```python
"""Script takes args and transforms into python dict with arrays as dict values"""
import json
import sys


my_strings = sys.argv[1:]

# Make dict with the string as key and list of letters as value
string_letters_dict = {string: [s.upper() for s in string] for string in my_strings}

# Cast to JSON and print to stdout
print(json.dumps(string_letters_dict))
```

## Ruby

`json_object_with_array_values.rb`

```ruby
# Script takes arguments and transforms them into dict with arrays as dict values
# and returns as JSON
require 'json'

my_strings = ARGV

# Make dict with the string as key and list of letters as value
string_letters_dict = my_strings.to_h { |string| [string, string.upcase.chars] }

# Cast to JSON and print to stdout
puts JSON.generate(string_letters_dict)
```

## Nodejs

`json_object_with_array_values.mjs`

```javascript
// Script takes command line args and transforms into python dict with arrays as dict values

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
// Script takes command line args and transforms into python dict with arrays as dict values

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
// Script takes args and transforms into python dict with arrays as dict values

// Get the command-line arguments into an array
$myStrings = array_slice($argv, 1);

// Create an associative array (dictionary) with each string as a key and an array of letters as the value
$stringLettersDict = array_combine(
    $myStrings, array_map(
        fn($str) => str_split(strtoupper($str)), $myStrings
    )
);

// Encode the dictionary as JSON and print to stdout
echo json_encode($stringLettersDict) . "\n";
```

## R

`json_object_with_array_values.R`

```r
#' Script transforms command-line arguments into JSON object
library(jsonlite)

# Get the command-line arguments (strings)
args <- commandArgs(trailingOnly = TRUE)

# Create a named list with the string as the key and a list of uppercase letters as the value
string_letters <- list()
for (string in args) {
  letters <- toupper(strsplit(string, split="")[[1]])
  string_letters[[string]] <- letters
}

# Convert the named list to JSON and print to stdout
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
// Script takes arguments and transforms them into dict with arrays as dict values
// and returns as JSON

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
-- Lua script to transform string arguments into a Lua table of arrays and output as JSON

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
// Script takes arguments and transforms them into dict with arrays as dict values and returns as JSON

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
// Script takes arguments and transforms them into dict with arrays as dict values
// and returns as JSON

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
//Script takes args and transforms into python dict with arrays as dict values
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

