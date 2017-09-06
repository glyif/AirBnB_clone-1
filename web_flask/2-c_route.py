#!/usr/bin/python3
"""
c is fun
"""

from flask import Flask

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


if __name__ == "__main__":
    app.run("0.0.0.0", "5000")
