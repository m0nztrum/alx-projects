#!/usr/bin/python3
"""module that contains class Rectanglele inheriting from Base(models.base)"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method that initiates the values for the rectangle object
        Args:
            width: the widht size
            height: the height size
            x: variable x
            y: variable y
        Return:
            returns nothing"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # The getter and setter for the width
    @property
    def width(self):
        """The getter size of the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter size of the width
        Args:
            value: size to assign to the width
        Return:
            returns nothing
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    # The getter and setter for the height
    @property
    def height(self):
        """The getter of the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter size of the height
        Args:
            value: size to assign to the height
        Return:
            returns nothing"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    # The getter and setter of the x variable
    @property
    def x(self):
        """The getter of the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """the setter of the x variable
        Args:
            value to assign to the x variable
        Return:
            returns nothing"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    # The getter and setter for the y variable
    @property
    def y(self):
        """The getter of the x"""
        return self.__y

    @y.setter
    def y(self, value):
        """the setter of the x variable
        Args:
            value to assign to the x variable
        Return:
            returns nothing"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """method for printing the area of a rectangle
        Args:
            No arguments
        Return:
            the area value of a rectangle instance
        """
        return self.width * self.height

    def display(self):
        """method that prints to stdout
        Rectangle object with the character "#"
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + self.width * "#")

    def __str__(self):
        """Method that overwrites the str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Method that assigns an argument to each attribute
        Args:
            *args: list of arguments
            **kwargs: Dictionary with arguments
        Return:
            Always nothing"""
        dict_order = ["id", "width", "height", "x", "y"]
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
        """Method that returns a dictionary with
        attributes of the object.
        """
        dict_order = ["x", "y", "id", "height", "width"]
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
