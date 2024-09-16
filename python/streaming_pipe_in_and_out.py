import sys

pipe_in = sys.argv[1]
pipe_out = sys.argv[2]

with open(pipe_in, 'r', encoding='utf-8') as input_pipe:
    with open(pipe_out, 'w', encoding='utf-8') as output_pipe:
        for line in input_pipe:
            output_pipe.write(line.upper())
            output_pipe.flush()
