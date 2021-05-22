#!/usr/bin/python3
"""a class state that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class to inherit BaseModel"""
    name = ''

    def __init__(self, **kwargs):
        super().__init__()
