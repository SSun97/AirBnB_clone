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
        self.assertEqual(hasattr(storage1, '__file_path'), False)
