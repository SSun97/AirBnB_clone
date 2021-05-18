#!/usr/bin/python3
"""test the airbnb project"""


import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime
#from models.base_model import Rectangle
# from models.square import Square

class TestClassMerthods(unittest.TestCase):
    """test the Airbnb project"""

    def test_BaseModel_id(self):
        self.assertEqual(type(BaseModel().genarate_id()), uuid.UUID)

    def test_create_time(self):
        self.assertEqual(type(BaseModel().create_at()), datetime)











if __name__ == '__main__':
    unittest.main()

