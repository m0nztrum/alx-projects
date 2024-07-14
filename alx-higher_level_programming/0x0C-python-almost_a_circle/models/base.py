#!/usr/bin/python3
"""module that contains the class Base"""
import json


class Base:
    """class Base is the base for all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Method that assigns the public instance attribute
        Args:
            id : is an integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns the JSON
           string representation
        Args:
           list_dictionaries(dict): List of dictionaries
        Return:
           JSON string
        """
        if list_dictionaries is None or bool(list_dictionaries) is False:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes the JSON string representation
            of list_objs to a file
        Args:
            list_objs(list): List of objects
        Return:
            Always nothing
        """
        filename = "{}.json".format(cls.__name__)
        list_dictionaries = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                list_dictionaries.append(dictionary)
            json_string = Base.to_json_string(list_dictionaries)
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list of the
           JSON string representation
        Args:
           json_string: JSON string
        Return:
           Python object
        """
        if json_string is None or bool(json_string) is False:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Update the class Base and returns a instance with all
           attributes already set
        Args:
           dictionary: Dictionary with all attributes of the object
        Return:
           A instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Method that returns a list of instances
        - the type of these instances depends on cls
        """
        filename = "{}.json".format(cls.__name__)
        instance_list = []
        try:
            with open(filename, "r") as f:
                json_string = f.read()
                dictionary_list = cls.from_json_string(json_string)
                for item in dictionary_list:
                    instance = cls.create(**item)
                    instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list
