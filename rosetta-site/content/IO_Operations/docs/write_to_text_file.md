+++
title = ''
draft = false
+++

# write_to_text_file

Write to a text file

## Python

```python {filename="write_to_text_file.py"}
outfile = "output.txt"
text = "Hello World!"

with open(outfile, 'w', encoding='utf-8') as f:
    f.write(text)
```

## Ruby

```ruby {filename="write_to_text_file.rb"}
File.write "output.txt", "Hello World!"
```

## Nodejs

```javascript {filename="write_to_text_file.mjs"}
import fs from 'fs/promises'

await fs.writeFile("output.txt", "Hello World!")
```

## Deno

```javascript {filename="write_to_text_file.mjs"}
await Deno.writeTextFile("output.txt", "Hello World!");
```

## Php

```php {filename="write_to_text_file.php"}
<?php

file_put_contents("output.txt", "Hello World!");
```

## R

```r {filename="write_to_text_file.R"}
writeLines("Hello World!", "output.txt")
```

## Perl

```perl {filename="write_to_text_file.pl"}
use strict;
use warnings;

open my $fh, '>', "output.txt";
print $fh "Hello World!";
close $fh;
```

## Java

```java {filename="WriteToTextFile.java"}
import java.nio.charset.StandardCharsets;
import java.nio.file.*;

public class WriteToTextFile {
    public static void main(String[] args) throws Exception {
        var outFile = Paths.get("output.txt");
        var text = "Hello World!";
        Files.write(outFile, text.getBytes(StandardCharsets.UTF_8));
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
local file = io.open("output.txt", "w")
file:write("Hello World!")
file:close()
```

## C#

```csharp {filename="WriteToTextFile.cs"}
using System;
using System.IO;

class WriteToTextFile
{
    public static void Main(string[] args)
    {

        File.WriteAllText("output.txt", "Hello World!");
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
	os.WriteFile("output.txt", []byte("Hello World!"), 0)
}
```

## Swift

```swift {filename="write_to_text_file.swift"}
import Foundation

try "Hello World!".write(toFile: "output.txt", atomically: false, encoding: .utf8)
```

## Raku

```raku {filename="write_to_text_file.raku"}
use v6;

my $fh = open "output.txt", :w;
$fh.print: "Hello World!";
$fh.close;
```

## Rust

```rust {filename="write_to_text_file.rs"}
use std::fs::write;

fn main() {
    write("output.txt", "Hello World!").unwrap();
}
```

