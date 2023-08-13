#!/usr/bin/python3
def no_c(my_string):
    s = list(my_string)
    for char in s:
        if char == 'c' or char == 'C':
            s.remove(char)
    return("".join(s))
