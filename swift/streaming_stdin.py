"""Script reads streaming input text and then prints capitalized string to stdout"""

while True:
    try:
        x = input()
        print(x.upper())
    except EOFError:
        break