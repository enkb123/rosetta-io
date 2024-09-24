import { readLines } from 'https://deno.land/std/io/mod.ts';

const file = await Deno.open("input.pipe", { read: true });

for await (const line of readLines(file)) {
  console.log(line.toUpperCase());
}

file.close();
