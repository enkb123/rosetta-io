// Script to read stdin line by line, transform, and write to stdout
import { readLines } from 'https://deno.land/std/io/mod.ts';

const rl = readLines(Deno.stdin);

let i = 1;
for await (const line of rl) {
  console.log(i, line.toUpperCase());
  i += 1;
}
