import sys

outfile = sys.argv[1]
text = sys.argv[2]

with open(outfile, 'w') as f:
    f.write(text.upper())
