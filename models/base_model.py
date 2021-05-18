#!/usr/bin/python3
"""Airbnb base model"""
from datetime import datetime, date, time
import uuid
import json
import os

class BaseModel:
    """the class of Airbnb Base Model"""


    def __init__(self):
        self.created_at = datetime.now()
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
            if k == "created_at":
                instance_dict[k] = instance_dict[k].isoformat()
            if k == "update_at":
                instance_dict[k] = self.update_at.isoformat()
        return instance_dict

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
<<<<<<< HEAD

=======
>>>>>>> b34736fdc52f03a82138517fa48bc29756ee369a
