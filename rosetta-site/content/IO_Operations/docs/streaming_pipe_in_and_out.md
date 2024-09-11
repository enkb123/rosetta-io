+++
title = ''
draft = false
+++

# streaming_pipe_in_and_out

Test that named pipe can be read line by line and can write to output pipe without waiting for all lines to arrive

## Python

`streaming_pipe_in_and_out.py`

```python
# Script reads text from a named pipe and writes it another named pipe, capitalized
import sys

pipe_in = sys.argv[1]
pipe_out = sys.argv[2]

with open(pipe_in, 'r', encoding='utf-8') as input_pipe:
    with open(pipe_out, 'w', encoding='utf-8') as output_pipe:
        for line in input_pipe:
            output_pipe.write(line.upper())
            output_pipe.flush()
```

## Ruby

`streaming_pipe_in_and_out.rb`

```ruby
# Script reads text from a named pipe and writes it another named pipe, capitalized

pipe_in, pipe_out = ARGV

File.open(pipe_out, 'w') do |output|
  output.sync = true

  File.open(pipe_in, 'r') do |input|
    input.each_line do |line|
      output.puts line.upcase
    end
  end
end
```

## Nodejs

`streaming_pipe_in_and_out.mjs`

```javascript
// Script reads text from a named pipe and writes it another named pipe, capitalized

import * as fs from 'fs';
import * as readline from 'node:readline/promises';

const pipeIn = process.argv[2];
const pipeOut = process.argv[3];

const input = fs.createReadStream(pipeIn);
const rl = readline.createInterface({ input })

const output = fs.createWriteStream(pipeOut);

for await(const line of rl){
  output.write(line.toUpperCase() + '\n');
}
```

## Deno

`streaming_pipe_in_and_out.mjs`

```javascript
//Script reads text from a named pipe and writes it another named pipe, capitalized

import { readLines } from 'https://deno.land/std/io/mod.ts';

const [pipeInPath, pipeOutPath] = Deno.args;

const input = await Deno.open(pipeInPath, { read: true });
const output = await Deno.open(pipeOutPath, { write: true });

const rl = readLines(input);

for await (const line of readLines(input)) {
  await output.write(new TextEncoder().encode(line.toUpperCase() + '\n'));
}

input.close();
output.close();
```

## Php

`streaming_pipe_in_and_out.php`

```php
<?php
//Script reads text from a named pipe and writes it another named pipe, capitalized
$pipe_in = $argv[1];
$pipe_out = $argv[2];

$input_pipe = fopen($pipe_in, 'r');
$output_pipe = fopen($pipe_out, 'w');

while (($line = fgets($input_pipe)) !== false) {
    fwrite($output_pipe, strtoupper($line));
    fflush($output_pipe);
}

fclose($input_pipe);
fclose($output_pipe);
```

## R

`streaming_pipe_in_and_out.R`

```r
# Script reads text from a named pipe and writes it another named pipe, capitalized
args <- commandArgs(trailingOnly = TRUE)

pipe_in <- args[1]
pipe_out <- args[2]


input <- file(pipe_in, "r")

output <- file(pipe_out, "w")

while (length(line <- readLines(input, n = 1)) > 0) {
  writeLines(toupper(line), output)
  flush(output)
}

close(input)
close(output)
```

## Perl

`streaming_pipe_in_and_out.pl`

```perl
# Script reads text from a named pipe and writes it another named pipe, capitalized
use strict;
use warnings;

my ($pipe_in, $pipe_out) = @ARGV;

open my $output, '>', $pipe_out or die "Cannot open output pipe: $!";
open my $input, '<', $pipe_in or die "Cannot open input pipe: $!";

$output->autoflush(1);

while (my $line = <$input>) {
    print $output uc($line);
}

close $input;
close $output;
```

## Java

`StreamingPipeInAndOut.java`

```java
// Script reads text from a named pipe and writes it another named pipe, capitalized
import java.io.*;

public class StreamingPipeInAndOut {
    public static void main (String[] args) throws IOException{
        String pipe_in = args[0];
        String pipe_out = args[1];

        BufferedReader input = new BufferedReader(new FileReader(pipe_in));
        BufferedWriter output = new BufferedWriter(new FileWriter(pipe_out));

        String line;
        while ((line = input.readLine()) != null) {
            output.write(line.toUpperCase());
            output.newLine();  // Ensure newline after each line
            output.flush();  // Flush to ensure immediate write
        }

        input.close();
        output.close();
    }
}
```

## Bash 3

`streaming_pipe_in_and_out.sh`

```bash
#!/bin/bash
# Script reads text from a named pipe and writes it another named pipe, capitalized

pipe_in="$1"
pipe_out="$2"

tr '[:lower:]' '[:upper:]' < "$pipe_in" > "$pipe_out"
```

## Bash 5

`streaming_pipe_in_and_out.sh`

```bash
#!/bin/bash
# Script reads text from a named pipe and writes it another named pipe, capitalized

pipe_in="$1"
pipe_out="$2"

tr '[:lower:]' '[:upper:]' < "$pipe_in" > "$pipe_out"
```

## Lua

`streaming_pipe_in_and_out.lua`

```lua
-- Script reads text from a named pipe and writes it another named pipe, capitalized
local pipe_in = arg[1]
local pipe_out = arg[2]

local input_file = io.open(pipe_in, "r")

local output_file = io.open(pipe_out, "w")

for line in input_file:lines() do
    output_file:write(line:upper(), "\n")
    output_file:flush()
end

input_file:close()
output_file:close()
```

## C#

`StreamingPipeInAndOut.cs`

```csharp
//Script reads text from a named pipe and writes it another named pipe, capitalized
using System;
using System.IO;
using System.IO.Pipes;

class StreamingPipeInAndOut
{
    public static void Main(string[] args)
    {
        string pipe_in = args[0];
        string pipe_out = args[1];

        using var input = new StreamReader(pipe_in);
        using var output = new StreamWriter(pipe_out) { AutoFlush = true };

        string line;
        while ((line = input.ReadLine()) != null)
        {
            output.WriteLine(line.ToUpper());
        }
    }
}
```

## Go

`streaming_pipe_in_and_out.go`

```go
// Script reads text from a named pipe and writes it to another pipe, capitalized
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	pipeIn := os.Args[1]
	pipeOut := os.Args[2]

	fileIn, _ := os.OpenFile(pipeIn, os.O_RDONLY, 0666)
	defer fileIn.Close()

	fileOut, _ := os.OpenFile(pipeOut, os.O_WRONLY, 0666)
	defer fileOut.Close()

	scanner := bufio.NewScanner(fileIn)
	for scanner.Scan() {
		if _, err := fileOut.WriteString(strings.ToUpper(scanner.Text()) + "\n"); err != nil {
			fmt.Println("Error writing to output pipe:", err)
			os.Exit(1)
		}
	}

}
```

## Swift

`streaming_pipe_in_and_out.swift`

```swift
//Script reads text from a named pipe and writes it another named pipe, capitalized

import Foundation

#if os(macOS) || os(iOS)
  import Darwin
#elseif os(Linux)
  import Glibc
#endif
setvbuf(stdout, nil, _IONBF, 0)

let arguments = CommandLine.arguments
let pipe_in = arguments[1]

let pipe_out = arguments[2]
let fileDescriptor = open(pipe_out, O_WRONLY)

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
    write(fileDescriptor, line.uppercased(), line.uppercased().utf8.count)
  }
} else {
  print("Error reading from pipe: Could not open file at path \(pipe_in)")
}
```

## Raku

`streaming_pipe_in_and_out.raku`

```raku
# Script reads text from a named pipe and writes it another named pipe, capitalized
use v6;

my ($pipe_in, $pipe_out) = @*ARGS;

my $output = open($pipe_out, :w);
my $input = open($pipe_in, :r);

for $input.lines {
    $output.print(.uc ~ "\n");
}
```

## Rust

`streaming_pipe_in_and_out.rs`

```rust
// Script reads text from a named pipe and writes it another named pipe, capitalized
use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader, BufWriter, Write};

fn main() {
    let args: Vec<String> = env::args().collect();

    let pipe_in = &args[1];
    let pipe_out = &args[2];

    let reader = BufReader::new(File::open(pipe_in).unwrap());
    let mut writer = BufWriter::new(File::create(pipe_out).unwrap());

    for line in reader.lines() {
        writeln!(writer, "{}", line.unwrap().to_uppercase()).unwrap();
        writer.flush().unwrap();
    }
}
```

