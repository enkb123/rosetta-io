+++
title = ''
draft = false
+++

# json_outputting_data

Create and output JSON

## Python

```python {filename="json_outputting_data.py"}
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

print(json.dumps(first_json_object))
print(json.dumps(second_json_object))
print(json.dumps(third_json_object))
```

## Ruby

```ruby {filename="json_outputting_data.rb"}
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

```javascript {filename="json_outputting_data.mjs"}
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

```javascript {filename="json_outputting_data.mjs"}
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

```php {filename="json_outputting_data.php"}
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
```

## R

```r {filename="json_outputting_data.R"}
library(jsonlite)

first_json_object <- list(
  true = TRUE,
  false = FALSE,
  zero = 0,
  int = 42,
  float = 3.14,
  null = NA,
  "empty string" = "",
  # b/c R can't handle the null character in strings, we use @NULL@ to represent
  # it then replace it with the actual JSON-encoded null character later
  "a string with non-ascii characters" = "hello \n @NULL@ \u0001 world 🥸"
)

second_json_object <- list(
  "array of strings" = c("abc", "def", "ghi", "jkl"),
  "array of numbers" = c(13, 42, 9000, -7),
  "array of nothing" = list(),
  "array of mixed" = list(13, "def", NA, FALSE, list("a"), list(o = 1)),
  "array of objects" = list(
    list(name = "Bob Barker", age = 84),
    list(address1 = "123 Main St", address2 = "Apt 1")
  ),
  "array of arrays" = list(
    c("a", "b", "c"),
    c("d", "e", "f")
  )
)

third_json_object <- list(
  objects = list(
    nested = list(
      objects = list(
        are = "supported"
      )
    )
  )
)

first_json_string <- gsub("@NULL@", "\\\\u0000", toJSON(first_json_object, auto_unbox = TRUE, pretty = FALSE))
second_json_string <- toJSON(second_json_object, auto_unbox = TRUE, pretty = FALSE)
third_json_string <- toJSON(third_json_object, auto_unbox = TRUE, pretty = FALSE)

cat(first_json_string, "\n")
cat(second_json_string, "\n")
cat(third_json_string, "\n")
```

## Perl

```perl {filename="json_outputting_data.pl"}
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

```java {filename="JsonOutputtingData.java"}
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.*;

public class JsonOutputtingData {

    public static void main(String[] args) throws Exception {
        var firstJsonObject = new HashMap<>(); // Can't use Map.of() because it doesn't support null values
        firstJsonObject.put("true", true);
        firstJsonObject.put("false", false);
        firstJsonObject.put("zero", 0);
        firstJsonObject.put("int", 42);
        firstJsonObject.put("float", 3.14);
        firstJsonObject.put("null", null);
        firstJsonObject.put("empty string", "");
        firstJsonObject.put("a string with non-ascii characters", "hello \n \0 \u0001 world 🥸");

        var secondJsonObject = Map.of(
            "array of strings", List.of("abc", "def", "ghi", "jkl"),
            "array of numbers", List.of(13, 42, 9000, -7),
            "array of nothing", List.of(),
            "array of mixed", Arrays.asList(13, "def", null, false, List.of("a"), Map.of("o", 1)),
            "array of objects", List.of(
                Map.of(
                    "name", "Bob Barker",
                    "age", 84
                ),
                Map.of(
                    "address1", "123 Main St",
                    "address2", "Apt 1"
                )
            ),
            "array of arrays", List.of(
                List.of("a", "b", "c"),
                List.of("d", "e", "f")
            )
        );

        var thirdJsonObject = Map.of(
            "objects", Map.of(
                "nested", Map.of(
                    "objects", Map.of(
                        "are", "supported"
                    )
                )
            )
        );

        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.disable(com.fasterxml.jackson.databind.SerializationFeature.INDENT_OUTPUT);
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

```bash {filename="json_outputting_data.sh"}
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

```bash {filename="json_outputting_data.sh"}
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

```lua {filename="json_outputting_data.lua"}
local json = require("dkjson")

local firstJsonObject = {
    ["true"] = true,
    ["false"] = false,
    ["zero"] = 0,
    ["int"] = 42,
    ["float"] = 3.14,
    ["null"] = json.null,
    ["empty string"] = "",
    ["a string with non-ascii characters"] = "hello \n \0 \u{0001} world 🥸"
}

local secondJsonObject = {
    ["array of strings"] = {"abc", "def", "ghi", "jkl"},
    ["array of numbers"] = {13, 42, 9000, -7},
    ["array of nothing"] = {},
    ["array of mixed"] = {13, "def", json.null, false, {"a"}, {["o"] = 1}},
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

print(json.encode(firstJsonObject))
print(json.encode(secondJsonObject))
print(json.encode(thirdJsonObject))
```

## C#

```csharp {filename="JsonOutputtingData.cs"}
using System;
using System.Collections.Generic;
using System.Text.Json;

class JsonOutputtingData
{
    public static void Main(string[] args)
    {
        var firstJsonObject = new Dictionary<string, object> {
            ["true"] = true,
            ["false"] = false,
            ["zero"] = 0,
            ["int"] = 42,
            ["float"] = 3.14,
            ["null"] = (object)null,
            ["empty string"] = "",
            ["a string with non-ascii characters"] = "hello \n \0 \u0001 world 🥸"
        };

        var secondJsonObject = new Dictionary<string, object> {
            ["array of strings"] = new[] { "abc", "def", "ghi", "jkl" },
            ["array of numbers"] = new[] { 13, 42, 9000, -7 },
            ["array of nothing"] = Array.Empty<object>(),
            ["array of mixed"] = new object[] { 13, "def", null, false, new[] { "a" }, new Dictionary<string, object> { ["o"] = 1 } },
            ["array of objects"] = new[]
            {
                new Dictionary<string, object>
                {
                    ["name"] = "Bob Barker",
                    ["age"] = 84
                },
                new Dictionary<string, object> {
                    ["address1"] = "123 Main St",
                    ["address2"] = "Apt 1"
                }
            },
            ["array of arrays"] = new[] {
                new[] { "a", "b", "c" },
                new[] { "d", "e", "f" }
            }
        };

        var thirdJsonObject = new Dictionary<string, object>
        {
            ["objects"] = new Dictionary<string, object>
            {
                ["nested"] = new Dictionary<string, object>
                {
                    ["objects"] = new Dictionary<string, object>
                    {
                        ["are"] = "supported"
                    }
                }
            }
        };

        Console.WriteLine(JsonSerializer.Serialize(firstJsonObject));
        Console.WriteLine(JsonSerializer.Serialize(secondJsonObject));
        Console.WriteLine(JsonSerializer.Serialize(thirdJsonObject));
    }
}
```

## Go

```go {filename="json_outputting_data.go"}
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

```swift {filename="json_outputting_data.swift"}
import Foundation

let firstJsonObject: [String: Any] = [
  "true": true,
  "false": false,
  "zero": 0,
  "int": 42,
  "float": 3.14,
  "null": NSNull(),
  "empty string": "",
  "a string with non-ascii characters": "hello \n \0 \u{0001} world 🥸",
]

let secondJsonObject: [String: Any] = [
  "array of strings": ["abc", "def", "ghi", "jkl"],
  "array of numbers": [13, 42, 9000, -7],
  "array of nothing": [],
  "array of mixed": [13, "def", NSNull(), false, ["a"], ["o": 1]],
  "array of objects": [
    ["name": "Bob Barker", "age": 84],
    ["address1": "123 Main St", "address2": "Apt 1"],
  ],
  "array of arrays": [
    ["a", "b", "c"],
    ["d", "e", "f"],
  ],
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

```raku {filename="json_outputting_data.raku"}
use JSON::Fast;

my %first-json-object = {
    'true'                    => True,
    'false'                   => False,
    'zero'                    => 0,
    'int'                     => 42,
    'float'                   => 3.14,
    'null'                    => Nil,
    'empty string'            => '',
    'a string with non-ascii characters' => "hello \n \0 \x01 world 🥸"
};

my %second-json-object = {
    'array of strings' => ['abc', 'def', 'ghi', 'jkl'],
    'array of numbers' => [13, 42, 9000, -7],
    'array of nothing' => [],
    'array of mixed'   => [13, 'def', Nil, False, ['a'], {'o' => 1 }],
    'array of objects' => [
        { 'name' => 'Bob Barker', 'age' => 84 },
        { 'address1' => '123 Main St', 'address2' => 'Apt 1' },
    ],
    'array of arrays' => [
        ['a', 'b', 'c'],
        ['d', 'e', 'f']
    ]
};

my %third-json-object = {
    'objects' => {
        'nested' => {
            'objects' => {
                'are' => 'supported'
            }
        }
    }
};

say to-json(%first-json-object, :pretty(False));
say to-json(%second-json-object, :pretty(False));
say to-json(%third-json-object, :pretty(False));
```

## Rust

```rust {filename="json_outputting_data.rs"}
// cargo-deps: json="0.12.4"

extern crate json;

use json::{array, object, JsonValue};

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
        "array of strings" => array!["abc", "def", "ghi", "jkl"],
        "array of numbers" => array![13, 42, 9000, -7],
        "array of nothing" => array![],
        "array of mixed" => array![13, "def", JsonValue::Null, false, array!["a"], object! { "o" => 1 }],
        "array of objects" => array![
            object! { "name" => "Bob Barker", "age" => 84 },
            object! { "address1" => "123 Main St", "address2" => "Apt 1" }
        ],
        "array of arrays" => array![
            array!["a", "b", "c"],
            array!["d", "e", "f"]
        ]
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

    println!("{}", first_json_object);
    println!("{}", second_json_object);
    println!("{}", third_json_object);
}
```

