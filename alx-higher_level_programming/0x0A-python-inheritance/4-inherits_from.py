#!/usr/bin/python3
"""module that contains the inherits_from function"""


def inherits_from(obj, a_class):
    """returns true if the object is subclass of a_class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
