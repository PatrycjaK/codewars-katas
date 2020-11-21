# Write function avg which calculates average of numbers in given list.


def find_average(avg):
    sum = 0
    for a in avg:
        sum += a
    return sum/len(avg)
