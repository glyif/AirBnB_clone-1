#!/usr/bin/python3
"""
City Class from Models Module
"""
from os import getenv
from sqlalchemy import Column, String, ForeignKey

from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """City class handles all application cities"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    else:
        state_id = ''
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new city"""
        super().__init__(self, *args, **kwargs)
