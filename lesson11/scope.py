name = "Dave"  # This is a global variable.
count = 1


def another():
    color = "blue"
    global count  # This will make a local scope variable a global variable.
    count += 1
    print(count)

    def greeting(name):
        nonlocal color  # This will allow us to modify the variable 'color' from the enclosing scope.
        color = "red"
        print(color)
        print(name)

    greeting("Dave")


another()
