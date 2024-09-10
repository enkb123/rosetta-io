const [filename, ...textParts] = Deno.args;
const text = textParts.join(' ');

await Deno.writeTextFile(filename, text.toUpperCase());
