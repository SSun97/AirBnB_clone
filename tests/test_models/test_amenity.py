#!/usr/bin/python3
"""test the airbnb project"""


import unittest
from models.amenity import Amenity


A = Amenity()


class TestClassMethods(unittest.TestCase):
    """test the Airbnb project"""

    def test_State_Amenity(self):
        self.assertEqual(type(A.name),str)