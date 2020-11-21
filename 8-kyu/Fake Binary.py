# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.


# 1st solution

def fake_bin(x):
    num_list = []
    result_list = []

    for item in x:
        item = int(item)
        num_list.append(item)
        if item < 5:
            item = str(0)
            result_list.append(item)
        else:
            item = str(1)
            result_list.append(item)
    result = ''.join(result_list)
    return result


# 2nd solution

def fake_bin(x):
    num_list = []
    result_list = []

    for item in x:
        item = int(item)
        num_list.append(item)
        if item < 5:
            result_list.append('0')
        else:
            result_list.append('1')
    result = ''.join(result_list)
    return result
