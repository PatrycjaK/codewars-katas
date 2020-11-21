# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

def filter_list(listed):
    integers = []
    for l in listed:
        if (isinstance(l, int)):
            integers.append(l)
    return integers
