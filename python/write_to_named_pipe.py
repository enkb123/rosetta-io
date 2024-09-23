import os

pipe_path = 'output.pipe'

if not os.path.exists(pipe_path):
    os.mkfifo(pipe_path)

with open(pipe_path, 'w') as pipe:
    pipe.write("Hello World!\n")
