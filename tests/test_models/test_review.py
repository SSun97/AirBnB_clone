#!/usr/bin/python3
"""test the airbnb project"""


import unittest
from models.review import Review

A = Review()


class TestClassMethods(unittest.TestCase):
    """test the Airbnb project"""

    def test_State_Amenity(self):
        self.assertEqual(type(A.place_id), str)
        self.assertEqual(type(A.user_id), str)
        self.assertEqual(type(A.text), str)