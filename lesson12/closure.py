# Closure is a function having access to the scope of its parent
# function after the parent function has returned.


def parent_function(person, coins):
    coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game  # This will return the inner function play_game, which has access to the
    # variable coins from the parent_function scope.


tommy = parent_function(
    "Tommy", 3
)  # This will create a closure for Tommy with 3 coins.
jenny = parent_function("Jenny", 5)

tommy()
tommy()

jenny()

tommy()
