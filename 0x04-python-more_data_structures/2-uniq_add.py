#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add all unique integers in a list (once for each integer)."""
    new_list = []
    sum = 0
    for num in my_list:
        if num not in new_list:
            sum += num
            new_list.append(num)
            return sum
