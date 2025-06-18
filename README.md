# Pizza Restaurant API

A RESTful Flask API for managing pizzas, restaurants, and their price offerings.

---

##  Setup Instructions

1. **Clone the repo**

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

2. **Set up virtual environment with Pipenv**

```bash
pipenv install
pipenv shell
```

3. **Set environment variable for Flask**

```bash
export FLASK_APP=server.app:create_app
```

4. **Run the app**

```bash
flask run
```

##  Database Migration & Seeding

**(one) Initialize & migrate DB**

```bash
flask db init
flask db migrate -m "initial"
flask db upgrade
```

**(two) Seed data**

```bash
PYTHONPATH=. python server/seed.py
```

##  Routes Summary

### GET /pizzas

Returns all pizzas

### POST /pizzas

Creates a new pizza

```json
{
  "name": "BBQ Chicken",
  "ingredients": "BBQ Sauce, Chicken, Cheese"
}
```

### GET /restaurants

Returns all restaurants

### GET /restaurants/\:id

Returns one restaurant with pizzas offered

### DELETE /restaurants/\:id

Deletes a restaurant and all associated RestaurantPizzas

### POST /restaurants

Creates a new restaurant

```json
{
  "name": "New York Slice",
  "address": "789 Dough Blvd"
}
```

### POST /restaurant\_pizzas

Creates a new restaurant pizza (price entry)

```json
{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

---

## Validation Rules

### Pizza

* `name` is required and must be unique
* `ingredients` is required

### RestaurantPizza

* `price` must be between 1 and 30 (inclusive)
* `pizza_id` and `restaurant_id` must reference valid models

##  Testing with Thunder Client or Postman

* Make sure the server is running
* Use `http://127.0.0.1:5000` as the base URL
* For POST/DELETE requests, use `application/json` header

---

##  Example GET Response

### GET /restaurants/1

```json
{
  "id": 1,
  "name": "Mama's Pizza",
  "address": "123 Pizza Street",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Tomato, Mozzarella, Basil"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Tomato, Cheese, Pepperoni"
    }
  ]
}
```

---

## Error Response Example

### POST /restaurant\_pizzas with invalid price

```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

---
