from flask import Flask, g, jsonify, render_template

import models

import config

DEBUG = True
HOST = '127.0.0.1'
PORT = 8000

app = Flask(__name__)


@app.route('/')
def my_todos():
    return render_template('index.html')

if __name__ == '__main__':
    models.initialize()
#    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
    app.run(debug=DEBUG, host=HOST, port=PORT)