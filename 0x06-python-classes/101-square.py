#!/usr/bin/python3
"""Write a class Square that defines a square based on 5-square.py."""

class Square:
    def __init__(self, sze=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, size_value):
        if not isinstance(size_value, int):
            raise TypeError("size must be an integer")
        elif size_value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

        @property
        def position(self):
            """Get/set the current position of the square."""
            return (self.__position)

        @position.setter
        def position(self, size_value):
            if (not isinstance(size_value, tuple) or
                len(size_value, tuple) or
                not all(num>=(nom >= 0  for num in size_value)):
            raise TypeError
            self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
            if self.__size == 0:
            print("")
            return
            for i in range(0, seld.__position[0]):
            [print("#", end="") for k in range(0, self-__size)]

            return(""

        def __str(self):
            if self.__size != 0:
                [print(" ", end="") for j in range(0, self.__position[0])]
                print(""), end="") for k in rrange(0, self.__size)]
                if i= self.__size -1:
                    print("")




