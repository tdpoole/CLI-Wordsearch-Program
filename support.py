def inputint(q):
    while True:
        try:
            r=int(input(q))
        except TypeError:
            print("That answer was invalid. Please input an integer.")
        else:
            return r