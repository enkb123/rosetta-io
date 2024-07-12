//Script reads text from a named pipe and writes it to stdout, capitalized

import { createReadStream } from 'fs';

const [pipe_in] = process.argv.slice(2);

const inputPipe = createReadStream(pipe_in);

inputPipe.setEncoding('utf8');

inputPipe.on('data', (chunk) => {
  process.stdout.write(chunk.toUpperCase());
});

inputPipe.on('end', () => {
  process.stdout.end();
});
