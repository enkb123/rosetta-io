while True:
    try:
        user_input = input()
        print("line: " + user_input)
    except EOFError:
        break
