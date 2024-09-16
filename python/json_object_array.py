import json
import sys


args = sys.argv[1:]

my_array = [{arg.upper(): len(arg)} for arg in args]

print(json.dumps(my_array))
