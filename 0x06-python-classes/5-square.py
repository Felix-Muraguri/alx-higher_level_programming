#!/usr/bin/python3
"""Write a class square that defines a square based on 4-square.py."""

class Square:
    """Square class with a private attribute - size."""

    def __init__(self, size=0):
        """Initializes the size variable as a private instance attribute.
        Args: 
             size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
            """Instantiation with optional size of square."""
            return self.__size

    @size.setter
    def size(self, value):
            """Gets the size of the square."""
            if not isinstance(size_value, int):
                raise TypeError("size must be an integer")
            elif size_value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    def area(self):
            """Returns the current square area."""
            return (self.__size * self.__size)

    def my_print(self):
            """Prints in stdout the square with the character '#'"""
            for i in range(0, self.__size):
                [print("#", end="") for i in range(self.size)]
                print("")
            if self.size == 0:
                    print("") 
