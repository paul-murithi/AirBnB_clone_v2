#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models


class Amenity(BaseModel, Base):
    """Class Amenity
    Attributes:
             name (String): nme of amenity
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    # place_amenities = relationship('Place', secondary='place_amenity')
