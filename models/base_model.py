#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """Initializes a new instance of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute"""
        self.update_at = datetime.now()

    def to_dict(self):
        dict_representation = self.__dict__.copy()
        dict_representation["__class__"] = self.__class__.__name__
        dict_representation["created_at"] = self.created_at.isoformat()
        dict_representation["updated_at"] = self.updated_at.isoformat()
        return dict_representation
