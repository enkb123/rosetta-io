# stdin

## Python

`stdin.py`

```python
"""Script to read stdin line by line, transform, and return it"""

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
# Test script to get input, transform, and write to stdout

i = 1

while user_input = gets
  puts "#{i} #{user_input.upcase}"
  i += 1
end
```

## Nodejs

`stdin.mjs`

```javascript
// Script to read stdin line by line, transform, and write to stdout
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
// Script to read stdin line by line, transform, and write to stdout
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
// Script to read stdin line by line, transform, and return it

$i = 1;

while ($user_input = fgets(STDIN)) { // fgets returns false when nothing left to read
    echo $i++ . ' ' . strtoupper($user_input);
}

```

## R

`stdin.R`

```r
#' Script to read stdin, transform, and return it

i <- 1
for (line in readLines("stdin")) {
  cat(i, toupper(line), sep = " ", fill = TRUE) # fill flag adds new line
  i <- i + 1
}

```

## Perl

`stdin.pl`

```perl
# Test script to get input, transform, and write to stdout
use strict;
use warnings;

my $i = 1;
print $i++ . " " . uc while <STDIN>;

```

## Java

`Stdin.java`

```java
// Test script to get input, transform, and write to stdout

import java.util.Scanner;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Stream;

public class Stdin {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        AtomicInteger counter = new AtomicInteger(1);

        // Create a stream of lines from Scanner
        Stream.generate(scanner::nextLine)
              .takeWhile(line -> !line.isEmpty()) // Assuming empty line signals end, adjust as needed
              .forEach(line -> System.out.println(counter.getAndIncrement() + " " + line.toUpperCase()));

        scanner.close();
    }
}

```

## Bash 3

`stdin.sh`

```bash
#!/bin/bash

# Test script to get input, transform, and write to stdout

i=1

while IFS= read -r user_input; do
  echo "$((i++)) $user_input"
done | tr '[:lower:]' '[:upper:]'

```

## Bash 5

`stdin.sh`

```bash
#!/bin/bash

i=1

while IFS= read -r user_input; do
  echo "$((i++)) ${user_input^^}"
done

```

## Lua

`stdin.lua`

```lua
-- Lua script to read input, transform to uppercase, and print with line numbers
local i = 1

-- Read from stdin until EOF
for user_input in io.lines() do
    -- Transform input to uppercase and prepend with line number
    print(i .. " " .. user_input:upper())
    i = i + 1
end



```

## C#

`Stdin.cs`

```csharp
// Test script to get input, transform, and write to stdout

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
// Test script to get input, transform, and write to stdout
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
//Script to read stdin line by line, transform, and return it

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
# Test script to get input, transform, and write to stdout
use v6;

my $i = 1;
for lines() {
    say $i++ ~ " " ~ .uc;
}

```

