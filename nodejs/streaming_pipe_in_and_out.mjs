// Script reads text from a named pipe and writes it another named pipe, capitalized
import * as fs from 'fs';

const pipeIn = process.argv[2];
const pipeOut = process.argv[3];

const input = fs.createReadStream(pipeIn);
const output = fs.createWriteStream(pipeOut);

let remainingData = '';

input.on('data', (chunk) => {
  remainingData += chunk;
  const lines = remainingData.split('\n');

  for (let i = 0; i < lines.length - 1; i++) {
    output.write(lines[i].toUpperCase() + '\n');
  }

  remainingData = lines[lines.length - 1];
});

input.on('end', () => {
  output.end(); // Close the output stream
});
