import base64
import sys

test_string = sys.argv[1]

encoded_string = base64.b64encode(test_string.encode()).decode()

print(encoded_string)
