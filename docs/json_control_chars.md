# json_control_chars

## Python

`json_control_chars.py`

```python
"""Script takes control characters and outputs valid JSON"""
import json
import sys

test_string = sys.argv[1]

# Cast to JSON and print to stdout
print(json.dumps(test_string))

```

## Ruby

`json_control_chars.rb`

```ruby
# Script takes control characters and outputs valid JSON
require 'json'

test_string = ARGV[0]

# Cast to JSON and print to stdout
puts JSON.generate(test_string)

```

## Nodejs

`json_control_chars.mjs`

```javascript
// Script takes control characters and outputs valid JSON

const myString = process.argv[2]

console.log(JSON.stringify(myString))
```

## Deno

`json_control_chars.mjs`

```javascript
// Script takes control characters and outputs valid JSON

const myString = Deno.args[0]

console.log(JSON.stringify(myString))

```

## Php

`json_control_chars.php`

```php
<?php
// Script takes control characters and outputs valid JSON

// Get the command-line argument
$testString = $argv[1];

// Cast the string to JSON and print to stdout
echo json_encode($testString) . "\n";

```

## R

`json_control_chars.R`

```r
#' Script takes control characters and emoji and outputs valid JSON

library(jsonlite)

# Get the command-line arguments (strings)
args <- commandArgs(trailingOnly = TRUE)

cat(toJSON(args, auto_unbox = TRUE))

```

## Perl

`json_control_chars.pl`

```perl
# Script takes control characters and outputs valid JSON
use strict;
use warnings;
use JSON;

print JSON->new->encode($ARGV[0]);

```

## Java

`JsonControlChars.java`

```java
//Script takes control characters and outputs valid JSON
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonControlChars {
    public static void main(String[] args) throws JsonProcessingException{
        if (args.length == 0) {
            System.out.println("Usage: java JsonControlChars <test_string>");
            System.exit(1);
        }

        String testString = args[0];
        ObjectMapper objectMapper = new ObjectMapper();

        // Convert testString to JSON string
        String jsonString = objectMapper.writeValueAsString(testString);
        System.out.println(jsonString);

    }
}

```

## Lua

`json_control_chars.lua`

```lua
-- Lua script to output valid JSON from a string argument

local cjson = require("dkjson")

print(cjson.encode(arg[1]))

```

## C#

`JsonControlChars.cs`

```csharp
//Script takes control characters and outputs valid JSON
using System;
using System.Text.Json;

class JsonControlChars{
    public static void Main(string[] args){
        string testString = args[0];
        string jsonString = JsonSerializer.Serialize(testString);

        Console.WriteLine(jsonString);
    }
}


```

## Go

`json_control_chars.go`

```go
// Script takes control characters and outputs valid JSON
package main

import (
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	testString := os.Args[1]

	jsonString, _ := json.Marshal(testString)

	fmt.Println(string(jsonString))
}

```

## Swift

`json_control_chars.swift`

```swift
//Script takes control characters and outputs valid JSON
import Foundation

guard CommandLine.arguments.count == 2 else {
    print("Usage: swift JsonControlChars.swift <test_string>")
    exit(1)
}

let testString = CommandLine.arguments[1]

let jsonData = try JSONEncoder().encode(testString)
print(String(data: jsonData, encoding: .utf8)!)



```

## Raku

`json_control_chars.raku`

```raku
# Script takes control characters and outputs valid JSON
use v6;

use JSON::Fast;

say to-json(@*ARGS[0]);

```

