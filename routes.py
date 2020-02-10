from flask import Flask

app = Flask(__name__)

def test():
    return 'Works!'

app.add_url_rule('/', 'test', test,
    methods=['GET'])

