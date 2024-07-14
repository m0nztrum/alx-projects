#!/usr/bin/python3
"""This is a module that divides elements of a matrix"""


def matrix_divided(matrix, div):
    """This function devides all the elements of a matrix by a given number
    Args:
        matrix: a list of integers or floats type variables
        div: number to be used for division(can be a float or integer)
    Raises:
        TypeError: If the matrix contains non-numbers or rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If the div is 0
    Returns: A new matrix which represents the result of the divisions
    """
    error_mess = "matrix must be a matrix(list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_mess)
    len_rows = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_mess)
        len_rows.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_mess)
        row_count += 1
        if len(set(len_rows)) > 1:
            raise TypeError("Each row of the matrix must have the same size")
        if type(div) not in [int, float]:
            raise TypeError("div must be a number")
        if int(div) == 0:
            raise ZeroDivisionError("division by zero")
        new_matrix = list(
            map(lambda row: list(map(lambda x: round(x / div, 2), row)), matrix)
        )
        return new_matrix
