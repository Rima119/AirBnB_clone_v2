#!/usr/bin/python3
"""This module defines a class User"""
<<<<<<< HEAD
from models.base_model import Base
from sqlalchemy import Column, String


class User(Base):
=======
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
>>>>>>> cb7fc0205f8d7044872332ebc53e091381aa38c7
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
