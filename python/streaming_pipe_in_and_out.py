# Script reads text from a named pipe and writes it another named pipe, capitalized
import os
import sys
import select
import time

pipe_in = sys.argv[1]
pipe_out = sys.argv[2]

input_pipe = os.open(pipe_in, os.O_RDONLY | os.O_NONBLOCK)
output_pipe = open(pipe_out, 'w')

def is_readable(file_descriptor):
    return select.select([file_descriptor], [], [], 0) == ([file_descriptor], [], [])

while True:
    try:
        line = os.read(input_pipe, 1024)
        if not line:
            break
        output_pipe.write(line.decode().upper())
        output_pipe.flush()
    except BlockingIOError:
        time.sleep(0.1)  # Sleep if no data is available

os.close(input_pipe)
output_pipe.close()
