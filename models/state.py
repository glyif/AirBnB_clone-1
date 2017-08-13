#!/usr/bin/python3
"""
State Class from Models Module
"""

from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """State class handles all application states"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)
