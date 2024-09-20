file_path = './my-text-file.txt'

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        print(f"line: {line}")
