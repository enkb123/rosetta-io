+++
title = ''
draft = false
+++

# write_file

Test that a script, given a path to a named pipe, can write to that named pipe

## Python

`write_file.py`

```python
import sys

outfile = sys.argv[1]
text = sys.argv[2]

with open(outfile, 'w') as f:
    f.write(text.upper())
```

## Ruby

`write_file.rb`

```ruby
outfile, text = ARGV

File.write(outfile, text.upcase)
```

## Nodejs

`write_file.mjs`

```javascript
import fs from 'fs/promises'

const [outfile, text] = process.argv.slice(2)

await fs.writeFile(outfile, text.toUpperCase())
```

## Deno

`write_file.mjs`

```javascript
const [filename, ...textParts] = Deno.args;
const text = textParts.join(' ');

await Deno.writeTextFile(filename, text.toUpperCase());
```

## Php

`write_file.php`

```php
<?php

$outfile = $argv[1];
$text = $argv[2];

$uppercaseText = strtoupper($text);

file_put_contents($outfile, $uppercaseText);
```

## R

`write_file.R`

```r
args <- commandArgs(trailingOnly = TRUE)
outfile <- args[1]
text <- args[2]

writeLines(toupper(text), outfile, sep="")
```

## Perl

`write_file.pl`

```perl
use strict;
use warnings;

my ($outfile, $text) = @ARGV;

open my $fh, '>', $outfile or die "Cannot open $ARGV[0]: $!";

print $fh uc $text;
```

## Java

`WriteFile.java`

```java
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
outfile="$1"
text="$2"

if [ -z "$outfile" ] || [ -z "$text" ]; then
  echo "Usage: $0 <output_file> <text>"
  exit 1
fi

tr '[:lower:]' '[:upper:]' <<<"$text" >"$outfile"
```

## Bash 5

`write_file.sh`

```bash
outfile="$1"
text="$2"

if [ -z "$outfile" ] || [ -z "$text" ]; then
  echo "Usage: $0 <output_file> <text>"
  exit 1
fi

echo "${text^^}" > "$outfile"
```

## Lua

`write_file.lua`

```lua
local outfile = arg[1]
local text = arg[2]

local fh = io.open(outfile, "w")

fh:write(text:upper())

fh:close()
```

## C#

`WriteFile.cs`

```csharp
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
import Foundation

guard CommandLine.arguments.count == 3 else {
    print("Usage: swift script.swift <outfile> <text>")
    exit(1)
}

let outfile = CommandLine.arguments[1]
let text = CommandLine.arguments[2]

try text.uppercased().write(toFile: outfile, atomically: false, encoding: .utf8)
```

## Raku

`write_file.raku`

```raku
use v6;

my ($outfile, $text) = @*ARGS;

my $fh = open $outfile, :w;

$fh.print: $text.uc;
$fh.close;
```

## Rust

`write_file.rs`

```rust
use std::env;
use std::fs::write;

fn main() {
    let args: Vec<String> = env::args().collect();

    let out_file = &args[1];
    let text = &args[2].to_uppercase();

    write(out_file, text).unwrap();
}
```

