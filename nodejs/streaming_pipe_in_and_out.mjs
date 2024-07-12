// Script reads text from a named pipe and writes it another named pipe, capitalized

import { createReadStream, createWriteStream } from 'fs';

const [pipe_in, pipe_out] = process.argv.slice(2);

const inputPipe = createReadStream(pipe_in);
const outputPipe = createWriteStream(pipe_out);

inputPipe.setEncoding('utf8');

inputPipe.on('data', (chunk) => {
  outputPipe.write(chunk.toUpperCase());
});

inputPipe.on('end', () => {
  outputPipe.end();
});
