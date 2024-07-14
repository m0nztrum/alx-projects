#!/usr/bin/python3
"""
This module contains the is_same_class
"""


def is_same_class(obj, a_class):
    """Returns True if the object is the exact an intance  a_class"""
    return type(obj) == a_class
