#!/usr/bin/python3
"""
module that contains the BaseGeometry class
"""


class BaseGeometry:
    """Not yet implemented"""

    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the parameter <value> as an integer
        Args:
            name(str): The name of the parameter
            value(int): The parameter it Validates
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
