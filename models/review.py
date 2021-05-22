#!/usr/bin/python3
"""a class city that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """State class to inherit BaseModel"""

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, **kwargs):
        super().__init__()