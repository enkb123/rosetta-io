//Script reads text from a named pipe and writes it to stdout, capitalized

import { readLines } from 'https://deno.land/std/io/mod.ts';

const pipePath = Deno.args[0];


const file = await Deno.open(pipePath, { read: true });

const rl = readLines(file);

for await (const line of rl) {
  console.log(line.toUpperCase());
}

file.close();
