#!/usr/bin/python3
"""a class city that inherits from BaseModel"""
from models.base_model import BaseModel
from models.city import City
from models.user import User


class Place(BaseModel):
    """State class to inherit BaseModel"""
    name = ''
    city_id = ''
    user_id = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, **kwargs):
        super().__init__()