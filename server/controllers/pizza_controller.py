from flask import Blueprint, jsonify, request
from server.models.pizza import Pizza
from server.app import db

pizza_bp = Blueprint('pizzas', __name__)

@pizza_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([
        { 'id': p.id, 'name': p.name, 'ingredients': p.ingredients }
        for p in pizzas
    ])

@pizza_bp.route('/pizzas', methods=['POST'])
def create_pizza():
    data = request.get_json()

    if not data.get('name') or not data.get('ingredients'):
        return jsonify({ "errors": ["Name and ingredients are required."] }), 400

    new_pizza = Pizza(name=data['name'], ingredients=data['ingredients'])
    db.session.add(new_pizza)
    db.session.commit()

    return jsonify({
        "id": new_pizza.id,
        "name": new_pizza.name,
        "ingredients": new_pizza.ingredients
    }), 201
