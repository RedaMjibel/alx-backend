#!/usr/bin/env python3

"""
0. Basic Flask app
"""

from flask import Flask, request
from flask import render_template


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index() -> str:
    """ hello world """
    return render_template('0-index.html', strict_slashes=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
