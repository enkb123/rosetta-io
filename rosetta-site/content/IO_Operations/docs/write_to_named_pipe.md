+++
title = ''
draft = false
+++

# write_to_named_pipe

Write text to a named pipe

## Python

```python {filename="write_to_named_pipe.py"}
outfile = "output.pipe"
text = "Hello World!"

with open(outfile, 'w', encoding='utf-8') as f:
    f.write(text)
```

## Ruby

```ruby {filename="write_to_named_pipe.rb"}
File.write "output.pipe", "Hello World!"
```

## Nodejs

```javascript {filename="write_to_named_pipe.mjs"}
import fs from 'fs/promises'

await fs.writeFile("output.pipe", "Hello World!")
```

## Deno

```javascript {filename="write_to_named_pipe.mjs"}
const encoder = new TextEncoder();

await Deno.writeFile("output.pipe", encoder.encode("Hello World!"));
```

## Php

```php {filename="write_to_named_pipe.php"}
<?php

file_put_contents("output.pipe", "Hello World!");
```

## R

```r {filename="write_to_named_pipe.R"}
writeLines("Hello World!", "output.pipe")
```

## Perl

```perl {filename="write_to_named_pipe.pl"}
use strict;
use warnings;

open my $fh, '>', "output.pipe";
print $fh "Hello World!";
close $fh;
```

## Java

```java {filename="WriteToNamedPipe.java"}
import java.nio.charset.StandardCharsets;
import java.nio.file.*;

public class WriteToNamedPipe {
    public static void main(String[] args) throws Exception {
        var outFile = Paths.get("output.pipe");
        var text = "Hello World!";
        Files.write(outFile, text.getBytes(StandardCharsets.UTF_8));
    }
}
```

## Bash 3

```bash {filename="write_to_named_pipe.sh"}
echo "Hello World!" > output.pipe
```

## Bash 5

```bash {filename="write_to_named_pipe.sh"}
echo "Hello World!" > output.pipe
```

## Lua

```lua {filename="write_to_named_pipe.lua"}
local file = io.open("output.pipe", "w")
file:write("Hello World!")
file:close()
```

## C#

```csharp {filename="WriteToNamedPipe.cs"}
using System;
using System.IO;
using System.Diagnostics;

class WriteToNamedPipe
{
    public static void Main(string[] args)
    {
        using var writer = new StreamWriter("output.pipe") { AutoFlush = true };
        writer.WriteLine("Hello World!");
    }
}
```

## Go

```go {filename="write_to_named_pipe.go"}
package main

import (
	"os"
)

func main() {
	os.WriteFile("output.pipe", []byte("Hello World!"), 0)
}
```

## Swift

```swift {filename="write_to_named_pipe.swift"}
import Foundation

try "Hello World!".write(toFile: "output.pipe", atomically: false, encoding: .utf8)
```

## Raku

```raku {filename="write_to_named_pipe.raku"}
use v6;

my $fh = open "output.pipe", :w;
$fh.print: "Hello World!";
$fh.close;
```

## Rust

```rust {filename="write_to_named_pipe.rs"}
use std::fs::write;

fn main() {
    write("output.pipe", "Hello World!").unwrap();
}
```

