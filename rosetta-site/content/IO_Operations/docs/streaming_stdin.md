+++
title = ''
draft = false
+++

# streaming_stdin

Read from stdin line by line

## Python

`streaming_stdin.py`

```python
while True:
try:
    x = input()
    print(x.upper())
except EOFError:
    break
```

## Ruby

`streaming_stdin.rb`

```ruby
STDOUT.sync = true

while input = gets
  puts "received #{input}"
end
```

## Nodejs

`streaming_stdin.mjs`

```javascript
import * as readline from 'node:readline/promises'

const rl = readline.createInterface({ input: process.stdin })

for await (const line of rl) {
  console.log(line.toUpperCase())
}
```

## Deno

`streaming_stdin.mjs`

```javascript
import { readLines } from 'https://deno.land/std/io/mod.ts';

const rl = readLines(Deno.stdin);

for await (const line of rl) {
  console.log(line.toUpperCase());
}
```

## Php

`streaming_stdin.php`

```php
<?php

while ($user_input = fgets(STDIN)) {
    echo strtoupper($user_input);
}
```

## R

`streaming_stdin.R`

```r
while(length(line <- readLines("stdin", n = 1L)) > 0) {
  cat(toupper(line), fill = TRUE)
}
```

## Perl

`streaming_stdin.pl`

```perl
use strict;
use warnings;

$| = 1;

print uc while <STDIN>;
```

## Java

`StreamingStdin.java`

```java
import java.util.Scanner;
import java.util.stream.Stream;

public class StreamingStdin {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Stream.generate(scanner::nextLine)
              .takeWhile(line -> !line.isEmpty())
              .map(String::toUpperCase)
              .forEach(System.out::println);
        scanner.close();
    }
}
```

## Bash 3

`streaming_stdin.sh`

```bash
tr '[:lower:]' '[:upper:]'
```

## Bash 5

`streaming_stdin.sh`

```bash
tr '[:lower:]' '[:upper:]'
```

## Lua

`streaming_stdin.lua`

```lua
for line in io.lines() do
    print(line:upper())
end
```

## C#

`StreamingStdin.cs`

```csharp
using System;

class StreamingStdin{
    public static void Main(string[] args){
        string line;

        while (!string.IsNullOrEmpty(line = Console.ReadLine())){
            Console.WriteLine(line.ToUpper());
        }
    }
}
```

## Go

`streaming_stdin.go`

```go
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		fmt.Println(strings.ToUpper(scanner.Text()))
	}
}
```

## Swift

`streaming_stdin.swift`

```swift
#if os(macOS) || os(iOS)
import Darwin
#elseif os(Linux)
import Glibc
#endif
setvbuf(stdout, nil, _IONBF, 0)

import Foundation

while let line = readLine(), !line.isEmpty {
    print(line.uppercased())
}
```

## Raku

`streaming_stdin.raku`

```raku
use v6;

for lines() {
    say .uc;
    $*OUT.flush;
}
```

## Rust

`streaming_stdin.rs`

```rust
use std::io::{self, BufRead, Write};

fn main() {
    let mut stdout_handle = io::stdout().lock();
    let stdin_handle = io::stdin().lock();

    for line in stdin_handle.lines() {
        writeln!(stdout_handle, "{}", line.unwrap().to_uppercase()).unwrap();
        stdout_handle.flush().unwrap();
    }
}
```

