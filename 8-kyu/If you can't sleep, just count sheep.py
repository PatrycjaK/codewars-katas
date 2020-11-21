# If you can't sleep, just count sheep!!

# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.


def count_sheep(n):
    total_sheeps = ''
    for sheep in range(1, n+1):
        total_sheeps += '{} sheep...'.format(sheep)
    return total_sheeps
