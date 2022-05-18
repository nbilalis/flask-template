from flask import Flask
from os import environ

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(host='localhost', port=environ.get('SERVER_PORT', 5000), debug=True)
