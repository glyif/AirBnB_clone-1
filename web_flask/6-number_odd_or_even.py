#!/usr/bin/python3
"""
c is fun
"""

from flask import Flask, abort, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """
    hello world
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    displays hbnb
    """
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """
    c <text>
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """
    Python <text> or "is cool"
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<n>")
def is_number(n):
    """
    displays only if integer
    """
    try:
        return ("{} is a number".format(int(n)))
    except:
        abort(404)


@app.route("/number_template/<n>")
def number_template(n):
    """
    renders number template
    """
    try:
        number = int(n)
        return render_template("5-number.html", number=n)
    except:
        abort(404)


@app.route("/number_odd_or_even/<n>")
def even_odd(n):
    """
    even or odd
    """
    try:
        number = int(n)
        if number % 2:
            return render_template("6-number_odd_or_even.html", number=n, position="odd")
        return render_template("6-number_odd_or_even.html", number=n, position="even")
    except:
        abort(404)

if __name__ == "__main__":
    app.run("0.0.0.0", "5000")
