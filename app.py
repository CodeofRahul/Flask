from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Home page"

@app.route('/about')
def about():
    return "About"

@app.route('/contact')
def contact():
    return "Contact Us"

