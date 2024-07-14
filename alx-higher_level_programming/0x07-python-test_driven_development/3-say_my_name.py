#!/usr/bin/python3
""""
This module contains a function that prints a name
"""


def say_my_name(first_name, last_name=""):
    """This function prints name (<first name> <last name>)
    Args:
        first_name (str): The fisrt name to be printed
        last_name (str): The last name to be printed
    Raises:
        TypeError: If either the first_name and last_name are not strings
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
