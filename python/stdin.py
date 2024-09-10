i = 1
while True:
    try:
        user_input = input()
        print(i, user_input.upper())
        i += 1
    except EOFError:
        break
