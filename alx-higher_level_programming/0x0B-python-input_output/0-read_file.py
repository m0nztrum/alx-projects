#!/usr/bin/python3
"""
write a function that reads a text file (UTF8 encoding) and prints to stdout
"""


def read_file(filename=""):
    """Print the contents of a UTF text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
