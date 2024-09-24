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

File.foreach 'input.pipe' do |line|
  puts line.upcase
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

$input_pipe = fopen("input.pipe", 'r');

while (($line = fgets($input_pipe)) !== false) {
    echo strtoupper($line);
}

fclose($input_pipe);
```

## R

```r {filename="streaming_pipe_in.R"}
input <- file("input.pipe", "r")

while (length(line <- readLines(input, n = 1)) > 0) {
  cat(toupper(line), "\n")
}

close(input)
```

## Perl

```perl {filename="streaming_pipe_in.pl"}
use strict;
use warnings;

$| = 1;
open my $input, '<', "input.pipe";

print uc($_) while <$input>;

close $input;
```

## Java

```java {filename="StreamingPipeIn.java"}
import java.io.*;

public class StreamingPipeIn {
    public static void main(String[] args) throws Exception {
        var pipe_in = "input.pipe";

        var input = new BufferedReader(new FileReader(pipe_in));

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
tr '[:lower:]' '[:upper:]' < input.pipe
```

## Bash 5

```bash {filename="streaming_pipe_in.sh"}
tr '[:lower:]' '[:upper:]' < input.pipe
```

## Lua

```lua {filename="streaming_pipe_in.lua"}
local input_file = io.open("input.pipe", "r")

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
        using var reader = new StreamReader("input.pipe");

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
}
```

## Raku

```raku {filename="streaming_pipe_in.raku"}
use v6;

my $input = open "input.pipe", :r;

for $input.lines {
    say .uc;
    $*OUT.flush;
}

$input.close;
```

## Rust

```rust {filename="streaming_pipe_in.rs"}
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let file = File::open("input.pipe").unwrap();

    for line in BufReader::new(file).lines() {
        println!("{}", line.unwrap().to_uppercase());
    }
}
```

