from models import Base

class Pizza(Base):
    __tablename__ = 'pizzas'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    indgredients = Column(String)

    restaurant_pizzas = relationship(
        "RestaurantPizza",
        back_populates='pizza',
        cascade="all, delete-orphan"
    )