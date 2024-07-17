//Script reads text from a named pipe and writes it to stdout, capitalized

import { readLines } from 'https://deno.land/std/io/mod.ts';

const [pipePath] = Deno.args;
const file = await Deno.open(pipePath, { read: true });

for await (const line of readLines(file)) {
  console.log(line.toUpperCase());
}

file.close();
