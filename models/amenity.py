#!/usr/bin/python3
"""a class city that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """State class to inherit BaseModel"""
    name = ''

    def __init__(self, **kwargs):
        super().__init__()