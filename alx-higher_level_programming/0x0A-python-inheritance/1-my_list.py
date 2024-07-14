#!/usr/bin/python3
"""The mylist class"""


class MyList(list):
    """Inherits from list class"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
