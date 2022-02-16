from flask import Blueprint

pairs = Blueprint('pairs', __name__)


favorites = {
    'actor' : 'dennehy',
    'drink' : 'odouls',
    'day' : 'sunday',
    'tower' : 'sears',
    'bears' : 'hawks',
    'sox' : 'bulls'
    }


@pairs.route('/pairs', methods=['GET'])
def index():
    return favorites