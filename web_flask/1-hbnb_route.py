#!/usr/bin/python3
"""
hbnb route
"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """
    displays hbhb hello world
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    displays HBNB
    """
    return 'HBNB'

if __name__ == "__main__":
    app.run('0.0.0.0', '5000')
