# importing flask

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Display the home page."""
    return render_template("index.html")

# Displays the menu when navigating to /menu

@app.route("/menu")
def menu():
    """Display the pizza menu."""
    return render_template("menu.html")


if __name__ == "__main__":
    app.run(debug=True)

# displaying menu.html at menu page

@app.route("/menu")
def menu():
    """Display the pizza menu."""
    return render_template("menu.html")