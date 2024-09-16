while True:
    try:
        x = input()
        print(x.upper())
    except EOFError:
        break
