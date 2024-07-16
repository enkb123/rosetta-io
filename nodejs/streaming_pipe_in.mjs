//Script reads text from a named pipe and writes it to stdout, capitalized

import * as fs from 'fs';

const pipeIn = process.argv[2];

const input = fs.createReadStream(pipeIn);

let remainingData = '';

input.on('data', (chunk) => {
  remainingData += chunk;
  const lines = remainingData.split('\n');

  for (let i = 0; i < lines.length - 1; i++) {
    console.log(lines[i].toUpperCase());
  }
  remainingData = lines[lines.length - 1];
});
