from flask import Blueprint, request, jsonify
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Validate price
    if not (1 <= price <= 30):
        return jsonify({ "errors": ["Price must be between 1 and 30"] }), 400

    # Validate restaurant and pizza exist
    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not pizza or not restaurant:
        return jsonify({ "errors": ["Pizza or Restaurant not found"] }), 400

    new_link = RestaurantPizza(
        price=price,
        pizza_id=pizza_id,
        restaurant_id=restaurant_id
    )

    db.session.add(new_link)
    db.session.commit()

    return jsonify({
        'id': new_link.id,
        'price': new_link.price,
        'pizza_id': new_link.pizza_id,
        'restaurant_id': new_link.restaurant_id,
        'pizza': {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        },
        'restaurant': {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
    }), 201
