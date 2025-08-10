from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"


def randomfunfact():
    funfacts = [
        "Kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas City.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas.",
    ]

    index = choice("0123")  # Randomly select an index from 0 to 3.

    print(funfacts[int(index)])


if (
    __name__ == "__main__"
):  # This block will only run if this file is executed directly. Otherwise, it will not run if this file is imported as a module. If this is missing, the function will run when imported.
    randomfunfact()
