from flask import request, Blueprint, jsonify, abort
from server.models.restaurant import Restaurant
from server.app import db



restaurant_bp = Blueprint('restaurants', __name__)

@restaurant_bp.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.get_json()
    name = data.get('name')
    address = data.get('address')

    if not name or not address:
        return jsonify({"errors": ["Name and address are required"]}), 400

    new_restaurant = Restaurant(name=name, address=address)
    db.session.add(new_restaurant)
    db.session.commit()

    return jsonify({
        "id": new_restaurant.id,
        "name": new_restaurant.name,
        "address": new_restaurant.address
    }), 201
