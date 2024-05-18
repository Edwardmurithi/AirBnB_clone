#!/usr/bin/python3
"""
This is the Base Model
"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel"""

        t_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
             for key, value in kwargs.items():
                 if key == "__class__":
                     continue
                 elif key in ["created_at", "updated_at"]:
                     setattr(self, key, datetime.strptime(value, t_format))
                 else:
                     setattr(self, key, value)
        
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at


    def __str__(self):
        """Returns a string representation of the instance"""
        class_name = self.__class__.__name__
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute"""
        self.update_at = datetime.utcnow()

    def to_dict(self):
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep
