const filename = "output.txt";
const text = "Hello World!";

await Deno.writeTextFile(filename, text);
