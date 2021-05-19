#!/usr/bin/python3
"""test the airbnb project"""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime

storage1 = FileStorage()
class TestFileStorageClass(unittest.TestCase):
    """test the Airbnb project"""

    def test_File_storage(self):
        self.assertTrue(type(storage1._FileStorage__file_path) is str)
        self.assertTrue(type(storage1._FileStorage__objects) is dict)

    def test_functions(self):
        dic1 = storage1.all().copy()
        nb = BaseModel()
        nb.save()
        dic2 = storage1.all()
        self.assertTrue(type(dic1) is dict)
        self.assertTrue(dic1, dic2)
