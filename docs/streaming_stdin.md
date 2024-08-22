# streaming_stdin

## Python

`streaming_stdin.py`

```python
"""Script reads streaming input text and then prints capitalized string to stdout"""

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
# Script reads streaming input text and then prints capitalized string to stdout

STDOUT.sync = true

while input = gets
  puts input.upcase
end
```

## Nodejs

`streaming_stdin.mjs`

```javascript
// Script reads streaming input text and then prints capitalized string to stdout

import * as readline from 'node:readline/promises'

const rl = readline.createInterface({ input: process.stdin })

for await (const line of rl) {
  console.log(line.toUpperCase())
}
```

## Deno

`streaming_stdin.mjs`

```javascript
// Script reads streaming input text and then prints capitalized string to stdout
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
// Script reads streaming input text and then prints capitalized string to stdout

while ($user_input = fgets(STDIN)) {
    echo strtoupper($user_input);
}

```

## R

`streaming_stdin.R`

```r
#' Script to read input from stdin, line by line, transform, and write to stdout

while(length(line <- readLines("stdin", n = 1L)) > 0) {
  cat(toupper(line), fill = TRUE)
}

```

## Perl

`streaming_stdin.pl`

```perl
use strict;
use warnings;

$| = 1;  # Turn off output buffering

print uc while <STDIN>;

```

## Java

`StreamingStdin.java`

```java
// Script reads streaming input text and then prints capitalized string to stdout

import java.util.Scanner;
import java.util.stream.Stream;

public class StreamingStdin {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Stream.generate(scanner::nextLine)
              .takeWhile(line -> !line.isEmpty()) // or other termination condition
              .map(String::toUpperCase)
              .forEach(System.out::println);
        scanner.close();
    }
}

```

## Bash 3

`streaming_stdin.sh`

```bash
#!/bin/bash

# Script reads streaming input text and then prints capitalized string to stdout

tr '[:lower:]' '[:upper:]'

```

## Bash 5

`streaming_stdin.sh`

```bash
#!/bin/bash

# Script reads streaming input text and then prints capitalized string to stdout

tr '[:lower:]' '[:upper:]'

```

## Lua

`streaming_stdin.lua`

```lua
-- Lua script to read streaming input and print capitalized string to stdout

-- Read all input lines and capitalize each line, then print
for line in io.lines() do
    print(line:upper())
end

```

## C#

`StreamingStdin.cs`

```csharp
// Script reads streaming input text and then prints capitalized string to stdout

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
// Script reads streaming input text and then prints capitalized string to stdout

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
// Script reads streaming input text and then prints capitalized string to stdout

// Turn off buffering for stdout
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
#Script reads streaming input text and then prints capitalized string to stdout
use v6;

for lines() {
    say .uc;
    $*OUT.flush;
}

```

