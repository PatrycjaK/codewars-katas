# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.


# 1st solution

def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    else:
        return 'No'

# 2nd solution


def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'
