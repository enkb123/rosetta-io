+++
title = ''
draft = false
+++

# stdin

Check that input is read from stdin, line by line.
The script executed in the docker container accepts a text file as input,
reads each line, capitalizes it, then prints it out.


## Python

`stdin.py`

```python
i = 1
while True:
    try:
        user_input = input()
        print(i, user_input.upper())
        i += 1
    except EOFError:
        break
```

## Ruby

`stdin.rb`

```ruby
i = 1

while user_input = gets
  puts "#{i} #{user_input.upcase}"
  i += 1
end
```

## Nodejs

`stdin.mjs`

```javascript
import * as readline from 'node:readline/promises'

const rl = readline.createInterface({ input: process.stdin })

let i = 1
for await (const line of rl) {
  console.log(i, line.toUpperCase())
  i += 1
}
```

## Deno

`stdin.mjs`

```javascript
import { readLines } from 'https://deno.land/std/io/mod.ts';

const rl = readLines(Deno.stdin);

let i = 1;
for await (const line of rl) {
  console.log(i, line.toUpperCase());
  i += 1;
}
```

## Php

`stdin.php`

```php
<?php

$i = 1;

while ($user_input = fgets(STDIN)) {
    echo $i++ . ' ' . strtoupper($user_input);
}
```

## R

`stdin.R`

```r
i <- 1
for (line in readLines("stdin")) {
  cat(i, toupper(line), sep = " ", fill = TRUE)
  i <- i + 1
}
```

## Perl

`stdin.pl`

```perl
use strict;
use warnings;

my $i = 1;
print $i++ . " " . uc while <STDIN>;
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
        AtomicInteger counter = new AtomicInteger(1);

        Stream.generate(scanner::nextLine)
              .takeWhile(line -> !line.isEmpty())
              .forEach(line -> System.out.println(counter.getAndIncrement() + " " + line.toUpperCase()));

        scanner.close();
    }
}
```

## Bash 3

`stdin.sh`

```bash
i=1

while IFS= read -r user_input; do
  echo "$((i++)) $user_input"
done | tr '[:lower:]' '[:upper:]'
```

## Bash 5

`stdin.sh`

```bash
i=1

while IFS= read -r user_input; do
  echo "$((i++)) ${user_input^^}"
done
```

## Lua

`stdin.lua`

```lua
local i = 1

for user_input in io.lines() do
    print(i .. " " .. user_input:upper())
    i = i + 1
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
        int counter = 1;
        while ((line = Console.ReadLine()) != null)
        {
            Console.WriteLine($"{counter++} {line.ToUpper()}");
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
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for lineNumber := 1; scanner.Scan(); lineNumber++ {
		fmt.Printf("%d %s\n", lineNumber, strings.ToUpper(scanner.Text()))
	}
}
```

## Swift

`stdin.swift`

```swift
import Foundation

var i = 1

while let user_input = readLine() {
    print("\(i) \(user_input.uppercased())")
    i += 1
}
```

## Raku

`stdin.raku`

```raku
use v6;

my $i = 1;
for lines() {
    say $i++ ~ " " ~ .uc;
}
```

## Rust

`stdin.rs`

```rust
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    for (counter, line) in stdin.lock().lines().enumerate() {
        let line = line.unwrap().trim().to_string();
        if line.is_empty() {
            break;
        }
        println!("{} {}", counter + 1, line.to_uppercase());
    }
}
```

