#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list)
    new = my_list[:]
    if (idx == 0 or idx > n - 1):
        return (my_list)
    else:
        new[idx] = element
        return (new)
