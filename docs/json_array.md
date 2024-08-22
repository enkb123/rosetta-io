# json_array

## Python

`json_array.py`

```python
"""Script takes args and turns into JSON array"""
import json
import sys


my_strings = sys.argv[1:]

# Cast to JSON and print to stdout
print(json.dumps(my_strings))

```

## Ruby

`json_array.rb`

```ruby
# Script takes args and turns into JSON array
require 'json'

my_strings = ARGV

puts JSON.generate(my_strings)
```

## Nodejs

`json_array.mjs`

```javascript
// Script takes args and turns into JSON array

const myStrings = process.argv.slice(2) // Get command-line arguments, excluding 'node' and script name

console.log(JSON.stringify(myStrings))
```

## Deno

`json_array.mjs`

```javascript
// Script takes args and turns into JSON array

const myStrings = Deno.args // Get command-line arguments, excluding 'node' and script name

console.log(JSON.stringify(myStrings))

```

## Php

`json_array.php`

```php
<?php
// Script takes args and turns into JSON array

// Get the command-line arguments into an array
$myStrings = array_slice($argv, 1);

// Encode the array as JSON and print to stdout
echo json_encode($myStrings) . "\n";

```

## R

`json_array.R`

```r
#' Script takes command line arguments and turns into JSON array
library(jsonlite)

# Get the command-line arguments (strings)
args <- commandArgs(trailingOnly = TRUE)

# Convert the strings to a JSON array and print to stdout
cat(toJSON(args))

```

## Perl

`json_array.pl`

```perl
# Script takes args and turns into JSON array
use strict;
use warnings;
use JSON;

print encode_json(\@ARGV), "\n";

```

## Java

`JsonArray.java`

```java
//Script takes args and turns into JSON array

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
-- Lua script to convert command-line arguments to JSON array

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
//Script takes args and turns into JSON array

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
//Script takes args and turns into JSON array

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
//Script takes args and turns into JSON array

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
# Script takes args and turns into JSON array
use v6;

use JSON::Fast;

say to-json(@*ARGS);

```

