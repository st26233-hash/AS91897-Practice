from flask import Flask, render_template, request

app = Flask(__name__)

# Creating cart list
cart = []

# Pizza data
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

# Topping and size price data
sizes = {
    "Medium": 0.00,
    "Large": 3.00
}

topping_prices = {
    "Pepperoni": 2.00,
    "Mushrooms": 1.50,
    "Olives": 1.50
}


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Menu page
@app.route("/menu")
def menu():
    return render_template("menu.html", pizzas=pizzas)


# Customise page
@app.route("/customise/<int:pizza_id>", methods=["GET", "POST"])
def customise(pizza_id):

    for pizza in pizzas:
        if pizza["id"] == pizza_id:

            if request.method == "POST":
                size = request.form["size"]
                selected_toppings = request.form.getlist("topping")
                quantity = int(request.form["quantity"])

                # Calculate the price of one pizza
                price = pizza["price"]
                price = price + sizes[size]

                for topping in selected_toppings:
                    price = price + topping_prices[topping]

                # Calculate the total for the quantity
                total = price * quantity

                # Create a cart item
                item = {
                    "pizza": pizza,
                    "size": size,
                    "toppings": selected_toppings,
                    "quantity": quantity,
                    "total": total
                }

                # Add the item to the cart
                cart.append(item)

                # Calculate the cart total
                cart_total = 0

                for item in cart:
                    cart_total = cart_total + item["total"]

                return render_template(
                    "cart.html",
                    cart=cart,
                    cart_total=cart_total
                )

            return render_template("customise.html", pizza=pizza)

    return "Pizza not found", 404


# Cart route
@app.route("/cart")
def view_cart():
    cart_total = 0

    for item in cart:
        cart_total = cart_total + item["total"]

    return render_template(
        "cart.html",
        cart=cart,
        cart_total=cart_total
    )

# Checkout page
@app.route("/checkout", methods=["GET", "POST"])
def checkout():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        return render_template(
            "confirmation.html",
            name=name,
            email=email,
            phone=phone,
            cart=cart
        )
    return render_template("checkout.html")

# Remove item from cart
@app.route("/remove/<int:item_id>")
def remove_item(item_id):

    if item_id >= 0 and item_id < len(cart):
        cart.pop(item_id)

    cart_total = 0

    for item in cart:
        cart_total = cart_total + item["total"]

    return render_template(
        "cart.html",
        cart=cart,
        cart_total=cart_total
    )

# Running website
if __name__ == "__main__":
    app.run(debug=True)