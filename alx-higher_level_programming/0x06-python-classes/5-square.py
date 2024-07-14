#!/usr/bin/python3
"""A python module that defines a square"""


class Square:
    """Square with a private object attribute size"""

    def __init__(self, size=0):
        """
        Args:
            size: size of square
        Returns:
            TypeError: if the size is not an integer
            ValueError: if the size is less than zero
        """
        self.size = size

    def area(self):
        """finds area of Square
        Returns: the area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """property to retrieve the private object __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for the private object __size
        Returs: None
        """
        if type(value) is not int:
            raise TypeError("size must be an int")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """prints the square in stdout with character #
        Returns:
            Nothing
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
