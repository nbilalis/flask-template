from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from os import environ

app = Flask(__name__)

# python -c 'import secrets; print(secrets.token_hex())'
app.secret_key = environ.get('SECRET_KEY', '05a691f2eee3a3b65bf680461babbfa173c6a30d61746622165eb837c2873b24')

toolbar = DebugToolbarExtension(app)


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='localhost', port=int(environ.get('SERVER_PORT', 5000)), debug=True)
