+++
title = ''
draft = false
+++

# streaming_pipe_in

Read from named pipe line by line

## Python

```python {filename="streaming_pipe_in.py"}
import sys

pipe_in = "input.pipe"

with open(pipe_in, 'r', encoding='utf-8') as input_pipe:
    for line in input_pipe:
        sys.stdout.write(line.upper())
        sys.stdout.flush()
```

## Ruby

```ruby {filename="streaming_pipe_in.rb"}
STDOUT.sync = true

File.open 'input.pipe', 'r' do |pipe|
  pipe.each_line do |line|
    puts line.upcase
  end
end
```

## Nodejs

```javascript {filename="streaming_pipe_in.mjs"}
import * as fs from 'fs';
import * as readline from 'node:readline/promises';

const pipeIn = "input.pipe";

const input = fs.createReadStream(pipeIn);
const rl = readline.createInterface({ input })

for await (const line of rl) {
  console.log(line.toUpperCase())
}
```

## Deno

```javascript {filename="streaming_pipe_in.mjs"}
import { readLines } from 'https://deno.land/std/io/mod.ts';

const file = await Deno.open("input.pipe", { read: true });

for await (const line of readLines(file)) {
  console.log(line.toUpperCase());
}

file.close();
```

## Php

```php {filename="streaming_pipe_in.php"}
<?php

$pipe_in = "input.pipe";

$input_pipe = fopen($pipe_in, 'r');

while (($line = fgets($input_pipe)) !== false) {
    echo strtoupper($line);
}

fclose($input_pipe);
```

## R

```r {filename="streaming_pipe_in.R"}
pipe_in <- "input.pipe"

input <- file(pipe_in, "r")

while (length(line <- readLines(input, n = 1)) > 0) {
  cat(paste(toupper(line), "\n", sep = ""))
}

close(input)
```

## Perl

```perl {filename="streaming_pipe_in.pl"}
use strict;
use warnings;

$| = 1;

my ($pipe_in) = "input.pipe";

open my $input, '<', $pipe_in or die "Cannot open input pipe: $!";

while (my $line = <$input>) {
    print uc($line);
}

close $input;
```

## Java

```java {filename="StreamingPipeIn.java"}
import java.io.*;

public class StreamingPipeIn {
    public static void main(String[] args) throws IOException {
        String pipe_in = "input.pipe";

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

```bash {filename="streaming_pipe_in.sh"}
pipe_in="input.pipe"

tr '[:lower:]' '[:upper:]' < "$pipe_in"
```

## Bash 5

```bash {filename="streaming_pipe_in.sh"}
pipe_in="input.pipe"

tr '[:lower:]' '[:upper:]' < "$pipe_in"
```

## Lua

```lua {filename="streaming_pipe_in.lua"}
local pipe_in = "input.pipe"

local input_file = assert(io.open(pipe_in, "r"), "Failed to open input pipe: " .. pipe_in)

for line in input_file:lines() do
    io.write(line:upper() .. "\n")
    io.flush()
end

input_file:close()
```

## C#

```csharp {filename="StreamingPipeIn.cs"}
using System;
using System.IO;

class StreamingPipeIn
{
    public static void Main(string[] args)
    {
        string pipe_in = "input.pipe";
        using var reader = new StreamReader(pipe_in);

        string line;
        while ((line = reader.ReadLine()) != null)
        {
            Console.WriteLine(line.ToUpper());
        }
    }
}
```

## Go

```go {filename="streaming_pipe_in.go"}
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	pipeIn := "input.pipe"

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

```swift {filename="streaming_pipe_in.swift"}
import Foundation

#if os(macOS) || os(iOS)
  import Darwin
#elseif os(Linux)
  import Glibc
#endif
setvbuf(stdout, nil, _IONBF, 0)

let pipe_in = "input.pipe"

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

```raku {filename="streaming_pipe_in.raku"}
use v6;

my $pipe_in = "input.pipe";

my $input = open($pipe_in, :r);

for $input.lines() {
    say .uc;
    $*OUT.flush;
}

$input.close;
```

## Rust

```rust {filename="streaming_pipe_in.rs"}
use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let pipe_in = "input.pipe";

    let file = File::open(pipe_in).unwrap();
    let reader = BufReader::new(file);

    for line in reader.lines() {
        println!("{}", line.unwrap().to_uppercase());
    }
}
```

