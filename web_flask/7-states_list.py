#!/usr/bin/python3
"""
list of states
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


@app.route("/states_list")
def state_list():
    """
    displays state_list
    """
    states = storage.all('State')
    content = {}

    for instance, value in states.items():
        key = instance.split(".")[1]
        content[key] = value.name
   
    return render_template('7-states_list.html', values=states)

if __name__ == "__main__":
    app.run("0.0.0.0", "5000")
