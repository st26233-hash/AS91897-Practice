# importing flask

from flask import Flask, render_template

app = Flask(__name__)

# collection of pizza data

pizzas = [
    {
        "id": 1,
        "name": "Margherita",
        "description": "Tomato sauce, mozzarella and basil",
        "price": 14.00
    },
    {
        "id": 2,
        "name": "Pepperoni",
        "description": "Tomato sauce, mozzarella and pepperoni",
        "price": 16.00
    },
    {
        "id": 3,
        "name": "Meat Lovers",
        "description": "Tomato sauce, mozzarella, beef, ham and pepperoni",
        "price": 19.00
    },
    {
        "id": 3,
        "name": "Vegetarian",
        "description": "Tomato sauce, mozzarella, mushrooms, capsicum and onion",
        "price": 17.00
    },
    {
        "id": 4,
        "name": "BBQ Chicken",
        "description": "BBQ sauce, mozzarella, chicken and onion",
        "price": 19.00
    }
]

@app.route("/")
def home():
    """Display the home page."""
    return render_template("index.html")

# Displays the menu when navigating to /menu

@app.route("/menu")
def menu():
    """Display the pizza menu."""
    return render_template("menu.html", pizzas=pizzas)


if __name__ == "__main__":
    app.run(debug=True)

# displaying menu.html at menu page

@app.route("/menu")
def menu():
    """Display the pizza menu."""
    return render_template("menu.html")

# customisation form route

 @app.route("/customise/<int:pizza_id>", methods=["GET", "POST"])
def customise(pizza_id):
    """Display and process pizza customisation."""

    for pizza in pizzas:
        if pizza["id"] == pizza_id:

            if request.method == "POST":
                size = request.form["size"]
                toppings = request.form.getlist("topping")
                quantity = request.form["quantity"]

                print(size)
                print(toppings)
                print(quantity)

            return render_template("customise.html", pizza=pizza)

    return "Pizza not found", 404