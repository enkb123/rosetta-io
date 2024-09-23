+++
title = ''
draft = false
+++

# read_file

Read a file line by line

## Python

`read_file.py`

```python
file_path = './my-text-file.txt'

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        print(f"line: {line}")
```

## Ruby

`read_file.rb`

```ruby
File.open("./my-text-file.txt", "r") do |f|
  f.each_line do |line|
    puts "line: #{line}"
  end
end
```

## Nodejs

`read_file.mjs`

```javascript
import { promises as fs } from 'fs';

const filePath = './my-text-file.txt'

const fileContent = await fs.readFile(filePath, 'utf8')

for (const line of fileContent.split("\n")) {
  if (line !== "") {
    console.log('line:', line);
  }
}
```

## Deno

`read_file.mjs`

```javascript
const filePath = "./my-text-file.txt";
const fileContent = await Deno.readTextFile(filePath);

for (const line of fileContent.split("\n")) {
  if (line !== "") {
    console.log('line:', line);
  }
}
```

## Php

`read_file.php`

```php
<?php

$file_path = './my-text-file.txt';
$file = fopen($file_path, 'r');

foreach (file($file_path) as $index => $line) {
    echo "line: $line";
}
```

## R

`read_file.R`

```r
file_path <- "./my-text-file.txt"

lines <- readLines(file_path)

for (line in lines) {
  cat("line:", line, "\n")
}
```

## Perl

`read_file.pl`

```perl
use strict;
use warnings;

my $file_path = './my-text-file.txt';
open my $fh, '<', $file_path;

print "line: $_" while <$fh>;
```

## Java

`ReadFile.java`

```java
import java.nio.file.Files;
import java.nio.file.Paths;

public class ReadFile {
    public static void main(String[] args) throws Exception {
        var filePath = Paths.get("./my-text-file.txt");

        Files.lines(filePath)
            .filter(line -> !line.isEmpty())
            .forEach(line -> System.out.println("line: " + line));
    }
}
```

## Bash 3

`read_file.sh`

```bash
file_path="./my-text-file.txt"

while IFS= read -r line; do
  echo "line: $line"

done < "$file_path"
```

## Bash 5

`read_file.sh`

```bash
file_path="./my-text-file.txt"

while IFS= read -r line; do
  echo "line: $line"

done < "$file_path"
```

## Lua

`read_file.lua`

```lua
local filePath = "./my-text-file.txt"

local file = io.open(filePath, "r")

for line in file:lines() do
    print("line: " .. line)
end
file:close()
```

## C#

`ReadFile.cs`

```csharp
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

`read_file.go`

```go
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

`read_file.swift`

```swift
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

`read_file.raku`

```raku
use v6;

my $file-path = './my-text-file.txt';

for $file-path.IO.lines {
    say "line: $_";
}
```

## Rust

`read_file.rs`

```rust
use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() {
    let file_path = "./my-text-file.txt";
    let file = File::open(file_path).unwrap();

    let reader = BufReader::new(file);

    for line in reader.lines() {
        println!("line: {}", line.unwrap());
    }
}
```

