#!/usr/bin/python3
# 101-remove_chat_at.py
# Felix-Muraguri <felixmuraguri@gmail.com>

def remove_char_at(str, n):
    """Create a copy of the string without the character at position n."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])

