file_path = './my-text-file.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        print(f"line: {line}")
