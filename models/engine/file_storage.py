#!/usr/bin/python3
"""Doc"""
import json
import os


class FileStorage:
    """store the information of airbnb"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return __object dictionary"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        self.__objects.update(obj)

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        json_string = json.dumps(self.__objects)
        with open(self.__file_path, "w") as f:
            f.write(json_string)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
            otherwise, do nothing. If the file does not exist, no exception should be raised)
        """

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        else:
            pass