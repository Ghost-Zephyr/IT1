#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True

from routes import *

if __name__ == "__main__":
    app.run(port=8080)
