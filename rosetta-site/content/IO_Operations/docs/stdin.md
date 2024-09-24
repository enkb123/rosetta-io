+++
title = ''
draft = false
+++

# stdin

Read from stdin line by line

## Python

```python {filename="stdin.py"}
while True:
try:
    user_input = input()
    print("line: " + user_input)
except EOFError:
    break
```

## Ruby

```ruby {filename="stdin.rb"}
while user_input = gets
  puts "line: #{user_input}"
end
```

## Nodejs

```javascript {filename="stdin.mjs"}
import * as readline from 'node:readline/promises'

const rl = readline.createInterface({ input: process.stdin })

for await (const line of rl) {
  console.log("line:", line)
}
```

## Deno

```javascript {filename="stdin.mjs"}
import { readLines } from 'https://deno.land/std/io/mod.ts';

const rl = readLines(Deno.stdin);

for await (const line of rl) {
  console.log("line:", line);
}
```

## Php

```php {filename="stdin.php"}
<?php

while ($user_input = fgets(STDIN)) {
    echo "line: ", $user_input;
}
```

## R

```r {filename="stdin.R"}
for (line in readLines("stdin")) {
  cat("line:", line, "\n")
}
```

## Perl

```perl {filename="stdin.pl"}
use strict;
use warnings;

print "line: $_" while <STDIN>;
```

## Java

```java {filename="Stdin.java"}
import java.util.Scanner;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Stream;

public class Stdin {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Stream.generate(scanner::nextLine)
              .takeWhile(line -> !line.isEmpty())
              .forEach(line -> System.out.println("line: " + line));

        scanner.close();
    }
}
```

## Bash 3

```bash {filename="stdin.sh"}
while IFS= read -r user_input|| [[ -n $user_input ]]; do
  echo "line: $user_input"
done | tr '[:upper:]' '[:lower:]'
```

## Bash 5

```bash {filename="stdin.sh"}
while IFS= read -r user_input|| [[ -n $user_input ]]; do
  echo "line: $user_input"
done | tr '[:upper:]' '[:lower:]'
```

## Lua

```lua {filename="stdin.lua"}
for user_input in io.lines() do
    print("line: " .. user_input)
end
```

## C#

```csharp {filename="Stdin.cs"}
using System;
using System.Collections.Generic;
using System.Linq;

class Stdin
{
    public static void Main(string[] args)
    {
        string line;
        while ((line = Console.ReadLine()) != null)
        {
            Console.WriteLine($"line: {line}");
        }
    }
}
```

## Go

```go {filename="stdin.go"}
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		fmt.Println("line: " + scanner.Text())
	}
}
```

## Swift

```swift {filename="stdin.swift"}
import Foundation

while let line = readLine() {
    print("line: \(line)")
}
```

## Raku

```raku {filename="stdin.raku"}
use v6;

for lines() {
    say "line: $_";
}
```

## Rust

```rust {filename="stdin.rs"}
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    for line in stdin.lock().lines() {
        let line = line.unwrap().trim().to_string();
        if line.is_empty() {
            break;
        }
        println!("line: {}", line);
    }
}
```

