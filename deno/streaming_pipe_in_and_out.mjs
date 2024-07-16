//Script reads text from a named pipe and writes it another named pipe, capitalized

import { readLines } from 'https://deno.land/std/io/mod.ts';

const pipeInPath = Deno.args[0];
const pipeOutPath = Deno.args[1];

const input = await Deno.open(pipeInPath, { read: true });
const output = await Deno.open(pipeOutPath, { write: true });

const rl = readLines(input);

for await (const line of rl) {
  const uppercaseLine = line.toUpperCase() + '\n';
  const bytes = new TextEncoder().encode(uppercaseLine);
  await Deno.write(output.rid, bytes);
}

input.close();
output.close();
