from app import db, create_app
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import RestaurantPizza


app = create_app()

with app.app_context():
    # This is seeded data from deepseek
    Pizza.query.delete()
    RestaurantPizza.query.delete()

   
    r1 = Restaurant(name="Mama's Pizza", address="123 Pizza Street")
    r2 = Restaurant(name="Kiki's Pizza", address="456 Crust Ave")

 
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Cheese, Pepperoni")
    p3 = Pizza(name="Hawaiian", ingredients="Pineapple, Ham, Cheese")

   
    rp1 = RestaurantPizza(price=10, restaurant=r1, pizza=p1)
    rp2 = RestaurantPizza(price=12, restaurant=r1, pizza=p2)
    rp3 = RestaurantPizza(price=15, restaurant=r2, pizza=p2)
    rp4 = RestaurantPizza(price=14, restaurant=r2, pizza=p3)

    db.session.add_all([r1, r2, p1, p2, p3, rp1, rp2, rp3, rp4])
    db.session.commit()

    print("✅ Seed data inserted!")
