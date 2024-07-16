# Script reads text from a named pipe and writes it another named pipe, capitalized
import sys

pipe_in = sys.argv[1]
pipe_out = sys.argv[2]

with open(pipe_in, 'r', encoding='utf-8') as input_pipe:
    output_pipe = open(pipe_out, 'w')
    for line in input_pipe:
        output_pipe.write(line.upper())
        output_pipe.flush()
