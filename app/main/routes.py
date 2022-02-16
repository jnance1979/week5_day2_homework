
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'home'

@main.route('/about')
def about():
    return 'about'

@main.route('/contact')
def contact():
    return 'contact'