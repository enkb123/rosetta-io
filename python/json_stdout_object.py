import json
import sys

my_strings = sys.argv[1:]

string_length_dict = {string: len(string) for string in my_strings}

print(json.dumps(string_length_dict))
