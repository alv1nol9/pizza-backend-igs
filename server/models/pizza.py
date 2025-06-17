from server.app import db

class Pizza(db.Model):
    __tablename__ = 'pizzas'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String)

    restaurant_pizzas = db.relationship(
        'server.models.restaurant_pizza.RestaurantPizza',
        back_populates='pizza',
        cascade='all, delete-orphan'
    )
