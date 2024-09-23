import { readLines } from 'https://deno.land/std/io/mod.ts';

const output = await Deno.open('streaming-out.pipe', { write: true, create: true });

const input = await Deno.open('streaming-in.pipe', { read: true });

for await (const line of readLines(input)) {
  await output.write(new TextEncoder().encode(`received ${line}\n`));
}

input.close();

output.close();
