#!/usr/bin/python3
# 8-uppercase.py
# Felix-Muraguri <felixmuraguri@gmail.com>

def uppercase(str):
    """Print a string in uppercase."""
    for i in range(len(str)):
        uni_code = ord(str[i])
        if uni_code >= 97 and uni_code <= 122:
            uni_code = uni_code - 32
            print ("{}". format(che(uni_code)), end='')
            print ()


