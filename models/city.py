#!/usr/bin/python3
"""
City Class
"""
import os
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
import models
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """get  application cities"""
    if storage_type == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities', cascade='delete')
    else:
        state_id = ''
        name = ''

    if storage_type != 'db':
        @property
        def places(self):
            """
            get place
            """
            all_places = models.storage.all("Place")
            result = []
            for obj in all_places.values():
                if str(obj.city_id) == str(self.id):
                    result.append(obj)
            return result
