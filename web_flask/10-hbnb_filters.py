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


@app.route("/hbnb_filters")
def hbnb_filters():
    """
    hbnb filters
    """
    return render_template('10-hbnb_filters.html',
                           states=storage.all("State"),
                           amenities=storage.all("Amenity"))

if __name__ == "__main__":
    app.run("0.0.0.0", "5000")
