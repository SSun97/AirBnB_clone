#!/usr/bin/python3
"""test the airbnb project"""


import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import json
from os import remove, path

from models.user import User

A = User()


class TestClassMethods(unittest.TestCase):
    """test the Airbnb project"""

    def test_user_email(self):
        self.assertTrue(hasattr(User, 'email'))
        self.assertEqual(type(A.email), str)


    def test_user_password(self):
        self.assertTrue(hasattr(User, 'password'))
        self.assertEqual(type(A.password), str)

    def test_user_first_name(self):
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertEqual(type(A.first_name), str)

    def test_user_last_name(self):
        self.assertTrue(hasattr(User, 'last_name'))
        self.assertEqual(type(A.last_name), str)




if __name__ == '__main__':
    unittest.main()

