#!/usr/bin/python3
""" State Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE', '') != 'db':
        @property
        def cities(self):
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
