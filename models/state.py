#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import models
from models.city import City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="State",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """getter attribute cities that returns the list"""
        city_list = []
        for city in models. storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
