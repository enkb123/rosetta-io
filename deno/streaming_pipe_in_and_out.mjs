import { readLines } from 'https://deno.land/std/io/mod.ts';

const [pipeInPath, pipeOutPath] = Deno.args;

const input = await Deno.open(pipeInPath, { read: true });
const output = await Deno.open(pipeOutPath, { write: true });

const rl = readLines(input);

for await (const line of readLines(input)) {
  await output.write(new TextEncoder().encode(line.toUpperCase() + '\n'));
}

input.close();
output.close();
