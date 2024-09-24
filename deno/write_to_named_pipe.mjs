const encoder = new TextEncoder();

await Deno.writeFile("output.pipe", encoder.encode("Hello World!"));
