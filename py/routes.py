from flask import Flask
from . import jinja

app = Flask(__name__)


app.add_url_rule('/it1', 'index', jinja.index,
    methods=['GET'])

app.add_url_rule('/it1/js', 'jsindex', jinja.jsindex,
    methods=['GET'])

app.add_url_rule('/it1/js/1', 'js1', jinja.js1,
    methods=['GET'])

