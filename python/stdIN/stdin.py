# Test script to get input, transform, and return it
import sys

if len(sys.argv) != 2:
    print("Usage: python stdin.py <input_string>")
    sys.exit(1)

user_input = sys.argv[1]
capitalized_input = user_input.upper()
print(capitalized_input)
