#!/usr/bin/python3
"""a class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class to inherit BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        super().__init__()
