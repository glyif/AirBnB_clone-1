#!/usr/bin/python3
"""
flask hello world
"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """
    hello world function
    """
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run('0.0.0.0', '5000')
