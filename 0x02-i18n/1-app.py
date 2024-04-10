#!/usr/bin/env python3
"""
1. Basic Babel setup
"""

from flask import Flask
from flask_babel import Babel
from flask import render_template

babel = Babel()


class Config:
    """ includes languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


@app.route("/", methods=["GET"])
def index() -> str:
    """ hello world """
    return render_template('0-index.html', strict_slashes=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
