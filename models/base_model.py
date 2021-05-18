#!/usr/bin/python3
"""Airbnb base model"""
from datetime import datetime, date, time
import uuid
import json
import os

class BaseModel:
    """the class of Airbnb Base Model"""


    def __init__(self):
        self.create_at = datetime.now()
        self.update_at = datetime.now()
        self.id = str(uuid.uuid4())

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""

        self.update_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = str(type(self).__name__)
        for k in instance_dict.keys():
            if k == "create_at":
                instance_dict[k] = instance_dict[k].isoformat()
            if k == "update_at":
                instance_dict[k] = self.update_at.isoformat()
        return instance_dict



    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)




my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
