#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

from py.routes import *

if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run(port=8080)

