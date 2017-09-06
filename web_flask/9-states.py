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


@app.route("/states")
def state_list():
    """
    displays cities by states
    """
    states = storage.all("State")

    return render_template("9-states.html", states=states, header="States")


@app.route("/states/<id>")
def spec_state(id):
    """
    specific state
    """
    try:
        states = storage.all("State")
        state = []
        for obj in states.values():
            if str(obj.id) == id:
                state.append(obj)
        header = "State: {}".format(state[0].name)
        return render_template('9-states.html', states=state, header=header)
    except:
        state = []
        header = "Not found!"
        return render_template('9-states.html', states=state, header=header)



if __name__ == "__main__":
    app.run("0.0.0.0", "5000")
