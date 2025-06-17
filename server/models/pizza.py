from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import Base

class Pizza(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    indgredients = Column(String)

    restaurant_pizzas = relationship(
        "RestaurantPizza",
        back_populates='restaurant',
        cascade="all, delete-orphan"
    )