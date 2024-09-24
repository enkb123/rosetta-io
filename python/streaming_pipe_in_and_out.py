input_file = 'streaming-in.pipe'
output_file = 'streaming-out.pipe'

with open(input_file, 'r', encoding='utf-8') as input_pipe:
    with open(output_file, 'w', encoding='utf-8') as output_pipe:
        for line in input_pipe:
            output_pipe.write(f"received {line.strip()}\n")
            output_pipe.flush()
