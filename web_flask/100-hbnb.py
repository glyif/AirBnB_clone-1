#!/usr/bin/python3
"""
cities by state
"""

from flask import Flask, abort, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """
    tear down, closes storage
    """
    storage.close()


@app.route("/hbnb")
def hbnb_home():
    """
    hbnb filters
    """
    return render_template('100-hbnb.html',
                           states=storage.all("State"),
                           amenities=storage.all("Amenity"),
                           places=storage.all("Place"),
                           users=storage.all("User"))

if __name__ == "__main__":
    app.run("0.0.0.0", "5000")
