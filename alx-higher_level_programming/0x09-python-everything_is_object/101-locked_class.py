#!/usr/bin/python3
"""A module that defines a locked class"""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called "first_name"
    """

    __slots__ = ["first_name"]
