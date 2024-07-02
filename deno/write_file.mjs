// Script to write text to a new file

const [filename, ...textParts] = Deno.args;
const text = textParts.join(' ');

await Deno.writeTextFile(filename, text);
console.log(`Successfully wrote to ${filename}`);

