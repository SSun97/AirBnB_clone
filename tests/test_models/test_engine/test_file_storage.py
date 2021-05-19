#!/usr/bin/python3
"""test the airbnb project"""
import json
import unittest
from os import remove
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime

storage1 = FileStorage()
class TestFileStorageClass(unittest.TestCase):
    """test the Airbnb project"""

    def test_File_storage(self):
        self.assertTrue(type(storage1._FileStorage__file_path) is str)
        self.assertTrue(type(storage1._FileStorage__objects) is dict)

    def test_all(self):
        """ Tests for new method """
        tmp = storage1.all().copy()
        n = BaseModel()
        self.assertFalse(tmp == storage1.all())

    def test_functions(self):
        dic1 = storage1.all().copy()
        nb = BaseModel()
        nb.save()
        dic2 = storage1.all()
        self.assertTrue(type(dic1) is dict)
        self.assertTrue(dic1, dic2)
    def test_save(self):
        try:
            remove("file.json")
        except:
            pass
        nb = BaseModel()
        nb.save()
        storage1.save()
        FileStorage.save(self)
        with open("file.json") as f:
            dict1 = json.load(f)
            self.assertTrue(type(dict1), dict)

    def test_safe_self(self):
        FileStorage.save(self)
        with open("file.json") as f:
            dict1 = json.load(f).copy()
        nb = BaseModel()
        FileStorage.save(self)
        FileStorage.reload(self)
        with open("file.json") as f:
            dict2 = json.load(f)
        self.assertNotEqual(dict1, dict2)


    def test_reload(self):
        try:
            remove("file.json")
        except:
            pass
        storage2 = FileStorage()
        storage2.save()
        storage2.reload()
        dict1 = storage2.all()
        self.assertEqual(dict1, storage1.all())




if __name__ == '__main__':
    unittest.main()