//Script reads text from a named pipe and writes it another named pipe, capitalized

const [pipe_in, pipe_out] = Deno.args.slice(0, 2);

const inputPipe = await Deno.open(pipe_in);
const outputPipe = await Deno.open(pipe_out, { write: true, create: true });

const decoder = new TextDecoder("utf-8");
const encoder = new TextEncoder();


const buf = new Uint8Array(1024); // Buffer size for reading

while (true) {
  const n = await inputPipe.read(buf);
  if (n === null) break;
  const chunk = decoder.decode(buf.subarray(0, n));
  await outputPipe.write(encoder.encode(chunk.toUpperCase()));
}

  inputPipe.close();
  outputPipe.close();
