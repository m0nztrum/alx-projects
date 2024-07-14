#!/usr/bin/python3
"""test cases for the base.py file
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import os


class Test_Base(unittest.TestCase):
    """Class to evaluate different test cases for the base.py file"""

    def test_instance_type_id_class(self):
        """checks for the instance of the class"""
        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertFalse(type(b1) == type(Base))
        self.assertFalse(id(b1) == id(Base))
        b2 = Base()
        self.assertTrue(type(b1) == type(b2))
        self.assertFalse(id(b1) == id(b2))

    def test_none_id(self):
        """checks when id is none"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b1 = Base()
        self.assertEqual(b1.id, 3)
        b2 = Base()
        self.assertEqual(b2.id, 4)

    def test_id_value(self):
        """checking when the id has an integer value"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b1.id = 4
        self.assertEqual(b1.id, 4)
        b2 = Base(50)
        self.assertEqual(b2.id, 50)
