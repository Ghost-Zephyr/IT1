from flask import Flask
from . import jinja

app = Flask(__name__)


app.add_url_rule('/it1', 'index', jinja.index,
    methods=['GET'])

app.add_url_rule('/it1/js', 'javascirpt', jinja.javascirpt,
    methods=['GET'])

app.add_url_rule('/it1/js/1', 'javascirpt1', jinja.javascirpt1,
    methods=['GET'])

