+++
title = ''
draft = false
+++

# write_file

Test that a script, given a path to a named pipe, can write to that named pipe

## Python

`write_file.py`

```python
"""Script to write text to a new file.
Run script as `python write_file.py <output_file>.py "some text"`
"""
import sys
import os

outfile = sys.argv[1]
text = sys.argv[2]

with open(outfile, 'w') as f:
    f.write(text.upper())
```

## Ruby

`write_file.rb`

```ruby
# Script to write text to a new file
# Run script as `ruby write_file.rb <output_file>.txt 'some text'`

outfile, text = ARGV

File.write(outfile, text.upcase)
```

## Nodejs

`write_file.mjs`

```javascript
// Script to write text to a new file
import fs from 'fs/promises'

const [outfile, text] = process.argv.slice(2) // Get command-line arguments

await fs.writeFile(outfile, text.toUpperCase())
```

## Deno

`write_file.mjs`

```javascript
// Script to write text to a new file

const [filename, ...textParts] = Deno.args;
const text = textParts.join(' ');

await Deno.writeTextFile(filename, text.toUpperCase());
```

## Php

`write_file.php`

```php
<?php
// Write text to a new file

// Get command-line arguments
$outfile = $argv[1];
$text = $argv[2];

// Convert the text to uppercase
$uppercaseText = strtoupper($text);

// Write the uppercase text to the specified file
file_put_contents($outfile, $uppercaseText);
```

## R

`write_file.R`

```r
# 'Script to write text to a new file

# Get the command-line arguments
args <- commandArgs(trailingOnly = TRUE)
outfile <- args[1]
text <- args[2]

# Open the output file and write text in uppercase
writeLines(toupper(text), outfile, sep="")
```

## Perl

`write_file.pl`

```perl
# Script to write text to a new file
# Run script as `perl write_file.pl <output_file>.txt 'some text'`
use strict;
use warnings;

my ($outfile, $text) = @ARGV;

open my $fh, '>', $outfile or die "Cannot open $ARGV[0]: $!";

print $fh uc $text;
```

## Java

`WriteFile.java`

```java
//Script to write text to a new file
//Run script as `java write_file.java <output_file>.txt 'some text'`

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

public class WriteFile {
    public static void main(String[] args) throws IOException{
        if (args.length != 2) {
            System.err.println("Usage: java WriteFile.java <output_file>.txt 'some text'");
            System.exit(1);
        }

        String outFile = args[0];
        String text = args[1].toUpperCase();
        Files.write(Paths.get(outFile), text.getBytes(StandardCharsets.UTF_8));
    }
}
```

## Bash 3

`write_file.sh`

```bash
#!/bin/bash

# Script to write text to a new file
# Run script as `bash write_file.sh <output_file>.txt 'some text'`

outfile="$1"
text="$2"

if [ -z "$outfile" ] || [ -z "$text" ]; then
  echo "Usage: $0 <output_file> <text>"
  exit 1
fi

echo -n "$text" | tr -d '\n' | tr '[:lower:]' '[:upper:]' > "$outfile"
```

## Bash 5

`write_file.sh`

```bash
#!/bin/bash

# Script to write text to a new file
# Run script as `bash write_file.sh <output_file>.txt 'some text'`

outfile="$1"
text="$2"

if [ -z "$outfile" ] || [ -z "$text" ]; then
  echo "Usage: $0 <output_file> <text>"
  exit 1
fi

echo -n "${text^^}" > "$outfile"
```

## Lua

`write_file.lua`

```lua
-- Lua script to write text to a new file
-- Run script as `lua write_file.lua <output_file>.txt 'some text'`

local outfile = arg[1]
local text = arg[2]

local fh = io.open(outfile, "w")

fh:write(text:upper())

fh:close()
```

## C#

`WriteFile.cs`

```csharp
//Script to write text to a new file
//Run script as `csharp write_file.cs <output_file>.txt 'some text'`

using System;
using System.IO;

class WriteFile
{
    public static void Main(string[] args)
    {
        string outFile = args[0];
        string text = args[1].ToUpper();

        File.WriteAllText(outFile, text);
    }
}
```

## Go

`write_file.go`

```go
//Script to write text to a new file
//Run script as `go write_file.go <output_file>.txt 'some text'`

package main

import (
	"os"
	"strings"
)

func main() {

	outFile := os.Args[1]
	text := strings.ToUpper(os.Args[2])

	_ = os.WriteFile(outFile, []byte(text), 0644)

}
```

## Swift

`write_file.swift`

```swift
/*Script to write text to a new file.
Run script as `swift write_file.py <output_file>.swift "some text"`
*/

import Foundation

guard CommandLine.arguments.count == 3 else {
    print("Usage: swift script.swift <outfile> <text>")
    exit(1)
}

let outfile = CommandLine.arguments[1]
let text = CommandLine.arguments[2]

// atomically must be false when writing to named pipe
try text.uppercased().write(toFile: outfile, atomically: false, encoding: .utf8)
```

## Raku

`write_file.raku`

```raku
# Script to write text to a new file
# Run script as `perl write_file.pl <output_file>.txt 'some text'`
use v6;

my ($outfile, $text) = @*ARGS;

my $fh = open $outfile, :w;

$fh.print: $text.uc;
$fh.close;
```

## Rust

`write_file.rs`

```rust
//Script to write text to a new file
//Run script as `cargo write_file.rs <output_file>.txt 'some text'`

use std::env;
use std::fs::write;

fn main() {
    let args: Vec<String> = env::args().collect();

    let out_file = &args[1];
    let text = &args[2].to_uppercase();

    write(out_file, text).unwrap();
}
```

