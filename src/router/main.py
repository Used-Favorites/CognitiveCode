from flask import Blueprint

main = Blueprint('main', __name__)

@main.before_request
def before_request():
    print('Before Request')

@main.route('/', methods=['GET'])
def hello() -> dict[any]:
    return {
        'message': 'Hello World!'
    }