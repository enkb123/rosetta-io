import sys

pipe_in = sys.argv[1]

with open(pipe_in, 'r', encoding='utf-8') as input_pipe:
    for line in input_pipe:
        sys.stdout.write(line.upper())
        sys.stdout.flush()
