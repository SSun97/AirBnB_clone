#!/usr/bin/python3
"""a class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class to inherit BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, **kwargs):
        super().__init__()

    # def __str__(self):
    #     return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

