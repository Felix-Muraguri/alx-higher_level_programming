#!/usr/bin/python3

"""A class Square that defines a square based o 1-square.py)."""

class Square:
    """Square class with a private attribute size."""

    def __init__(self, size=0):
        """Initializes the size variable as a private instance attribute.

        Args:
            __size (int): The __size of the new square.
        """    
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
