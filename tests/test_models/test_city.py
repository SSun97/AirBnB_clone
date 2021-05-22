#!/usr/bin/python3
"""test the airbnb project"""


import unittest
from models.city import City


A = City()


class TestClassMethods(unittest.TestCase):
    """test the Airbnb project"""

    def test_State_attr(self):
        self.assertEqual(type(A.state_id), str)
        self.assertEqual(type(A.name),str)