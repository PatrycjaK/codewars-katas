# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example:
# 348597 => [7,9,5,8,4,3]


def digitize(n):
    abc = list(str(n))
    for item in range(0, len(abc)):
        abc[item] = int(abc[item])
    cba = abc[::-1]
    return cba
