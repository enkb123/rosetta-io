+++
title = ''
draft = false
+++

# streaming_pipe_in_and_out

Read line by line from a named pipe and write to another named pipe

## Python

```python {filename="streaming_pipe_in_and_out.py"}
input_file = 'streaming-in.pipe'
output_file = 'streaming-out.pipe'

with open(input_file, 'r', encoding='utf-8') as input_pipe:
    with open(output_file, 'w', encoding='utf-8') as output_pipe:
        for line in input_pipe:
            output_pipe.write(f"received {line.strip()}\n")
            output_pipe.flush()
```

## Ruby

```ruby {filename="streaming_pipe_in_and_out.rb"}
File.open 'streaming-out.pipe', 'w' do |output|
  output.sync = true

  File.foreach "streaming-in.pipe" do |line|
    output.puts "received #{line}"
  end
end
```

## Nodejs

```javascript {filename="streaming_pipe_in_and_out.mjs"}
import * as fs from 'fs';
import * as readline from 'node:readline/promises';

const inputStream = fs.createReadStream('streaming-in.pipe');
const outputStream = fs.createWriteStream('streaming-out.pipe');

const rl = readline.createInterface({ input: inputStream });

for await (const line of rl) {
  outputStream.write(`received ${line}\n`);
}

outputStream.end();
```

## Deno

```javascript {filename="streaming_pipe_in_and_out.mjs"}
import { readLines } from 'https://deno.land/std/io/mod.ts';

const output = await Deno.open('streaming-out.pipe', { write: true });
const input = await Deno.open('streaming-in.pipe', { read: true });

const textEncoder = new TextEncoder();

for await (const line of readLines(input)) {
  await output.write(textEncoder.encode(`received ${line}\n`));
}

input.close();
output.close();
```

## Php

```php {filename="streaming_pipe_in_and_out.php"}
<?php

$output_pipe = fopen('streaming-out.pipe', 'w');
$input_pipe = fopen('streaming-in.pipe', 'r');

while (($line = fgets($input_pipe)) !== false) {
    fwrite($output_pipe, "received " . $line);
}

fclose($input_pipe);
fclose($output_pipe);
```

## R

```r {filename="streaming_pipe_in_and_out.R"}
input <- file("streaming-in.pipe", "r")
output <- file("streaming-out.pipe", "w")

while (length(line <- readLines(input, n = 1)) > 0) {
  writeLines(paste("received", line), con = output)
  flush(output)
}

close(input)
close(output)
```

## Perl

```perl {filename="streaming_pipe_in_and_out.pl"}
use strict;
use warnings;

open my $output, '>', 'streaming-out.pipe';
open my $input, '<', 'streaming-in.pipe';

$output->autoflush(1);

print $output "received $_" while <$input>;

close $input;
close $output;
```

## Java

```java {filename="StreamingPipeInAndOut.java"}
import java.io.*;

public class StreamingPipeInAndOut {
    public static void main (String[] args) throws IOException{
        var inputPath = "streaming-in.pipe";
        var outputPath = "streaming-out.pipe";

        var input = new BufferedReader(new FileReader(inputPath));
        var output = new BufferedWriter(new FileWriter(outputPath));

        String line;
        while ((line = input.readLine()) != null) {
            output.write("received " + line);
            output.newLine();
            output.flush();
        }

        input.close();
        output.close();
    }
}
```

## Bash 3

```bash {filename="streaming_pipe_in_and_out.sh"}
while IFS= read -r line; do
    echo "received $line"
done < streaming-in.pipe > streaming-out.pipe
```

## Bash 5

```bash {filename="streaming_pipe_in_and_out.sh"}
while IFS= read -r line; do
    echo "received $line"
done < streaming-in.pipe > streaming-out.pipe
```

## Lua

```lua {filename="streaming_pipe_in_and_out.lua"}
local output = io.open("streaming-out.pipe", "w")
local input = io.open("streaming-in.pipe", "r")

for line in input:lines() do
    output:write("received " .. line .. "\n")
    output:flush()
end

input:close()
output:close()
```

## C#

```csharp {filename="StreamingPipeInAndOut.cs"}
using System;
using System.IO;

class StreamingPipeInAndOut
{
    public static void Main(string[] args)
    {
        using var input = new StreamReader("streaming-in.pipe");
        using var output = new StreamWriter("streaming-out.pipe") { AutoFlush = true };

        string line;
        while ((line = input.ReadLine()) != null)
        {
            output.WriteLine($"received {line}");
        }
    }
}
```

## Go

```go {filename="streaming_pipe_in_and_out.go"}
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	input, _ := os.Open("streaming-in.pipe")
	defer input.Close()

	output, _ := os.OpenFile("streaming-out.pipe", os.O_WRONLY, 0)
	defer output.Close()

	output.Sync()

	scanner := bufio.NewScanner(input)

	for scanner.Scan() {
		line := scanner.Text()
		fmt.Fprintf(output, "received %s\n", line)

	}
}
```

## Swift

```swift {filename="streaming_pipe_in_and_out.swift"}
import Foundation

#if os(macOS) || os(iOS)
  import Darwin
#elseif os(Linux)
  import Glibc
#endif
setvbuf(stdout, nil, _IONBF, 0)

let pipe_in = "streaming-in.pipe"
let pipe_out = "streaming-out.pipe"

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

if let lines = FileLines(path: pipe_in) {
  for line in lines {
    let outputLine = "received \(line)"
    write(fileDescriptor, outputLine, outputLine.utf8.count)
  }
}
```

## Raku

```raku {filename="streaming_pipe_in_and_out.raku"}
use v6;

my $output = open 'streaming-out.pipe', :w;
my $input = open 'streaming-in.pipe', :r;

$output.say("received $_") for $input.lines;

$output.close;
$input.close;
```

## Rust

```rust {filename="streaming_pipe_in_and_out.rs"}
use std::fs::File;
use std::io::{self, BufRead, BufReader, Write};

fn main() {
    let mut output = File::create("streaming-out.pipe").unwrap();
    let input = File::open("streaming-in.pipe").unwrap();

    for line in BufReader::new(input).lines() {
        writeln!(output, "received {}", line.unwrap()).unwrap();
    }
}
```

