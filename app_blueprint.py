from flask import Blueprint

app_blueprint = Blueprint('app_blueprint', __name__)

@app_blueprint.route('/')
def index():
    return "Home page"

@app_blueprint.route('/about')
def about():
    return "About"

@app_blueprint.route('/contact')
def contact():
    return "Contact Us"
