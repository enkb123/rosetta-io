import sys

pipe_in = "input.pipe"

with open(pipe_in, 'r', encoding='utf-8') as input_pipe:
    for line in input_pipe:
        sys.stdout.write(line.upper())
        sys.stdout.flush()
