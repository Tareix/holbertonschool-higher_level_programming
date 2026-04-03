#!/usr/bin/python3
"""Module for Square class."""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with # using position."""
        if self.__size == 0:
            print("")
            return

        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
