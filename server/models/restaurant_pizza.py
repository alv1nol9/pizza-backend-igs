from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from models import Base
 
class RestaurantPizza(Base):
    __tablename__ = 'restaurant_pizzas'

    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)

    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)
    pizza_id = Column(Integer, ForeignKey('pizzas.id'), nullable=False)

    restaurant = relationship('Restaurant, back_populates="restaurant_pizzas')
    pizza = relationship('Pizza', back_populates="restaurant_pizzas")
    
    __table_args__ = (
        CheckConstraint{'price >= 1 AND price <= 30', name="check_price_between_1_and_30"},
    )