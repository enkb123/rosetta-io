+++
title = ''
draft = false
+++

# streaming_pipe_in

Test that named pipe can be read line by line and can write to stdout

## Python

`streaming_pipe_in.py`

```python
import sys

pipe_in = sys.argv[1]

with open(pipe_in, 'r', encoding='utf-8') as input_pipe:
    for line in input_pipe:
        sys.stdout.write(line.upper())
        sys.stdout.flush()
```

## Ruby

`streaming_pipe_in.rb`

```ruby
# Script reads text from a named pipe and writes it to stdout, capitalized

STDOUT.sync = true

pipe_in = ARGV.fetch(0)

File.open(pipe_in, 'r') do |pipe|
  pipe.each_line do |line|
    puts line.upcase
  end
end
```

## Nodejs

`streaming_pipe_in.mjs`

```javascript
//Script reads text from a named pipe and writes it to stdout, capitalized

import * as fs from 'fs';
import * as readline from 'node:readline/promises';

const pipeIn = process.argv[2];

const input = fs.createReadStream(pipeIn);
const rl = readline.createInterface({ input })

for await (const line of rl) {
  console.log(line.toUpperCase())
}
```

## Deno

`streaming_pipe_in.mjs`

```javascript
//Script reads text from a named pipe and writes it to stdout, capitalized

import { readLines } from 'https://deno.land/std/io/mod.ts';

const [pipePath] = Deno.args;
const file = await Deno.open(pipePath, { read: true });

for await (const line of readLines(file)) {
  console.log(line.toUpperCase());
}

file.close();
```

## Php

`streaming_pipe_in.php`

```php
<?php
// Script reads text from a named pipe and writes it to stdout, capitalized
$pipe_in = $argv[1];

$input_pipe = fopen($pipe_in, 'r');

while (($line = fgets($input_pipe)) !== false) {
    echo strtoupper($line);
}

fclose($input_pipe);
?>
```

## R

`streaming_pipe_in.R`

```r
# Script reads text from a named pipe and writes it to stdout, capitalized
# Command-line arguments
args <- commandArgs(trailingOnly = TRUE)

# Named pipe path (input)
pipe_in <- args[1]

# Open named pipe for reading
input <- file(pipe_in, "r")

# Read each line from input pipe, convert to uppercase, and print to stdout
while (length(line <- readLines(input, n = 1)) > 0) {
  cat(paste(toupper(line), "\n", sep = ""))    # Print capitalized line to stdout
}

# Close input pipe
close(input)
```

## Perl

`streaming_pipe_in.pl`

```perl
# Script reads text from a named pipe and writes it to stdout, capitalized

use strict;
use warnings;

$| = 1;  # Turn off output buffering

my ($pipe_in) = @ARGV;

open my $input, '<', $pipe_in or die "Cannot open input pipe: $!";

while (my $line = <$input>) {
    print uc($line);
}

close $input;
```

## Java

`StreamingPipeIn.java`

```java
//Script reads text from a named pipe and writes it to stdout, capitalized

import java.io.*;

public class StreamingPipeIn {
    public static void main(String[] args) throws IOException {
        String pipe_in = args[0];

        BufferedReader input = new BufferedReader(new FileReader(pipe_in));

        String line;
        while ((line = input.readLine()) != null) {
            System.out.println(line.toUpperCase());
        }

        input.close();
    }
}
```

## Bash 3

`streaming_pipe_in.sh`

```bash
#!/bin/bash

# Script reads text from a named pipe and writes it to stdout, capitalized
pipe_in="$1"

tr '[:lower:]' '[:upper:]' < "$pipe_in"
```

## Bash 5

`streaming_pipe_in.sh`

```bash
#!/bin/bash

# Script reads text from a named pipe and writes it to stdout, capitalized
pipe_in="$1"

tr '[:lower:]' '[:upper:]' < "$pipe_in"
```

## Lua

`streaming_pipe_in.lua`

```lua
-- Script reads text from a named pipe and writes it to stdout, capitalized
local pipe_in = arg[1]

local input_file = assert(io.open(pipe_in, "r"), "Failed to open input pipe: " .. pipe_in)

for line in input_file:lines() do
    io.write(line:upper() .. "\n")
    io.flush()
end

input_file:close()
```

## C#

`StreamingPipeIn.cs`

```csharp
// Script reads text from a named pipe and writes it to stdout, capitalized

using System;
using System.IO;
using System.Text;

class StreamingPipeIn
{
    public static void Main(string[] args)
    {
        string pipe_in = args[0];

        using var reader = new StreamReader(args[0]);

        string line;
        while ((line = reader.ReadLine()) != null)
        {
            Console.WriteLine(line.ToUpper());
        }
    }
}
```

## Go

`streaming_pipe_in.go`

```go
//Script reads text from a named pipe and writes it to stdout, capitalized

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	pipeIn := os.Args[1]

	file, _ := os.Open(pipeIn)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println(strings.ToUpper(line))
	}
}
```

## Swift

`streaming_pipe_in.swift`

```swift
import Foundation

#if os(macOS) || os(iOS)
  import Darwin
#elseif os(Linux)
  import Glibc
#endif
setvbuf(stdout, nil, _IONBF, 0)

let arguments = CommandLine.arguments
let pipe_in = arguments[1]

public class FileLines: Sequence, IteratorProtocol {
  private let file: UnsafeMutablePointer<FILE>

  init?(path: String) {
    guard let file = fopen(path, "r") else { return nil }
    self.file = file
  }

  public func next() -> String? {
    var line: UnsafeMutablePointer<CChar>? = nil
    var linecap: Int = 0
    defer { free(line) }
    return getline(&line, &linecap, file) > 0 ? String(cString: line!) : nil
  }

  deinit {
    fclose(file)
  }

  public func makeIterator() -> FileLines {
    return self
  }
}

// in new versions of Swift, this can be replaced with `if let lines = FileHandle(forReadingAtPath: pipe_in).bytes.lines`
if let lines = FileLines(path: pipe_in) {
  for line in lines {
    print(line.uppercased(), terminator: "")
  }
} else {
  print("Error reading from pipe: Could not open file at path \(pipe_in)")
}
```

## Raku

`streaming_pipe_in.raku`

```raku
use v6;

my $pipe_in = @*ARGS[0];

my $input = open($pipe_in, :r);

for $input.lines() {
    say .uc;
    $*OUT.flush;
}

$input.close;
```

## Rust

`streaming_pipe_in.rs`

```rust
//Script reads text from a named pipe and writes it to stdout, capitalized

use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let pipe_in = env::args().nth(1).unwrap();

    let file = File::open(pipe_in).unwrap();
    let reader = BufReader::new(file);

    for line in reader.lines() {
        println!("{}", line.unwrap().to_uppercase());
    }
}
```

