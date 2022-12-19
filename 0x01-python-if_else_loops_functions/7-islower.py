#!/usr/bin/python3
# 7-islower.py
# Felix-Muraguri <felixmuraguri@gmail.com>

def islower(c):
    """Check for lowercase charactes."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
