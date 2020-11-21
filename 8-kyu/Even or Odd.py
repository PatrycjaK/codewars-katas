# Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


# 1st solution

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 2nd solution


def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
