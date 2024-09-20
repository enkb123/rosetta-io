while True:
    try:
        user_input = input()
        print("received " + user_input)
    except EOFError:
        break
