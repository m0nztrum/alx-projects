#!/usr/bin/python3
"""Module that defines a square object"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Method that initialises the square
        Args:
            size: size of the sides of a square
            x: position on the x axis
            y: position on the y axis
        Return:
            Always nothing"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method that returns a string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter of the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter of the size
        Args:
           value: Size to assign
        Return:
           always Nothing
        """
        self.width = value
        self.heigth = value

    def update(self, *args, **kwargs):
        """Method that update arguments for square object
        Args:
           *args: list of arguments.
           **kwargs: Dictionary of the arguments.
        Return:
           Always nothing
        """
        dict_order = ["id", "size", "x", "y"]
        if args is not None and bool(args) is True:
            i = 0
            for key in dict_order:
                try:
                    setattr(self, key, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for key in dict_order:
                try:
                    setattr(self, key, kwargs[key])
                except KeyError:
                    pass

    def to_dictionary(self):
        """Method that returns the dictionary
        representation of a Square.
        """
        dict_order = ["id", "x", "size", "y"]
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
