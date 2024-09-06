+++
title = read_json_file
draft = true
+++

# read_json_file

Test that a JSON file is read correctly

## Python

`read_json_file.py`

```python
"""Read JSON file, transform and print to stdout"""
import json
import sys

json_file = sys.argv[1]

with open(json_file, "r") as f:
    people = json.load(f)

for person in people:
    print(f"Hello, {person['age']} year old {person['first_name']}")
```

## Ruby

`read_json_file.rb`

```ruby
# Read JSON file, transform and print to stdout
require 'json'

json_file = ARGV[0]

people = JSON.load_file(json_file)

people.each do |person|
  puts "Hello, #{person['age']} year old #{person['first_name']}"
end
```

## Nodejs

`read_json_file.mjs`

```javascript
// Read JSON file, transform and print to stdout
import fs from 'fs/promises'

const jsonFile = process.argv[2]

const data = await fs.readFile(jsonFile, 'utf8')
const people = JSON.parse(data)

for (const person of people) {
  console.log(`Hello, ${person.age} year old ${person.first_name}`)
}
```

## Deno

`read_json_file.mjs`

```javascript
// Read JSON file, transform and print to stdout
const jsonFile = Deno.args[0];

const data = await Deno.readTextFile(jsonFile);

const people = JSON.parse(data);

for (const person of people) {
    console.log(`Hello, ${person.age} year old ${person.first_name}`);
}
```

## Php

`read_json_file.php`

```php
<?php
// Read JSON file, transform, and print to stdout


$jsonFile = $argv[1];

// Read JSON data from the file
$jsonData = file_get_contents($jsonFile);

// Parse JSON data
$people = json_decode($jsonData);

foreach ($people as $person) {
    echo "Hello, {$person->age} year old {$person->first_name}\n";
}
```

## R

`read_json_file.R`

```r
#' Read JSON file, transform and print to stdout

library(jsonlite)

# Get the JSON file path from the command line arguments
args <- commandArgs(trailingOnly = TRUE)

# Read and parse the JSON file as a list of named lists
people <- fromJSON(args[1])

# Iterate through the list of people and print the transformed message
for (i in 1:nrow(people)){
    cat(paste0("Hello, ", people$age[i], " year old ", people$first_name[i], "\n"))
}
```

## Perl

`read_json_file.pl`

```perl
# Read JSON file, transform and print to stdout
use strict;
use warnings;
use JSON;

open my $fh, '<', $ARGV[0] or die "Cannot open file: $ARGV[0]\n";

my $people = decode_json(do { local $/; <$fh> });

print "Hello, $_->{'age'} year old $_->{'first_name'}\n" for @$people;
```

## Java

`ReadJsonFile.java`

```java
// Read JSON file, transform and print to stdout
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;

public class ReadJsonFile {
    public static void main(String[] args) throws IOException{
        if (args.length < 1) {
            System.out.println("Usage: java ReadJsonFile <json_file>");
            return;
        }
        JsonNode people = new ObjectMapper().readTree(new File(args[0]));
        people.forEach(person -> System.out.println("Hello, " + person.get("age").asLong() + " year old " + person.get("first_name").asText()));

    }
}
```

## Lua

`read_json_file.lua`

```lua
-- Lua script to read JSON file, parse, and print to stdout

local cjson = require("dkjson")

local file_path = arg[1]
local fh = io.open(file_path, "r")
local json_content = fh:read("*a")
fh:close()

local people = cjson.decode(json_content)

for _, person in ipairs(people) do
    print(string.format("Hello, %d year old %s", person.age, person.first_name))
end
```

## C#

`ReadJsonFile.cs`

```csharp
// Read JSON file, transform and print to stdout
using System;
using System.IO;
using System.Text.Json;

class ReadJsonFile{
    public static void Main(string[] args){
        string jsonFilePath = args[0];
        string jsonContent = File.ReadAllText(jsonFilePath);

        JsonElement root = JsonDocument.Parse(jsonContent).RootElement;

        foreach (JsonElement person in root.EnumerateArray()){
            long age = person.GetProperty("age").GetInt64();
            string firstName = person.GetProperty("first_name").GetString();
            Console.WriteLine($"Hello, {age} year old {firstName}");
        }
    }
}
```

## Go

`read_json_file.go`

```go
package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type Person struct {
	FirstName string `json:"first_name"`
	Age       int64  `json:"age"`
}

func main() {

	file := os.Args[1]
	data, _ := os.ReadFile(file)

	var people []Person
	json.Unmarshal(data, &people)

	for _, person := range people {
		fmt.Printf("Hello, %d year old %s\n", person.Age, person.FirstName)
	}
}
```

## Swift

`read_json_file.swift`

```swift
//Read JSON file, transform and print to stdout
import Foundation

guard let jsonFile = CommandLine.arguments.dropFirst().first else {
    print("Usage: swift script.swift <json_file>")
    exit(1)
}

let fileURL = URL(fileURLWithPath: jsonFile)
let jsonData = try Data(contentsOf: fileURL)
let people = try JSONSerialization.jsonObject(with: jsonData) as! [[String: Any]]

for (_, person) in people.enumerated() {
    let age = person["age"] as! Int
    let firstName = person["first_name"] as! String

    print("Hello, \(age) year old \(firstName)")
}
```

## Raku

`read_json_file.raku`

```raku
# Read JSON file, transform and print to stdout
use v6;
use JSON::Fast;

my $file-path = @*ARGS[0];

my $fh = open $file-path, :r;

my $people = from-json($fh.slurp-rest);

for @$people -> $person {
    say "Hello, {$person<age>} year old {$person<first_name>}";
}

$fh.close;
```

## Rust

`read_json_file.rs`

```rust
//cargo-deps: json="0.12.4"

use std::env;
use std::fs;
extern crate json;
fn main() {
    let filename = env::args().nth(1).unwrap();

    let json_string = fs::read_to_string(filename).unwrap();
    let parsed_json = json::parse(&json_string).unwrap();

    let people = parsed_json.members();
    for person in people {
        let age = person["age"].as_u32().unwrap();
        let first_name = person["first_name"].as_str().unwrap();
        println!("Hello, {} year old {}", age, first_name);
    }
}
```

