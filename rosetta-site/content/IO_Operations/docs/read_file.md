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
import fs  from 'fs'
const path = './my-text-file.txt';

fs.readFile(path, 'utf8', (_, data) => {
    data.split('\n').forEach(line => {
    if (line.trim() !== '') {
      console.log(`line: ${line}`);
    }
  });
});
```

## Deno

`read_file.mjs`

```javascript
const filePath = "./my-text-file.txt";
const fileContent = await Deno.readTextFile(filePath);

for (const line of fileContent.split("\n")) {
  if (line.trim() !== "") {
    console.log(`line: ${line}`);
  }
}
```

## Php

`read_file.php`

```php
<?php

$filePath = './my-text-file.txt';
$file = fopen($filePath, 'r');

while (($line = fgets($file)) !== false) {
    $line = trim($line);
    echo "line: $line\n";
}

fclose($file);
```

## R

`read_file.R`

```r
file_path <- "./my-text-file.txt"

con <- file(file_path, "r")

while (length(line <- readLines(con, n = 1, warn = FALSE)) > 0) {
  cat("line:", line, "\n")
}

close(con)
```

## Perl

`read_file.pl`

```perl
use strict;
use warnings;

my $file_path = './my-text-file.txt';
open my $fh, '<', $file_path;

while (my $line = <$fh>) {
    chomp $line;
    print "line: $line\n";

}

close $fh;
```

## Java

`ReadFile.java`

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadFile {
    public static void main(String[] args) throws IOException{
        String filePath = "./my-text-file.txt";

        BufferedReader br = new BufferedReader(new FileReader(filePath));
        String line;
        while ((line = br.readLine()) != null) {
            if (!line.isEmpty()) {
                System.out.println("line: " + line);
            }

        }
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
        string filePath = "./my-text-file.txt";
        using (StreamReader reader = new StreamReader(filePath))
        {
            string line;
            while ((line = reader.ReadLine()) != null)
            {
                Console.WriteLine($"line: {line}");
            }
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
let fileURL = URL(fileURLWithPath: filePath)

let content = try String(contentsOf: fileURL, encoding: .utf8)
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
my $file = $file-path.IO;

if $file ~~ :e {
    for $file.lines {
        say "line: $_";

    }
}
```

## Rust

`read_file.rs`

```rust
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() -> io::Result<()> {
    let file_path = "./my-text-file.txt";
    let file = File::open(file_path)?;

    let reader = io::BufReader::new(file);

    for line in reader.lines() {
        let line = line?;
        println!("line: {}", line);
    }

    Ok(())
}
```

