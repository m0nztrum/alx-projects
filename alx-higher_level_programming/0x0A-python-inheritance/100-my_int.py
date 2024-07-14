#!/usr/bin/python3
"""contains class MyInt"""


class MyInt(int):
    """Invert the int operator == and !="""

    def __equ__(self, value):
        """inverts the int operator == with !="""
        return int(self) != value

    def __nequ__(self, value):
        """inverts the int operator != with =="""
        return int(self) == value
