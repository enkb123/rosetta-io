+++
title = ''
draft = false
+++

# streaming_stdin

Read from stdin line by line

## Python

```python {filename="streaming_stdin.py"}
while True:
try:
    user_input = input()
    print("received " + user_input)
except EOFError:
    break
```

## Ruby

```ruby {filename="streaming_stdin.rb"}
STDOUT.sync = true

while input = gets
  puts "received #{input}"
end
```

## Nodejs

```javascript {filename="streaming_stdin.mjs"}
import * as readline from 'node:readline/promises'

const rl = readline.createInterface({ input: process.stdin })

for await (const line of rl) {
  console.log("received", line)
}
```

## Deno

```javascript {filename="streaming_stdin.mjs"}
import { readLines } from 'https://deno.land/std/io/mod.ts';

const rl = readLines(Deno.stdin);

for await (const line of rl) {
  console.log("received", line);
}
```

## Php

```php {filename="streaming_stdin.php"}
<?php

while ($user_input = fgets(STDIN)) {
    echo "received ", $user_input;
}
```

## R

```r {filename="streaming_stdin.R"}
while(length(line <- readLines("stdin", n = 1L)) > 0) {
  cat("received", line, "\n")
}
```

## Perl

```perl {filename="streaming_stdin.pl"}
use strict;
use warnings;

$| = 1;
print "received $_" while <STDIN>;
```

## Java

```java {filename="StreamingStdin.java"}
import java.util.Scanner;
import java.util.stream.Stream;

public class StreamingStdin {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Stream.generate(scanner::nextLine)
              .takeWhile(line -> !line.isEmpty())
              .forEach(line -> System.out.println("received " + line));

        scanner.close();
    }
}
```

## Bash 3

```bash {filename="streaming_stdin.sh"}
while IFS= read -r user_input|| [[ -n $user_input ]]; do
  echo "received $user_input"
done | tr '[:upper:]' '[:lower:]'
```

## Bash 5

```bash {filename="streaming_stdin.sh"}
while IFS= read -r user_input|| [[ -n $user_input ]]; do
  echo "received $user_input"
done | tr '[:upper:]' '[:lower:]'
```

## Lua

```lua {filename="streaming_stdin.lua"}
for user_input in io.lines() do
    print("received " .. user_input)
end
```

## C#

```csharp {filename="StreamingStdin.cs"}
using System;

class StreamingStdin{
    public static void Main(string[] args){
        string line;

        while (!string.IsNullOrEmpty(line = Console.ReadLine())){
            Console.WriteLine($"received {line}");
        }
    }
}
```

## Go

```go {filename="streaming_stdin.go"}
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		fmt.Println("received", scanner.Text())
	}
}
```

## Swift

```swift {filename="streaming_stdin.swift"}
#if os(macOS) || os(iOS)
import Darwin
#elseif os(Linux)
import Glibc
#endif
setvbuf(stdout, nil, _IONBF, 0)

import Foundation

while let line = readLine() {
    print("received \(line)")
}
```

## Raku

```raku {filename="streaming_stdin.raku"}
for lines() {
    say "received $_";
    $*OUT.flush;
}
```

## Rust

```rust {filename="streaming_stdin.rs"}
use std::io::{self, BufRead};

fn main() {
    for maybe_line in io::stdin().lock().lines() {
        let line = maybe_line.unwrap().trim().to_string();
        if line.is_empty() {
            break;
        }
        println!("received {}", line);
    }
}
```

