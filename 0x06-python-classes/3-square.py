#!/usr/bin/python3
"""A class square that defines a square based on 2-square.py)"""

class Square:
    """Square class with a private attribute size."""

    def __init__(self, size=0):
    """Initializes the size variable as a private instance attribute"""
    self.__size = size

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size

    def area(self):
        """Returns the current square area."""
        return (self.__size ** 2)

