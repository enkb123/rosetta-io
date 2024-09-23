const encoder = new TextEncoder();
const pipePath = "output.pipe";

await Deno.open(pipePath, { create: true, write: true });

await Deno.writeFile(pipePath, encoder.encode("Hello World!"));
