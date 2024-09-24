outfile = "output.pipe"
text = "Hello World!"

with open(outfile, 'w', encoding='utf-8') as f:
    f.write(text)
