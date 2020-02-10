from jinja2 import Environment, FileSystemLoader

j2_env = Environment(loader=FileSystemLoader('.'), trim_blocks=True)

def index():
    return 'Works!'

def javascirpt():
    return 'Works!'

def javascirpt1():
    template = j2_env.get_template('javascript/1.jinja2')
    return template.render()

