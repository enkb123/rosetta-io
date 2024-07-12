//Script reads text from a named pipe and writes it to stdout, capitalized

const [pipe_in] = Deno.args.slice(0, 1);

const inputPipe = await Deno.open(pipe_in);

const decoder = new TextDecoder("utf-8");
const encoder = new TextEncoder();

const bufSize = 1024; // Buffer size for reading
let remaining = "";


  while (true) {
    const buf = new Uint8Array(bufSize);
    const n = await inputPipe.read(buf);
    if (n === null) {
      break;
    }
    let chunk = decoder.decode(buf.subarray(0, n));
    chunk = remaining + chunk;
    const lines = chunk.split("\n");
    remaining = lines.pop() || ""; // Last element is incomplete line

    for (let line of lines) {
      console.log(line.toUpperCase());
    }
  }

  inputPipe.close();
