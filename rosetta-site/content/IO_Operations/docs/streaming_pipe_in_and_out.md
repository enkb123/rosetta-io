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

  File.open 'streaming-in.pipe', 'r' do |input|
    input.each_line do |line|
      output.puts "received #{line}"
    end
  end
end
```

## Nodejs

```javascript {filename="streaming_pipe_in_and_out.mjs"}
import * as fs from 'fs';
import * as readline from 'node:readline/promises';


const inputStream = fs.createReadStream('streaming-in.pipe');
const outputStream = fs.createWriteStream('streaming-out.pipe', { flags: 'a' });

const rl = readline.createInterface({
  input: inputStream,
});

for await (const line of rl) {
  outputStream.write(`received ${line}\n`);
}

outputStream.end();
```

## Deno

```javascript {filename="streaming_pipe_in_and_out.mjs"}
import { readLines } from 'https://deno.land/std/io/mod.ts';

const output = await Deno.open('streaming-out.pipe', { write: true, create: true });

const input = await Deno.open('streaming-in.pipe', { read: true });

for await (const line of readLines(input)) {
  await output.write(new TextEncoder().encode(`received ${line}\n`));
}

input.close();

output.close();
```

## Php

```php {filename="streaming_pipe_in_and_out.php"}
<?php

$inputFile = 'streaming-in.pipe';
$outputFile = 'streaming-out.pipe';

$output_pipe = fopen($outputFile, 'w');
$input_pipe = fopen($inputFile, 'r');

while (($line = fgets($input_pipe)) !== false) {
    fwrite($output_pipe, "received " . $line);
}

fclose($input_pipe);
fclose($output_pipe);
```

## R

```r {filename="streaming_pipe_in_and_out.R"}
input_file <- "streaming-in.pipe"
output_file <- "streaming-out.pipe"


input <- file(input_file, "r")

output <- file(output_file, "w")

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

my $input_file = 'streaming-in.pipe';
my $output_file = 'streaming-out.pipe';


open my $output, '>', $output_file or die "Cannot open output pipe: $!";
open my $input, '<', $input_file or die "Cannot open input pipe: $!";

$output->autoflush(1);

while (my $line = <$input>) {
    print $output "received $line";
}

close $input;
close $output;
```

## Java

```java {filename="StreamingPipeInAndOut.java"}
import java.io.*;

public class StreamingPipeInAndOut {
    public static void main (String[] args) throws IOException{
        String inputPath = "streaming-in.pipe";
        String outputPath = "streaming-out.pipe";

        BufferedReader input = new BufferedReader(new FileReader(inputPath));
        BufferedWriter output = new BufferedWriter(new FileWriter(outputPath));

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
input_file="streaming-in.pipe"
output_file="streaming-out.pipe"

exec 3> "$output_file"

while IFS= read -r line; do
    echo "received $line" >&3
done < "$input_file"

exec 3>&-
```

## Bash 5

```bash {filename="streaming_pipe_in_and_out.sh"}
input_file="streaming-in.pipe"
output_file="streaming-out.pipe"

exec 3> "$output_file"

while IFS= read -r line; do
    echo "received $line" >&3
done < "$input_file"

exec 3>&-
```

## Lua

```lua {filename="streaming_pipe_in_and_out.lua"}
local input_file = "streaming-in.pipe"
local output_file = "streaming-out.pipe"

local output = io.open(output_file, "w")

local input = io.open(input_file, "r")

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
        using (FileStream outputStream = new FileStream("streaming-out.pipe", FileMode.Create, FileAccess.Write))
        using (StreamWriter output = new StreamWriter(outputStream) { AutoFlush = true })
        {
            using (FileStream inputStream = new FileStream("streaming-in.pipe", FileMode.Open, FileAccess.Read))
            using (StreamReader input = new StreamReader(inputStream))
            {
                string line;
                while ((line = input.ReadLine()) != null)
                {
                    output.WriteLine($"received {line}");
                }
            }
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
	output, _ := os.OpenFile("streaming-out.pipe", os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0644)
	defer output.Close()

	output.Sync()

	input, _ := os.Open("streaming-in.pipe")
	defer input.Close()

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

my $input-file = 'streaming-in.pipe';
my $output-file = 'streaming-out.pipe';

my $output = open $output-file, :w;

my $input = open $input-file, :r;

for $input.lines -> $line {
    $output.say("received $line");
}

$output.close;
$input.close;
```

## Rust

```rust {filename="streaming_pipe_in_and_out.rs"}
use std::fs::File;
use std::io::{self, BufRead, Write};
use std::path::Path;

fn main() -> io::Result<()> {
    let input_path = "streaming-in.pipe";
    let output_path = "streaming-out.pipe";

    let mut output = File::create(output_path)?;

    let input = File::open(input_path)?;
    let reader = io::BufReader::new(input);

    for line in reader.lines() {
        let line = line?;
        writeln!(output, "received {}", line)?;
    }

    Ok(())
}
```

