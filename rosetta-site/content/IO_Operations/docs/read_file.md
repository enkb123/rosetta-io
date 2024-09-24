+++
title = ''
draft = false
+++

# read_file

Read a file line by line

## Python

```python {filename="read_file.py"}
file_path = './my-text-file.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        print(f"line: {line}")
```

## Ruby

```ruby {filename="read_file.rb"}
File.foreach("./my-text-file.txt") do |line|
  puts "line: #{line}"
end
```

## Nodejs

```javascript {filename="read_file.mjs"}
import { promises as fs } from 'fs'

const filePath = './my-text-file.txt'

const fileContent = await fs.readFile(filePath, 'utf8')

for (const line of fileContent.split("\n")) {
  if (line !== "") {
    console.log('line:', line)
  }
}
```

## Deno

```javascript {filename="read_file.mjs"}
const filePath = "./my-text-file.txt";
const fileContent = await Deno.readTextFile(filePath);

for (const line of fileContent.split("\n")) {
  if (line !== "") {
    console.log('line:', line);
  }
}
```

## Php

```php {filename="read_file.php"}
<?php

$file_path = './my-text-file.txt';

foreach (file($file_path) as $index => $line) {
    echo "line: $line";
}
```

## R

```r {filename="read_file.R"}
file_path <- "./my-text-file.txt"

lines <- readLines(file_path)

for (line in lines) {
  cat("line:", line, "\n")
}
```

## Perl

```perl {filename="read_file.pl"}
use strict;
use warnings;

my $file_path = './my-text-file.txt';
open my $fh, '<', $file_path;

print "line: $_" while <$fh>;
```

## Java

```java {filename="ReadFile.java"}
import java.nio.file.Files;
import java.nio.file.Paths;

public class ReadFile {
    public static void main(String[] args) throws Exception {
        var filePath = Paths.get("./my-text-file.txt");

        Files.lines(filePath)
            .forEach(line -> System.out.println("line: " + line));
    }
}
```

## Bash 3

```bash {filename="read_file.sh"}
file_path="./my-text-file.txt"

while IFS= read -r line; do
  echo "line: $line"

done < "$file_path"
```

## Bash 5

```bash {filename="read_file.sh"}
file_path="./my-text-file.txt"

while IFS= read -r line; do
  echo "line: $line"

done < "$file_path"
```

## Lua

```lua {filename="read_file.lua"}
local filePath = "./my-text-file.txt"

local file = io.open(filePath, "r")

for line in file:lines() do
    print("line: " .. line)
end
file:close()
```

## C#

```csharp {filename="ReadFile.cs"}
using System;
using System.IO;

class ReadFile
{
    public static void Main(string[] args)
    {
        var filePath = "./my-text-file.txt";

        foreach (var line in File.ReadLines(filePath))
        {
            Console.WriteLine($"line: {line}");
        }
    }
}
```

## Go

```go {filename="read_file.go"}
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	filePath := "./my-text-file.txt"

	file, _ := os.Open(filePath)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if line != "" {
			fmt.Println("line:", line)
		}
	}
}
```

## Swift

```swift {filename="read_file.swift"}
import Foundation

let filePath = "./my-text-file.txt"

let content = try String(contentsOfFile: filePath, encoding: .utf8)
let lines = content.components(separatedBy: .newlines)
for line in lines {
  if !line.isEmpty {
    print("line: \(line)")
  }
}
```

## Raku

```raku {filename="read_file.raku"}
use v6;

say "line: $_" for './my-text-file.txt'.IO.lines;
```

## Rust

```rust {filename="read_file.rs"}
use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() {
    let file = File::open("./my-text-file.txt").unwrap();

    for line in BufReader::new(file).lines() {
        println!("line: {}", line.unwrap());
    }
}
```

