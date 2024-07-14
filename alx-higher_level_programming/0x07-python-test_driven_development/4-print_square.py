#!/usr/bin/python3
"""
This is the print square module.
"""


def print_square(size):
    """Prints a square with "#" thas has a length of size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size > 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
