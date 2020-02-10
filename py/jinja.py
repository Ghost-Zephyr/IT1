from jinja2 import Environment, FileSystemLoader
from os.path import abspath

j2_env = Environment(loader=FileSystemLoader(abspath('.')), trim_blocks=True)

def index():
    template = j2_env.get_template('index.jinja2')
    return template.render()

def jsindex():
    template = j2_env.get_template('javascript/index.jinja2')
    return template.render()

def js1():
    template = j2_env.get_template('javascript/1.jinja2')
    return template.render()

