#!/usr/bin/python3
"""Airbnb base model"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """the class of Airbnb Base Model"""

    def __init__(self, **kwargs): # A = BaseModel(id = 123134, created_at = 2021)

        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    if k != "__class__":
                        setattr(self, k, v)
        else:
            # obj = {"{}.{}".format(type(self).__class__.__name__, self.id): self}
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""

        self.updated_at = datetime.now()
        models.storage.save()

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
