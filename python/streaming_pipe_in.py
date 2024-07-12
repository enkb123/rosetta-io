# Script reads text from a named pipe and writes it to stdout, capitalized
import os
import sys
import select
import time

pipe_in = sys.argv[1]

input_pipe = os.open(pipe_in, os.O_RDONLY | os.O_NONBLOCK)

def is_readable(file_descriptor):
    return select.select([file_descriptor], [], [], 0) == ([file_descriptor], [], [])

while True:
    try:
        line = os.read(input_pipe, 1024)
        if not line:
            break
        sys.stdout.write(line.decode().upper())
        sys.stdout.flush()
    except BlockingIOError:
        time.sleep(0.1)  # Sleep if no data is available

os.close(input_pipe)
