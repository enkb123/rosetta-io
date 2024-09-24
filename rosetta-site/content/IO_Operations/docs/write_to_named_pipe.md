+++
title = ''
draft = false
+++

# write_to_named_pipe

Write text to a named pipe

## Python

```python {filename="write_to_named_pipe.py"}
import os

pipe_path = 'output.pipe'

if not os.path.exists(pipe_path):
    os.mkfifo(pipe_path)

with open(pipe_path, 'w') as pipe:
    pipe.write("Hello World!\n")
```

## Ruby

```ruby {filename="write_to_named_pipe.rb"}
File.write "output.pipe", "Hello World!"
```

## Nodejs

```javascript {filename="write_to_named_pipe.mjs"}
import fs from 'fs';

const [pipeName, text] = ["output.pipe", "Hello World!"];

const writeToPipe = (pipe, data) => {
    return new Promise((resolve) => {
        const writableStream = fs.createWriteStream(pipe);
        writableStream.on('finish', resolve);
        writableStream.write(data);
        writableStream.end();
    });
};

writeToPipe(pipeName, text)
```

## Deno

```javascript {filename="write_to_named_pipe.mjs"}
const encoder = new TextEncoder();
const pipePath = "output.pipe";

await Deno.open(pipePath, { create: true, write: true });

await Deno.writeFile(pipePath, encoder.encode("Hello World!"));
```

## Php

```php {filename="write_to_named_pipe.php"}
<?php

$pipePath = 'output.pipe';

if (!file_exists($pipePath)) {
    posix_mkfifo($pipePath, 0666);
}

$pipe = fopen($pipePath, 'w') or die("Could not open '$pipePath'");

fwrite($pipe, "Hello World!\n");

fclose($pipe);
```

## R

```r {filename="write_to_named_pipe.R"}
pipe_path <- "output.pipe"

if (!file.exists(pipe_path)) {
  system(paste("mkfifo", pipe_path))
}

pipe <- file(pipe_path, open = "w")

writeLines("Hello World!", pipe)

close(pipe)
```

## Perl

```perl {filename="write_to_named_pipe.pl"}
use strict;
use warnings;

my $pipe_path = 'output.pipe';

system("mkfifo $pipe_path") unless -e $pipe_path;

open(my $pipe, '>', $pipe_path) or die "Could not open '$pipe_path': $!";

print $pipe "Hello World!\n";

close($pipe);
```

## Java

```java {filename="WriteToNamedPipe.java"}
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.*;

public class WriteToNamedPipe {
    public static void main(String[] args) throws IOException, InterruptedException{
        String pipePath = "output.pipe";

        Path path = Paths.get(pipePath);
        if (!Files.exists(path)) {
            new ProcessBuilder("mkfifo", pipePath).inheritIO().start().waitFor();
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(pipePath))) {
            writer.write("Hello World!");
        }
    }
}
```

## Bash 3

```bash {filename="write_to_named_pipe.sh"}
pipe_out="output.pipe"

mkfifo "$pipe_out" 2>/dev/null

echo "Hello World!" > "$pipe_out"
```

## Bash 5

```bash {filename="write_to_named_pipe.sh"}
pipe_out="output.pipe"

mkfifo "$pipe_out" 2>/dev/null

echo "Hello World!" > "$pipe_out"
```

## Lua

```lua {filename="write_to_named_pipe.lua"}
local pipePath = "output.pipe"

os.execute("mkfifo " .. pipePath)

local pipe = io.open(pipePath, "w")
pipe:write("Hello World!\n")
pipe:close()
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
        string pipePath = "output.pipe";

        if (!File.Exists(pipePath))
        {
            Process.Start("mkfifo", pipePath)?.WaitForExit();
        }

        using (var pipeStream = new FileStream(pipePath, FileMode.Open, FileAccess.Write))
        using (var writer = new StreamWriter(pipeStream) { AutoFlush = true })
        {
            writer.WriteLine("Hello World!");
        }
    }
}
```

## Go

```go {filename="write_to_named_pipe.go"}
package main

import (
	"os"
	"syscall"
)

func main() {
	pipePath := "output.pipe"

	syscall.Mkfifo(pipePath, 0666)

	file, _ := os.OpenFile(pipePath, os.O_WRONLY|os.O_APPEND, os.ModeNamedPipe)
	defer file.Close()

	file.WriteString("Hello World!")
}
```

## Swift

```swift {filename="write_to_named_pipe.swift"}
import Foundation

let pipePath = "output.pipe"

if !FileManager.default.fileExists(atPath: pipePath) {
    mkfifo(pipePath, 0o644)
}

if let pipe = fopen(pipePath, "w") {
    fputs("Hello World!\n", pipe)
    fclose(pipe)
}
```

## Raku

```raku {filename="write_to_named_pipe.raku"}
use v6;

my $pipe-path = 'output.pipe';

my $path = IO::Path.new($pipe-path);
if !$path.e {
    run "mkfifo", $pipe-path;
}

my $pipe = open $pipe-path, :w;

$pipe.print("Hello World!\n");

$pipe.close;
```

## Rust

```rust {filename="write_to_named_pipe.rs"}
use std::fs::OpenOptions;
use std::io::Write;
use std::process::Command;

fn main() {
    let pipe_path = "output.pipe";

    if std::fs::metadata(pipe_path).is_err() {
        Command::new("mkfifo")
            .arg(pipe_path)
            .status();
    }

    let mut pipe = OpenOptions::new()
        .write(true)
        .open(pipe_path)
        .expect("Could not open named pipe");

    pipe.write_all(b"Hello World!\n");
}
```

