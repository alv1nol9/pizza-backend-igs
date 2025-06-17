from server.app import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String)

    restaurant_pizzas = db.relationship(
        'server.models.restaurant_pizza.RestaurantPizza',
        back_populates='restaurant',
        cascade='all, delete-orphan'
    )
