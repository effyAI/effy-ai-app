from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from resources.calculator import calculator

app = Flask(__name__)
cors = CORS(app)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'


if __name__ == "__main__":
    app.run(port=5000)