#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""

import json
import models
from os import getenv, environ
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


now = datetime.now
strptime = datetime.strptime

if getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """attributes and functions for BaseModel class"""

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime(),
                            nullable=False,
                            default=datetime.utcnow)
        updated_at = Column(DateTime(),
                            nullable=False,
                            default=datetime.utcnow,
                            onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """instantiation of new BaseModel Class"""
        self.id = str(uuid4())
        self.created_at = now()
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        models.storage.new(self)

    def __is_serializable(self, obj_v):
        """checks if object is serializable"""
        try:
            nada = json.dumps(obj_v)
            return True
        except:
            return False

    def bm_update(self, name, value):
        setattr(self, name, value)
        self.save()

    def save(self):
        """updates attribute updated_at to current time"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_json(self):
        """returns json representation of self"""
        bm_dict = {}
        for k, v in (self.__dict__).items():
            if (self.__is_serializable(v)):
                bm_dict[k] = v
            else:
                bm_dict[k] = str(v)
        bm_dict["__class__"] = type(self).__name__
        bm_dict.pop("_sa_instance_state", None)
        return(bm_dict)

    def __str__(self):
        """returns string type representation of object instance"""
        cname = type(self).__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)

    def delete(self):
        """delete method"""
        models.storage.delete(self)
