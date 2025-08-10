class JustNotCoolError(
    Exception
):  # Custom exception class based on Python Exception class. Here renamed to JustNotCoolError.
    pass


x = 2
try:
    raise JustNotCoolError(
        "This just isn't cool, man."
    )  # Raise custom exception message to introduce this custom class.
    # raise Exception("I'm a custom exception!")
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
except NameError:  # Name error message if something is not defined.
    print("NameError means something is probably undefined.")
except (
    ZeroDivisionError
):  # Zero division error message if something is divided by zero.
    print("Please do not divide by zero.")
except Exception as error:  # Catch all other exceptions.
    print(error)
else:  # If no exceptions are raised, this block will execute.
    print("No errors!")
finally:  # This block will always execute, regardless of whether an exception was raised or not.
    print("I'm going to print with or without an error.")
