#!/usr/bin/python3
"""Airbnb base model"""
from datetime import datetime, date, time
import uuid
import json
import os

class BaseModel:
    """the class of Airbnb Base Model"""


    def __init__(self, *args, **kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        attr_list = ["id", "created_at", "updated_at", "name", "my_number"]
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                for i in range(len(attr_list)):
                    if k == attr_list[i] and (k == "created_at" or k == "updated_at"):
                        setattr(self, attr_list[i], datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                    elif k == attr_list[i]:
                        setattr(self, attr_list[i], v)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance"""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = str(type(self).__name__)
        for k in instance_dict.keys():
            if k == "created_at":
                instance_dict[k] = str(instance_dict[k].isoformat())
            if k == "updated_at":
                instance_dict[k] = str(instance_dict[k].isoformat())
        return instance_dict

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)