import sys

outfile = "output.txt"
text = "Hello World!"

with open(outfile, 'w') as f:
    f.write(text)
