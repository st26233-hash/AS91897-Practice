from flask import Flask, render_template, request

app = Flask(__name__)

# creating the cart to store pizzas
cart = []

# collection of pizza data dictionary
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
        "id": 4,
        "name": "Vegetarian",
        "description": "Tomato sauce, mozzarella, mushrooms, capsicum and onion",
        "price": 17.00
    },
    {
        "id": 5,
        "name": "BBQ Chicken",
        "description": "BBQ sauce, mozzarella, chicken and onion",
        "price": 19.00
    }
]

# toppings/sizes price data dictionary
sizes = {
    "Medium": 0.00,
    "Large": 3.00
}

topping_prices = {
    "Pepperoni": 2.00,
    "Mushrooms": 1.50,
    "Olives": 1.50
}

# routes for index menu and customise pages

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/menu")
def menu():
    return render_template("menu.html", pizzas=pizzas)

# receiving data from customise form and adding to cart, also checking if pizza exists

@app.route("/customise/<int:pizza_id>", methods=["GET", "POST"])
def customise(pizza_id):

    for pizza in pizzas:
        if pizza["id"] == pizza_id:

            if request.method == "POST":
                size = request.form["size"]
                selected_toppings = request.form.getlist("topping")
                quantity = int(request.form["quantity"])

                price = pizza["price"]
                price = price + sizes[size]

                for topping in selected_toppings:
                    price = price + topping_prices[topping]

                total = price * quantity

                item = {
                    "pizza": pizza,
                    "size": size,
                    "toppings": selected_toppings,
                    "quantity": quantity,
                    "total": total
                }

                cart.append(item)

                return render_template("cart.html", cart=cart)

            return render_template("customise.html", pizza=pizza)

    return "Pizza not found", 404


if __name__ == "__main__":
    app.run(debug=True)