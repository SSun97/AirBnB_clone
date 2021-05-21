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
class TestClassMerthods(unittest.TestCase):
    """test the Airbnb project"""

    def test_user_email(self):
        self.assertTrue(hasattr(User, 'email'))
        self.assertEqual(type(A.email), str)


    def test_user_password(self):
        self.assertTrue(hasattr(User, 'password'))

    def test_user_first_name(self):
        self.assertTrue(hasattr(User, 'first_name'))

    def test_user_last_name(self):
        self.assertTrue(hasattr(User, 'last_name'))




if __name__ == '__main__':
    unittest.main()

