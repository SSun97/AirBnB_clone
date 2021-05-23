#!/usr/bin/python3
"""test the airbnb project"""


import unittest
from models.state import State

A = State()


class TestClassMethods(unittest.TestCase):
    """test the Airbnb project"""

    def test_State_attr(self):
        self.assertEqual(type(A.name), str)