from flask import Flask
from . import jinja

app = Flask(__name__)

# tasks for jinja template
from os import path, popen
tasks = []
tf = popen(f'ls {path.abspath("./../javascript/tasks")}').read().split('\n')
for fn in tf:
    tn = fn.split('.')[0].split('-')
    tasks.append({
        'num': tn[0],
        'name': tn[1]
    })
del tf

app.add_url_rule('/it1', 'index', jinja.index,
    methods=['GET'])

app.add_url_rule('/it1/js', 'jsindex', jinja.jsindex,
    methods=['GET'], defaults={'tasks':tasks})

app.add_url_rule('/it1/js/1', 'js1', jinja.js1,
    methods=['GET'])

