#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    if models._type == "db":
        __tablename__ = 'states'
        name = Column(String(28), nullable=False)
        cities = relationship('City', backref='states', cascade='delete')
    else:
        name = ""

    if models._type != 'db':
        @property
        def cities(self):
            c_list = []
            cities = storage.all(City).values()
            for city in cities:
                if ciy.state_id == self.id:
                    c_list.append(city)
            return c_list
