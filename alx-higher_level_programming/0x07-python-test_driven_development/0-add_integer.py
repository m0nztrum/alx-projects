#!/usr/bin/python3
"""
This is the add integer module
The 0-add_integer give us one function add_integer
"""


def add_integer(a, b=98):
    """Return the addition of two integers"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        return TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
