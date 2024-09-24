import { readLines } from 'https://deno.land/std/io/mod.ts';

const output = await Deno.open('streaming-out.pipe', { write: true });
const input = await Deno.open('streaming-in.pipe', { read: true });

const textEncoder = new TextEncoder();

for await (const line of readLines(input)) {
  await output.write(textEncoder.encode(`received ${line}\n`));
}

input.close();
output.close();
