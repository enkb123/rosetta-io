+++
title = ''
draft = false
+++

# write_to_text_file

Write to a text file

## Python

`write_to_text_file.py`

```python
import sys

outfile = "output.txt"
text = "Hello World!"

with open(outfile, 'w') as f:
    f.write(text)
```

## Ruby

`write_to_text_file.rb`

```ruby
File.write "output.txt", "Hello World!"
```

## Nodejs

`write_to_text_file.mjs`

```javascript
import fs from 'fs/promises'

const [outfile, text] = ["output.txt", "Hello World!"]

await fs.writeFile(outfile, text)
```

## Deno

`write_to_text_file.mjs`

```javascript
const filename = "output.txt";
const text = "Hello World!";

await Deno.writeTextFile(filename, text);
```

## Php

`write_to_text_file.php`

```php
<?php

$outfile = "output.txt";
$text = "Hello World!";

file_put_contents($outfile, $text);
```

## R

`write_to_text_file.R`

```r
args <- commandArgs(trailingOnly = TRUE)
outfile <- "output.txt"
text <- "Hello World!"

writeLines(text, outfile, sep="")
```

## Perl

`write_to_text_file.pl`

```perl
use strict;
use warnings;

my ($outfile, $text) = ("output.txt", "Hello World!");

open my $fh, '>', $outfile or die "Cannot open!";

print $fh $text;
```

## Java

`WriteToTextFile.java`

```java
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

`write_to_text_file.sh`

```bash
echo "Hello World!" > output.txt
```

## Bash 5

`write_to_text_file.sh`

```bash
echo "Hello World!" > output.txt
```

## Lua

`write_to_text_file.lua`

```lua
local filename = "output.txt"
local text = "Hello World!"

local file = io.open(filename, "w")

if file then
    file:write(text)
    file:close()
end
```

## C#

`WriteToTextFile.cs`

```csharp
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

`write_to_text_file.go`

```go
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

`write_to_text_file.swift`

```swift
import Foundation

let outfile = "output.txt"
let text = "Hello World!"

try text.write(toFile: outfile, atomically: false, encoding: .utf8)
```

## Raku

`write_to_text_file.raku`

```raku
use v6;

my ($outfile, $text) = ("output.txt", "Hello World!");

my $fh = open $outfile, :w;

$fh.print: $text;
$fh.close;
```

## Rust

`write_to_text_file.rs`

```rust
use std::env;
use std::fs::write;

fn main() {
   let out_file = "output.txt";
    let text = "Hello World!";

    write(out_file, text).unwrap();
}
```

