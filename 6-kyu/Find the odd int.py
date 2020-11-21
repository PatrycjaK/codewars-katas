# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.


def find_it(lista):
    for i in range(0, len(lista)):
        counter = 0
        for j in range(0, len(lista)):
            if lista[i] == lista[j]:
                counter += 1
        if counter % 2 != 0:
            return lista[i]
