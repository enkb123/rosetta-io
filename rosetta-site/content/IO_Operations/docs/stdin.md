+++
title = ''
draft = false
+++

# stdin

Read from stdin line by line

## Python

`stdin.py`

```python
while True:
try:
    user_input = input()
    print("line: " + user_input)
except EOFError:
    break
```

## Ruby

`stdin.rb`

```ruby
while user_input = gets
  puts "line: #{user_input}"
end
```

## Nodejs

`stdin.mjs`

```javascript
import * as readline from 'node:readline/promises'

const rl = readline.createInterface({ input: process.stdin })

for await (const line of rl) {
  console.log("line:", line)
}
```

## Deno

`stdin.mjs`

```javascript
import { readLines } from 'https://deno.land/std/io/mod.ts';

const rl = readLines(Deno.stdin);

for await (const line of rl) {
  console.log("line:", line);
}
```

## Php

`stdin.php`

```php
<?php

while ($user_input = fgets(STDIN)) {
    echo "line: ", $user_input;
}
```

## R

`stdin.R`

```r
for (line in readLines("stdin")) {
  cat("line:", line, "\n")
}
```

## Perl

`stdin.pl`

```perl
use strict;
use warnings;

print "line: $_" while <STDIN>;
```

## Java

`Stdin.java`

```java
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

`stdin.sh`

```bash
while IFS= read -r user_input|| [[ -n $user_input ]]; do
  echo "line: $user_input"
done | tr '[:upper:]' '[:lower:]'
```

## Bash 5

`stdin.sh`

```bash
while IFS= read -r user_input|| [[ -n $user_input ]]; do
  echo "line: $user_input"
done | tr '[:upper:]' '[:lower:]'
```

## Lua

`stdin.lua`

```lua
for user_input in io.lines() do
    print("line: " .. user_input)
end
```

## C#

`Stdin.cs`

```csharp
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

`stdin.go`

```go
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

`stdin.swift`

```swift
import Foundation

while let line = readLine() {
    print("line: \(line)")
}
```

## Raku

`stdin.raku`

```raku
use v6;

for lines() {
    say "line: $_";
}
```

## Rust

`stdin.rs`

```rust
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

