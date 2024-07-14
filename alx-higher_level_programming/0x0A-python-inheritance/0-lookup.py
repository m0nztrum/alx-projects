#!/usr/bin/python3
"""Python module that contains the lookup function"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    return dir(obj)
