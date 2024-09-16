+++
title = ''
draft = false
+++

# read_file

Check that a file is read line by line, when file path is given
as command line argument


## Python

`read_file.py`

```python
import sys

file_path = sys.argv[1]

with open(file_path, 'r') as f:
    i = 1
    for line in f.readlines():
        print(i, line.upper(), end='')
        i += 1
```

## Ruby

`read_file.rb`

```ruby
file_path = ARGV[0]

begin
  File.open(file_path, 'r') do |f|
    f.each_line.with_index do |line, i|
      puts "#{i+1} #{line.upcase}"
    end
  end
rescue Errno::ENOENT
  puts "File not found: #{file_path}"
  exit(1)
end
```

## Nodejs

`read_file.mjs`

```javascript
import * as readline from 'node:readline/promises'
import fs  from 'fs'

const file_path = process.argv[2]

const rl = readline.createInterface({
  input: fs.createReadStream(file_path),
})

let i = 1
for await (const line of rl) {
  console.log(i + " " + line.toUpperCase())
  i++
}
```

## Deno

`read_file.mjs`

```javascript
const filePath = Deno.args[0];
const file = await Deno.open(filePath);
const decoder = new TextDecoder();

let i = 1;
let partialLine = '';

for await (const chunk of Deno.iter(file)) {
    const chunkStr = decoder.decode(chunk, { stream: true });
    const lines = (partialLine + chunkStr).split('\n');

    for (const line of lines.slice(0, -1)) {
        console.log(`${i++} ${line.toUpperCase()}`);
    }

    partialLine = lines[lines.length - 1];
}

if (partialLine) {
    console.log(`${i} ${partialLine.toUpperCase()}`);
}

file.close();
```

## Php

`read_file.php`

```php
<?php

$file_path = $argv[1];

$file = fopen($file_path, 'r');

foreach (file($file_path) as $index => $line) {
    echo ($index + 1) . ' ' . strtoupper($line);
}
```

## R

`read_file.R`

```r
file_path <- commandArgs(trailingOnly = TRUE)[1]

con <- file(file_path, "r")

i <- 1
while (length(line <- readLines(con, n = 1)) > 0) {
  cat(i, toupper(line), sep = " ", fill = TRUE)
  i <- i + 1
}

close(con)
```

## Perl

`read_file.pl`

```perl
use strict;
use warnings;

my $file_path = shift;

open my $fh, '<', $file_path or die "Cannot open file: $file_path\n";

my $i = 1;
print $i++ . " " . uc while <$fh>;
```

## Java

`ReadFile.java`

```java
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.concurrent.atomic.AtomicInteger;

class ReadFile{
    public static void main(String[] args) throws IOException {
        var filePath = Paths.get(args[0]);
        var lineNumber = new AtomicInteger(1);

        Files.lines(filePath)
                .map(String::toUpperCase)
                .map(line -> lineNumber.getAndIncrement() + " " + line)
                .forEach(System.out::println);
    }
}
```

## Bash 3

`read_file.sh`

```bash
file_path="$1"

if [ ! -f "$file_path" ]; then
  echo "File not found: $file_path"
  exit 1
fi

i=1

while IFS= read -r line; do
  echo "$((i++)) $(tr '[:lower:]' '[:upper:]' <<< "$line")"
done < "$file_path"
```

## Bash 5

`read_file.sh`

```bash
#!/bin/bash

file_path="$1"

if [ ! -f "$file_path" ]; then
  echo "File not found: $file_path"
  exit 1
fi

i=1

while IFS= read -r line; do
  echo "$((i++)) ${line^^}"
done < "$1"
```

## Lua

`read_file.lua`

```lua
local file_path = arg[1]
local fh = io.open(file_path, "r")
local i = 1

for line in fh:lines() do
    print(i .. " " .. line:upper())
    i = i + 1
end
```

## C#

`ReadFile.cs`

```csharp
using System;
using System.IO;
using System.Linq;

class ReadFile
{
    public static void Main (string[] args)
    {
        string filePath = args[0];
        var lines = File.ReadAllLines(filePath);
        lines.Select((line, index) => $"{index + 1} {line.ToUpper()}")
                .ToList()
                .ForEach(Console.WriteLine);
    }
}
```

## Go

`read_file.go`

```go
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	content, _ := os.ReadFile(os.Args[1])

	lines := strings.Split(string(content), "\n")
	lineNumber := 1

	for _, line := range lines {
		if line == "" {
			continue
		}
		fmt.Printf("%d %s\n", lineNumber, strings.ToUpper(line))
		lineNumber++
	}
}
```

## Swift

`read_file.swift`

```swift
import Foundation

guard CommandLine.arguments.count > 1 else {
    print("Usage: swift script.swift <file_path>")
    exit(1)
}

let fileContents = try String(contentsOfFile: CommandLine.arguments[1])
var i = 1
fileContents.enumerateLines { line, _ in
    print("\(i) \(line.uppercased())")
    i += 1
}
```

## Raku

`read_file.raku`

```raku
use v6;

my $file-path = @*ARGS.shift;
my $fh = open $file-path, :r;

my $i = 1;
for $fh.lines {
    say $i++ ~ " " ~ .uc;
}

$fh.close;
```

## Rust

`read_file.rs`

```rust
use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let file_path = env::args().nth(1).unwrap();

    let file = File::open(file_path).unwrap();
    let reader = BufReader::new(file);

    for (line_number, line_result) in reader.lines().enumerate() {
        let line = line_result.unwrap();
        println!("{} {}", line_number + 1, line.to_uppercase());
    }
}
```

