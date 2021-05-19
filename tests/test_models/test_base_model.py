#!/usr/bin/python3
"""test the airbnb project"""


import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import json
from os import remove, path

class TestClassMerthods(unittest.TestCase):
    """test the Airbnb project"""

    def test_BaseModel_id(self):
        self.assertEqual(type(BaseModel().id), str)

    def test_create_time(self):
        self.assertEqual(type(BaseModel().created_at), datetime)

    def test_save(self):
        nb = BaseModel()
        nb.save()
        t1 = nb.updated_at
        nb.save()
        nb.save()
        nb.save()
        nb.save()
        t2 = nb.updated_at
        self.assertNotEqual(t1, t2)

    def test_save2(self):
        """ Tests for save method """

        nb = BaseModel()
        date_string = nb.updated_at
        nb.save()
        nb.save()
        nb.save()
        nb.save()
        nb.save()
        self.assertFalse(nb.updated_at == date_string)
        remove("file.json")
        nb.save()

        self.assertTrue(path.exists("file.json"))

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

    def test_to_dict(self):
        nb = BaseModel()
        dict1 = nb.to_dict()
        nb2 = BaseModel(**dict1)
        dict2 = nb2.to_dict()
        self.assertEqual(dict1, dict2)
        self.assertTrue(type(dict1) is dict)
        self.assertEqual(dict1["__class__"], "BaseModel")
        self.assertTrue(type(dict1["created_at"]) is str)


    def assertHasAttr(self):
        testBool = hasattr(BaseModel(), 'save()')
        self.assertTrue(testBool)









if __name__ == '__main__':
    unittest.main()

