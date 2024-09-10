import json
import sys

my_strings = sys.argv[1:]

string_letters_dict = {string: [s.upper() for s in string] for string in my_strings}

print(json.dumps(string_letters_dict))
