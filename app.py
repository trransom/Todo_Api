from flask import Flask, g, jsonify, render_template

import models
from resources.todos import todos_api

import config

DEBUG = True
HOST = '127.0.0.1'
PORT = 8000

app = Flask(__name__)
app.register_blueprint(todos_api, url_prefix='/api/v1')


@app.route('/')
def my_todos():
    return render_template('index.html')

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)