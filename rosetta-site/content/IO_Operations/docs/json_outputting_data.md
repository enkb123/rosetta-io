+++
title = ''
draft = false
+++

# json_outputting_data

Create and output JSON

## Python

`json_outputting_data.py`

```python
import json

first_json_object = {
    "true": True,
    "false": False,
    "zero": 0,
    "int": 42,
    "float": 3.14,
    "null": None,
    "empty string": "",
    "a string with non-ascii characters": "hello \n \0 \x01 world 🥸"
}

second_json_object = {
    "array of strings": ["abc", "def", "ghi", "jkl"],
    "array of numbers": [13, 42, 9000, -7],
    "array of nothing": [],
    "array of mixed": [13, "def", None, False, ["a"], {"o": 1}],
    "array of objects": [
        {"name": "Bob Barker", "age": 84},
        {"address1": "123 Main St", "address2": "Apt 1"}
    ],
    "array of arrays": [
        ["a", "b", "c"],
        ["d", "e", "f"]
    ]
}

third_json_object = {
    "objects": {
        "nested": {
            "objects": {
                "are": "supported"
            }
        }
    }
}

print(json.dumps(first_json_object, ensure_ascii=False))
print(json.dumps(second_json_object, ensure_ascii=False))
print(json.dumps(third_json_object, ensure_ascii=False))
```

## Ruby

`json_outputting_data.rb`

```ruby
require 'json'

puts JSON.generate({
    "true" => true,
    "false" => false,
    "zero" => 0,
    "int" => 42,
    "float" => 3.14,
    "null" => nil,
    "empty string" => "",
    "a string with non-ascii characters" => "hello \n \0 \u0001 world 🥸",
})

puts JSON.generate({
    "array of strings" => ["abc", "def", "ghi", "jkl"],
    "array of numbers" => [13, 42, 9000, -7],
    "array of nothing" => [],
    "array of mixed" => [13, "def", nil, false, ["a"], { "o" => 1}],
    "array of objects" => [
        { "name" => "Bob Barker", "age" => 84 },
        { "address1" => "123 Main St", "address2" => "Apt 1" },
    ],
    "array of arrays" => [
        ["a", "b", "c"],
        ["d", "e", "f"],
    ],
})

puts JSON.generate({
    "objects" => { "nested" => { "objects" => { "are" => "supported" } } },
})
```

## Nodejs

`json_outputting_data.mjs`

```javascript
const json1 = JSON.stringify({
    "true": true,
    "false": false,
    "zero": 0,
    "int": 42,
    "float": 3.14,
    "null": null,
    "empty string": "",
    "a string with non-ascii characters": "hello \n \0 \u0001 world 🥸"
}, null);

const json2 = JSON.stringify({
    "array of strings": ["abc", "def", "ghi", "jkl"],
    "array of numbers": [13, 42, 9000, -7],
    "array of nothing": [],
    "array of mixed": [13, "def", null, false, ["a"], { "o": 1 }],
    "array of objects": [
        { "name": "Bob Barker", "age": 84 },
        { "address1": "123 Main St", "address2": "Apt 1" }
    ],
    "array of arrays": [
        ["a", "b", "c"],
        ["d", "e", "f"]
    ]
}, null);

const json3 = JSON.stringify({
    "objects": { "nested": { "objects": { "are": "supported" } } }
}, null);

console.log(json1);
console.log(json2);
console.log(json3);
```

## Deno

`json_outputting_data.mjs`

```javascript
const json1 = JSON.stringify({
    "true": true,
    "false": false,
    "zero": 0,
    "int": 42,
    "float": 3.14,
    "null": null,
    "empty string": "",
    "a string with non-ascii characters": "hello \n \0 \u0001 world 🥸"
}, null);

const json2 = JSON.stringify({
    "array of strings": ["abc", "def", "ghi", "jkl"],
    "array of numbers": [13, 42, 9000, -7],
    "array of nothing": [],
    "array of mixed": [13, "def", null, false, ["a"], { "o": 1 }],
    "array of objects": [
        { "name": "Bob Barker", "age": 84 },
        { "address1": "123 Main St", "address2": "Apt 1" }
    ],
    "array of arrays": [
        ["a", "b", "c"],
        ["d", "e", "f"]
    ]
}, null);

const json3 = JSON.stringify({
    "objects": { "nested": { "objects": { "are": "supported" } } }
}, null);

console.log(json1);
console.log(json2);
console.log(json3);
```

## Php

`json_outputting_data.php`

```php
<?php

$firstJsonObject = [
    "true" => true,
    "false" => false,
    "zero" => 0,
    "int" => 42,
    "float" => 3.14,
    "null" => null,
    "empty string" => "",
    "a string with non-ascii characters" => "hello \n \0 \x01 world 🥸"
];

$secondJsonObject = [
    "array of strings" => ["abc", "def", "ghi", "jkl"],
    "array of numbers" => [13, 42, 9000, -7],
    "array of nothing" => [],
    "array of mixed" => [13, "def", null, false, ["a"], ["o" => 1]],
    "array of objects" => [
        ["name" => "Bob Barker", "age" => 84],
        ["address1" => "123 Main St", "address2" => "Apt 1"]
    ],
    "array of arrays" => [
        ["a", "b", "c"],
        ["d", "e", "f"]
    ]
];

$thirdJsonObject = [
    "objects" => [
        "nested" => [
            "objects" => [
                "are" => "supported"
            ]
        ]
    ]
];

echo json_encode($firstJsonObject, JSON_UNESCAPED_UNICODE) . "\n";
echo json_encode($secondJsonObject, JSON_UNESCAPED_UNICODE) . "\n";
echo json_encode($thirdJsonObject, JSON_UNESCAPED_UNICODE) . "\n";
?>
```

## R

`json_outputting_data.R`

```r
library(jsonlite)

# Define the first JSON object
first_json_object <- list(
  true = TRUE,
  false = FALSE,
  zero = 0,
  int = 42,
  float = 3.14,
  null = NULL,
  empty_string = "",
  a_string_with_non_ascii_characters = "hello \n \0 \u0001 world 🥸"  # Make sure the escape sequence is correct
)

# Define the second JSON object
second_json_object <- list(
  array_of_strings = c("abc", "def", "ghi", "jkl"),
  array_of_numbers = c(13, 42, 9000, -7),
  array_of_nothing = list(),  # Should be an empty list
  array_of_mixed = list(13, "def", NULL, FALSE, c("a"), list(o = 1)),
  array_of_objects = list(
    list(name = "Bob Barker", age = 84),
    list(address1 = "123 Main St", address2 = "Apt 1")
  ),
  array_of_arrays = list(
    c("a", "b", "c"),
    c("d", "e", "f")
  )
)

# Define the third JSON object
third_json_object <- list(
  objects = list(
    nested = list(
      objects = list(
        are = "supported"
      )
    )
  )
)

# Convert the R lists to JSON strings and print them
cat(toJSON(first_json_object, auto_unbox = TRUE, pretty = FALSE), "\n")
cat(toJSON(second_json_object, auto_unbox = TRUE, pretty = FALSE), "\n")
cat(toJSON(third_json_object, auto_unbox = TRUE, pretty = FALSE), "\n")
```

## Perl

`json_outputting_data.pl`

```perl
use strict;
use warnings;
use JSON;

my $json = JSON->new->utf8;

my $data1 = {
    "true" => JSON::true,
    "false" => JSON::false,
    "zero" => 0,
    "int" => 42,
    "float" => 3.14,
    "null" => undef,
    "empty string" => "",
    "a string with non-ascii characters" => "hello \n \0 \x{0001} world \N{U+1F978}",
};

print $json->encode($data1) . "\n";

my $data2 = {
    "array of strings" => ["abc", "def", "ghi", "jkl"],
    "array of numbers" => [13, 42, 9000, -7],
    "array of nothing" => [],
    "array of mixed" => [13, "def", undef, JSON::false, ["a"], { "o" => 1 }],
    "array of objects" => [
        { "name" => "Bob Barker", "age" => 84 },
        { "address1" => "123 Main St", "address2" => "Apt 1" },
    ],
    "array of arrays" => [
        ["a", "b", "c"],
        ["d", "e", "f"],
    ],
};

print $json->encode($data2) . "\n";

my $data3 = {
    "objects" => { "nested" => { "objects" => { "are" => "supported" } } },
};

print $json->encode($data3) . "\n";
```

## Java

`JsonOutputtingData.java`

```java
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.*;

public class JsonOutputtingData {

    public static void main(String[] args) throws JsonProcessingException {
        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.disable(com.fasterxml.jackson.databind.SerializationFeature.INDENT_OUTPUT);

        Map<String, Object> firstJsonObject = new LinkedHashMap<>();
        firstJsonObject.put("true", true);
        firstJsonObject.put("false", false);
        firstJsonObject.put("zero", 0);
        firstJsonObject.put("int", 42);
        firstJsonObject.put("float", 3.14);
        firstJsonObject.put("null", null);
        firstJsonObject.put("empty string", "");
        firstJsonObject.put("a string with non-ascii characters", "hello \n \0 \u0001 world 🥸");

        Map<String, Object> secondJsonObject = new LinkedHashMap<>();
        secondJsonObject.put("array of strings", Arrays.asList("abc", "def", "ghi", "jkl"));
        secondJsonObject.put("array of numbers", Arrays.asList(13, 42, 9000, -7));
        secondJsonObject.put("array of nothing", new ArrayList<>());
        secondJsonObject.put("array of mixed", Arrays.asList(13, "def", null, false, Arrays.asList("a"), Collections.singletonMap("o", 1)));
        secondJsonObject.put("array of objects", Arrays.asList(
            new LinkedHashMap<String, Object>() {{ put("name", "Bob Barker"); put("age", 84); }},
            new LinkedHashMap<String, Object>() {{ put("address1", "123 Main St"); put("address2", "Apt 1"); }}
        ));
        secondJsonObject.put("array of arrays", Arrays.asList(
            Arrays.asList("a", "b", "c"),
            Arrays.asList("d", "e", "f")
        ));

        Map<String, Object> thirdJsonObject = new LinkedHashMap<>();
        thirdJsonObject.put("objects", Collections.singletonMap("nested", Collections.singletonMap("objects", Collections.singletonMap("are", "supported"))));

        printJson(objectMapper, firstJsonObject);
        printJson(objectMapper, secondJsonObject);
        printJson(objectMapper, thirdJsonObject);
    }

    private static void printJson(ObjectMapper objectMapper, Object data) throws JsonProcessingException {
        String jsonData = objectMapper.writeValueAsString(data);
        System.out.println(jsonData);
    }
}
```

## Bash 3

`json_outputting_data.sh`

```bash
# jo can't handle the null character (\0) so we use jq to add it as a workaraound
object_with_nonascii_string='{ "a string with non-ascii characters": "hello \n \u0000 \u0001 world 🥸" }'

jo \
  true=true false=false zero=0 int=42 float=3.14 null=null  -s "empty string"="" \
  | jq -c ". + $object_with_nonascii_string"

jo \
  "array of strings=$(
    jo -a abc def ghi jkl
  )" \
  "array of numbers=$(
    jo -a 13 42 9000 -7
  )" \
  "array of nothing=$(
    jo -a </dev/null
  )" \
  "array of mixed=$(
    jo -a 13 def null false "$(jo -a a)" "$(jo o=1)"
  )" \
  "array of objects=$(
    jo -a \
      "$(jo name="Bob Barker" age=84)" \
      "$(jo address1="123 Main St" address2="Apt 1")"
  )" \
  "array of arrays=$(
    jo -a \
      "$(jo -a a b c)" \
      "$(jo -a d e f)"
  )"

jo objects="$(
  jo nested="$(
    jo objects="$(
      jo are="supported"
    )"
  )"
)"
```

## Bash 5

`json_outputting_data.sh`

```bash
# jo can't handle the null character (\0) so we use jq to add it as a workaraound
object_with_nonascii_string='{ "a string with non-ascii characters": "hello \n \u0000 \u0001 world 🥸" }'

jo \
  true=true false=false zero=0 int=42 float=3.14 null=null  -s "empty string"="" \
  | jq -c ". + $object_with_nonascii_string"

jo \
  "array of strings=$(
    jo -a abc def ghi jkl
  )" \
  "array of numbers=$(
    jo -a 13 42 9000 -7
  )" \
  "array of nothing=$(
    jo -a </dev/null
  )" \
  "array of mixed=$(
    jo -a 13 def null false "$(jo -a a)" "$(jo o=1)"
  )" \
  "array of objects=$(
    jo -a \
      "$(jo name="Bob Barker" age=84)" \
      "$(jo address1="123 Main St" address2="Apt 1")"
  )" \
  "array of arrays=$(
    jo -a \
      "$(jo -a a b c)" \
      "$(jo -a d e f)"
  )"

jo objects="$(
  jo nested="$(
    jo objects="$(
      jo are="supported"
    )"
  )"
)"
```

## Lua

`json_outputting_data.lua`

```lua
local cjson = require("dkjson")

local firstJsonObject = {
    ["true"] = true,
    ["false"] = false,
    ["zero"] = 0,
    ["int"] = 42,
    ["float"] = 3.14,
    ["null"] = cjson.null,
    ["empty string"] = "",
    ["a string with non-ascii characters"] = "hello \n \0 \u{0001} world 🥸"
}

local secondJsonObject = {
    ["array of strings"] = {"abc", "def", "ghi", "jkl"},
    ["array of numbers"] = {13, 42, 9000, -7},
    ["array of nothing"] = {},
    ["array of mixed"] = {13, "def", cjson.null, false, {"a"}, {["o"] = 1}},
    ["array of objects"] = {
        {["name"] = "Bob Barker", ["age"] = 84},
        {["address1"] = "123 Main St", ["address2"] = "Apt 1"}
    },
    ["array of arrays"] = {
        {"a", "b", "c"},
        {"d", "e", "f"}
    }
}

local thirdJsonObject = {
    ["objects"] = {
        ["nested"] = {
            ["objects"] = {
                ["are"] = "supported"
            }
        }
    }
}

print(cjson.encode(firstJsonObject))
print(cjson.encode(secondJsonObject))
print(cjson.encode(thirdJsonObject))
```

## C#

`JsonOutputtingData.cs`

```csharp
using System;
using System.Collections.Generic;
using System.Text.Json;

class JsonOutputtingData
{
    public static void Main(string[] args)
    {
        var firstJsonObject = new Dictionary<string, object>
        {
            { "true", true },
            { "false", false },
            { "zero", 0 },
            { "int", 42 },
            { "float", 3.14 },
            { "null", null },
            { "empty string", "" },
            { "a string with non-ascii characters", "hello \n \0 \u0001 world 🥸" }
        };

        var secondJsonObject = new Dictionary<string, object>
        {
            { "array of strings", new[] { "abc", "def", "ghi", "jkl" } },
            { "array of numbers", new[] { 13, 42, 9000, -7 } },
            { "array of nothing", new object[] { } },
            { "array of mixed", new object[] { 13, "def", null, false, new[] { "a" }, new Dictionary<string, object> { { "o", 1 } } } },
            { "array of objects", new[]
                {
                    new Dictionary<string, object> { { "name", "Bob Barker" }, { "age", 84 } },
                    new Dictionary<string, object> { { "address1", "123 Main St" }, { "address2", "Apt 1" } }
                }
            },
            { "array of arrays", new[]
                {
                    new[] { "a", "b", "c" },
                    new[] { "d", "e", "f" }
                }
            }
        };

        var thirdJsonObject = new Dictionary<string, object>
        {
            { "objects", new Dictionary<string, object> { { "nested", new Dictionary<string, object> { { "objects", new Dictionary<string, object> { { "are", "supported" } } } } } } }
        };

        Console.WriteLine(JsonSerializer.Serialize(firstJsonObject));
        Console.WriteLine(JsonSerializer.Serialize(secondJsonObject));
        Console.WriteLine(JsonSerializer.Serialize(thirdJsonObject));
    }
}
```

## Go

`json_outputting_data.go`

```go
package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	firstJsonObject := map[string]interface{}{
		"true":                               true,
		"false":                              false,
		"zero":                               0,
		"int":                                42,
		"float":                              3.14,
		"null":                               nil,
		"empty string":                       "",
		"a string with non-ascii characters": "hello \n \x00 \u0001 world 🥸",
	}

	secondJsonObject := map[string]interface{}{
		"array of strings": []string{"abc", "def", "ghi", "jkl"},
		"array of numbers": []int{13, 42, 9000, -7},
		"array of nothing": []interface{}{},
		"array of mixed": []interface{}{
			13, "def", nil, false, []string{"a"}, map[string]interface{}{"o": 1},
		},
		"array of objects": []interface{}{
			map[string]interface{}{"name": "Bob Barker", "age": 84},
			map[string]interface{}{"address1": "123 Main St", "address2": "Apt 1"},
		},
		"array of arrays": []interface{}{
			[]string{"a", "b", "c"},
			[]string{"d", "e", "f"},
		},
	}

	thirdJsonObject := map[string]interface{}{
		"objects": map[string]interface{}{
			"nested": map[string]interface{}{
				"objects": map[string]interface{}{
					"are": "supported",
				},
			},
		},
	}

	printJSON(firstJsonObject)
	printJSON(secondJsonObject)
	printJSON(thirdJsonObject)
}

func printJSON(data interface{}) {
	jsonData, _ := json.Marshal(data)
	fmt.Println(string(jsonData))
}
```

## Swift

`json_outputting_data.swift`

```swift
import Foundation

let firstJsonObject: [String: Any] = [
    "true": true,
    "false": false,
    "zero": 0,
    "int": 42,
    "float": 3.14,
    "null": NSNull(),
    "empty string": "",
    "a string with non-ascii characters": "hello \n \0 \u{0001} world 🥸"
]

let secondJsonObject: [String: Any] = [
    "array of strings": ["abc", "def", "ghi", "jkl"],
    "array of numbers": [13, 42, 9000, -7],
    "array of nothing": [],
    "array of mixed": [13, "def", NSNull(), false, ["a"], ["o": 1]],
    "array of objects": [
        ["name": "Bob Barker", "age": 84],
        ["address1": "123 Main St", "address2": "Apt 1"]
    ],
    "array of arrays": [
        ["a", "b", "c"],
        ["d", "e", "f"]
    ]
]

let thirdJsonObject: [String: Any] = [
    "objects": [
        "nested": [
            "objects": [
                "are": "supported"
            ]
        ]
    ]
]

func jsonString(from dictionary: [String: Any]) -> String {
    let jsonData = try! JSONSerialization.data(withJSONObject: dictionary, options: [])
    return String(data: jsonData, encoding: .utf8)!
}

print(jsonString(from: firstJsonObject))
print(jsonString(from: secondJsonObject))
print(jsonString(from: thirdJsonObject))
```

## Raku

`json_outputting_data.raku`

```raku
use JSON::Fast;

my %first_json_object = Hash.new(
    'true'                    => True,
    'false'                   => False,
    'zero'                    => 0,
    'int'                     => 42,
    'float'                   => 3.14,
    'null'                    => Nil,
    'empty string'            => '',
    'a string with non-ascii characters' => "hello \n \0 \x01 world 🥸"
);

my %second_json_object = Hash.new(
    'array of strings' => ['abc', 'def', 'ghi', 'jkl'],
    'array of numbers' => [13, 42, 9000, -7],
    'array of nothing' => [],
    'array of mixed'   => [13, 'def', Nil, False, ['a'], Hash.new('o' => 1)],
    'array of objects' => [
        Hash.new('name' => 'Bob Barker', 'age' => 84),
        Hash.new('address1' => '123 Main St', 'address2' => 'Apt 1')
    ],
    'array of arrays' => [
        ['a', 'b', 'c'],
        ['d', 'e', 'f']
    ]
);

my %third_json_object = Hash.new(
    'objects' => Hash.new(
        'nested' => Hash.new(
            'objects' => Hash.new(
                'are' => 'supported'
            )
        )
    )
);

say to-json(%first_json_object, :pretty(False));
say to-json(%second_json_object, :pretty(False));
say to-json(%third_json_object, :pretty(False));
```

## Rust

`json_outputting_data.rs`

```rust
//cargo-deps: json="0.12.4"

extern crate json;

use json::{JsonValue, object};

fn main() {
    let first_json_object = object! {
        "true" => true,
        "false" => false,
        "zero" => 0,
        "int" => 42,
        "float" => 3.14,
        "null" => JsonValue::Null,
        "empty string" => "",
        "a string with non-ascii characters" => "hello \n \0 \u{0001} world 🥸"
    };

    let second_json_object = object! {
        "array of strings" => JsonValue::Array(vec![
            "abc".into(),
            "def".into(),
            "ghi".into(),
            "jkl".into()
        ]),
        "array of numbers" => JsonValue::Array(vec![
            13.into(),
            42.into(),
            9000.into(),
            (-7).into()
        ]),
        "array of nothing" => JsonValue::Array(vec![]),
        "array of mixed" => JsonValue::Array(vec![
            13.into(),
            "def".into(),
            JsonValue::Null,
            false.into(),
            JsonValue::Array(vec!["a".into()]),
            object! { "o" => 1 }
        ]),
        "array of objects" => JsonValue::Array(vec![
            object! { "name" => "Bob Barker", "age" => 84 },
            object! { "address1" => "123 Main St", "address2" => "Apt 1" }
        ]),
        "array of arrays" => JsonValue::Array(vec![
            JsonValue::Array(vec!["a".into(), "b".into(), "c".into()]),
            JsonValue::Array(vec!["d".into(), "e".into(), "f".into()])
        ])
    };

    let third_json_object = object! {
        "objects" => object! {
            "nested" => object! {
                "objects" => object! {
                    "are" => "supported"
                }
            }
        }
    };

    println!("{}", first_json_object.dump());
    println!("{}", second_json_object.dump());
    println!("{}", third_json_object.dump());
}
```

