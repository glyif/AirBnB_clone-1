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


@app.route("/cities_by_states")
def state_list():
    """
    displays cities by states
    """
    states = storage.all("State")

    return render_template("8-cities_by_states.html", values=states)

if __name__ == "__main__":
    app.run("0.0.0.0", "5000")
