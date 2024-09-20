+++
title = ''
draft = false
+++

# read_json_file

Read and parse a JSON file

## Python

`read_json_file.py`

```python
import json

json_file = "people.json"

with open(json_file, "r") as f:
    people = json.load(f)

for person in people:
    print(f"Hello, {person['age']} year old {person['first_name']}")
```

## Ruby

`read_json_file.rb`

```ruby
require 'json'

people = JSON.load_file("people.json")

people.each do |person|
  puts "Hello, #{person['age']} year old #{person['first_name']}"
end
```

## Nodejs

`read_json_file.mjs`

```javascript
import fs  from 'fs'

const filePath = './people.json';

fs.readFile(filePath, 'utf8', (_, data) => {

  const people = JSON.parse(data);

  people.forEach(person => {
      console.log(`Hello, ${person.age} year old ${person.first_name}`);
  });

});
```

## Deno

`read_json_file.mjs`

```javascript
const filePath = "./people.json";

const data = await Deno.readTextFile(filePath);

const people = JSON.parse(data);

for (const person of people) {
    console.log(`Hello, ${person.age} year old ${person.first_name}`);
}
```

## Php

`read_json_file.php`

```php
<?php

$filePath = 'people.json';

$jsonString = file_get_contents($filePath);

$people = json_decode($jsonString, true);

foreach ($people as $person) {
    $age = $person['age'];
    $firstName = $person['first_name'];
    echo "Hello, $age year old $firstName\n";
}
```

## R

`read_json_file.R`

```r
library(jsonlite)

filename <- "people.json"

people <- fromJSON(filename)

for (i in 1:nrow(people)){
    cat(paste0("Hello, ", people$age[i], " year old ", people$first_name[i], "\n"))
}
```

## Perl

`read_json_file.pl`

```perl
use strict;
use warnings;
use JSON;

my $file_path = 'people.json';

my $json_string;
{
    local $/;
    open my $fh, '<', $file_path;
    $json_string = <$fh>;
    close $fh;
}

my $people = decode_json($json_string);

foreach my $person (@$people) {
    my $age = $person->{age};
    my $first_name = $person->{first_name};
    print "Hello, $age year old $first_name\n";
}
```

## Java

`ReadJsonFile.java`

```java
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.File;
import java.io.IOException;

public class ReadJsonFile {
    public static void main(String[] args) throws IOException{
        String filePath = "people.json";
        ObjectMapper objectMapper = new ObjectMapper();

        JsonNode people = objectMapper.readTree(new File(filePath));
        for (JsonNode person : people) {
            int age = person.get("age").asInt();
            String firstName = person.get("first_name").asText();
            System.out.printf("Hello, %d year old %s%n", age, firstName);
        }
    }
}
```

## Bash 3

`read_json_file.sh`

```bash
file_path="people.json"

jq -c '.[]' "$file_path" | while IFS= read -r person; do
    age=$(echo "$person" | jq -r '.age')
    first_name=$(echo "$person" | jq -r '.first_name')
    echo "Hello, $age year old $first_name"
done
```

## Bash 5

`read_json_file.sh`

```bash
file_path="people.json"

jq -c '.[]' "$file_path" | while IFS= read -r person; do
    age=$(echo "$person" | jq -r '.age')
    first_name=$(echo "$person" | jq -r '.first_name')
    echo "Hello, $age year old $first_name"
done
```

## Lua

`read_json_file.lua`

```lua
local cjson = require("dkjson")

local filePath = "people.json"

local function readFile(filePath)
    local file = io.open(filePath, "r")
    local content = file:read("*a")
    file:close()
    return content
end

local jsonString = readFile(filePath)
local people, pos = cjson.decode(jsonString, 1, nil)

for _, person in ipairs(people) do
    print(string.format("Hello, %d year old %s", person.age, person.first_name))
end
```

## C#

`ReadJsonFile.cs`

```csharp
using System;
using System.IO;
using System.Text.Json;

class ReadJsonFile
{
    public static void Main(string[] args)
    {
        string filePath = "people.json";

        var json = File.ReadAllText(filePath);

        var people = JsonSerializer.Deserialize<JsonElement[]>(json);

        foreach (var person in people)
        {
            var age = person.GetProperty("age").GetInt32();
            var firstName = person.GetProperty("first_name").GetString();
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

func main() {
	filePath := "people.json"

	file, _ := os.Open(filePath)
	defer file.Close()

	var people []map[string]interface{}
	decoder := json.NewDecoder(file)
	decoder.Decode(&people)

	for _, person := range people {
		age := person["age"].(float64)
		firstName := person["first_name"].(string)
		fmt.Printf("Hello, %.0f year old %s\n", age, firstName)
	}
}
```

## Swift

`read_json_file.swift`

```swift
import Foundation

let jsonFile = "people.json"

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
use v6;
use JSON::Fast;

my $file-path = "people.json";

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
    let filename = "people.json";

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

