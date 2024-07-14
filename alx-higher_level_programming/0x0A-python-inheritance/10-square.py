#!/usr/bin/python3
"""
Contains the class Square which is a subclass of Rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A subclass representation of a Square"""

    def __init__(self, size):
        """instantation of the Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the Square"""
        return (self.__size) ** 2
