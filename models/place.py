#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import models


place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column("place_id", String(60), ForeignKey(
            'places.id'), primary_key=True),
        Column("amenity_id", String(60), ForeignKey(
            'amenities.id'), primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', backref='place')
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)
    amenity_ids = []

    @property
    def reviews(self):
        """Returns the list of Review instances."""
        from models.review import Review

        review_list = []
        all_reviews = models.storage.all(Review)
        for review in all_reviews.values():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list

    @property
    def amenities(self):
        """Returns the list of Amenities instances"""
        from models.amenity import Amenity

        amenity_list = []
        all_amenities = models.storage.all(Amenity)
        for amenity in all_amenities.values():
            if amenity.place_id == self.id:
                amenity_list.append(amenity)
        return amenity_list

    @amenities.setter
    def amenities(self, obj):
        """set amenity"""
        from models.amenity import Amenity

        if type(obj) is not Amenity:
            return
        self.amenity_ids.append(obj.id)
