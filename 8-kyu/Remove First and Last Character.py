# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
# You're given one parameter, the original string.
# You don't have to worry with strings with less than two characters.

# 1st solution

def remove_char(s):
    rem = list(s)
    rem.pop(-1)
    rem.pop(0)
    com = "".join(rem)
    return com

# 2nd solution improved


def remove_char(s):
    return s[1:-1]
