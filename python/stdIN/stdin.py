# Test script to get input, transform, and return it
import sys

# if len(sys.argv) != 2:
#     print("Usage: python stdin.py <input_string>")
#     sys.exit(1)
# 
# user_input = sys.argv[1]
i = 1
while True:
    try:
        user_input = input()
        print(i, user_input.upper())
        i += 1
    except EOFError:
        break


# print line number in front of each line
# Testing that it reads line by line
# and that it does the transformation (to make sure that we're
# getting the stdin throught python)