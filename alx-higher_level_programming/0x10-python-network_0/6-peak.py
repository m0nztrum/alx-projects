#!/usr/bin/python3
"""Module containing funtion find_peak"""


def find_peak(list_of_integers):
    """Funtion that finds a peak in an unsorted
    list of integers
    """
    left = 0
    right = len(list_of_integers) - 1
    if len(list_of_integers) == 0:
        return None

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
