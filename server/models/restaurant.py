from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from server.models import Base

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

    restaurant_pizzas = relationship(
        'RestaurantPizza',
        back_populates='restaurant',
        cascade='all, delete-orphan'
    )
