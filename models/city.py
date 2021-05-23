#!/usr/bin/python3
"""a class city that inherits from BaseModel"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """State class to inherit BaseModel"""
    state_id = ''
    name = ''

    def __init__(self, **kwargs):
        super().__init__()
