+++
title = ''
draft = false
+++

# write_to_text_file

Write to a text file

## Python

```python {filename="write_to_text_file.py"}
import sys

outfile = "output.txt"
text = "Hello World!"

with open(outfile, 'w') as f:
    f.write(text)
```

## Ruby

```ruby {filename="write_to_text_file.rb"}
File.write "output.txt", "Hello World!"
```

## Nodejs

```javascript {filename="write_to_text_file.mjs"}
import fs from 'fs/promises'

const [outfile, text] = ["output.txt", "Hello World!"]

await fs.writeFile(outfile, text)
```

## Deno

```javascript {filename="write_to_text_file.mjs"}
const filename = "output.txt";
const text = "Hello World!";

await Deno.writeTextFile(filename, text);
```

## Php

```php {filename="write_to_text_file.php"}
<?php

$outfile = "output.txt";
$text = "Hello World!";

file_put_contents($outfile, $text);
```

## R

```r {filename="write_to_text_file.R"}
args <- commandArgs(trailingOnly = TRUE)
outfile <- "output.txt"
text <- "Hello World!"

writeLines(text, outfile, sep="")
```

## Perl

```perl {filename="write_to_text_file.pl"}
use strict;
use warnings;

my ($outfile, $text) = ("output.txt", "Hello World!");

open my $fh, '>', $outfile or die "Cannot open!";

print $fh $text;
```

## Java

```java {filename="WriteToTextFile.java"}
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

public class WriteToTextFile {
    public static void main(String[] args) throws IOException{
        String outFile = "output.txt";
        String text = "Hello World!";
        Files.write(Paths.get(outFile), text.getBytes(StandardCharsets.UTF_8));
    }
}
```

## Bash 3

```bash {filename="write_to_text_file.sh"}
echo "Hello World!" > output.txt
```

## Bash 5

```bash {filename="write_to_text_file.sh"}
echo "Hello World!" > output.txt
```

## Lua

```lua {filename="write_to_text_file.lua"}
local filename = "output.txt"
local text = "Hello World!"

local file = io.open(filename, "w")

if file then
    file:write(text)
    file:close()
end
```

## C#

```csharp {filename="WriteToTextFile.cs"}
using System;
using System.IO;

class WriteToTextFile
{
    public static void Main(string[] args)
    {
        string outFile = "output.txt";
        string text = "Hello World!";

        File.WriteAllText(outFile, text);
    }
}
```

## Go

```go {filename="write_to_text_file.go"}
package main

import (
	"os"
)

func main() {

	outFile := "output.txt"
	text := "Hello World!"

	_ = os.WriteFile(outFile, []byte(text), 0644)

}
```

## Swift

```swift {filename="write_to_text_file.swift"}
import Foundation

let outfile = "output.txt"
let text = "Hello World!"

try text.write(toFile: outfile, atomically: false, encoding: .utf8)
```

## Raku

```raku {filename="write_to_text_file.raku"}
use v6;

my ($outfile, $text) = ("output.txt", "Hello World!");

my $fh = open $outfile, :w;

$fh.print: $text;
$fh.close;
```

## Rust

```rust {filename="write_to_text_file.rs"}
use std::env;
use std::fs::write;

fn main() {
   let out_file = "output.txt";
    let text = "Hello World!";

    write(out_file, text).unwrap();
}
```

