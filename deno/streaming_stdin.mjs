// Script reads streaming input text and then prints capitalized string to stdout
import { readLines } from 'https://deno.land/std/io/mod.ts';

const rl = readLines(Deno.stdin);

for await (const line of rl) {
  console.log(line.toUpperCase());
}
