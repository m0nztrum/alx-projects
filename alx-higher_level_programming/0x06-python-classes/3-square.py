#!/usr/bin/python3


class Square:
    """Square with a private object attribute size"""

    def __init__(self, size=0):
        """
        Args:
            size: size of square
        Raises:
            TypeError: if the size is not an integer
            ValueError: if the size is less than zero
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculates the area of Square
        Returns: the area of the square
        """

        return self.__size**2
