# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case


def is_isogram(string):
    char_frequency = {}
    for s in string.lower():
        if s in char_frequency:
            char_frequency[s] += 1
        else:
            char_frequency[s] = 1
    if string == "" or max(char_frequency.values()) <= 1:
        return True
    else:
        return False
