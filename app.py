from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this is a demo for CI/CD Pipeline1!"


