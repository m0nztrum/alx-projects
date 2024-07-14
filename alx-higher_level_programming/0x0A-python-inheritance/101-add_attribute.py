#!/usr/bin/python3
"""module containing a function that adds attributes to objects"""


def add_attributes(obj, att, value):
    """Add a new attribute to object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attributes")
    setattr(obj, att, value)
