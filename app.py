# from api import app
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask Github!'







if __name__ == '__main__':
    app.run(debug=True)