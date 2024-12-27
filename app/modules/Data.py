from flask import Blueprint
from flask import current_app

blueprint = Blueprint('hello', __name__, url_prefix = '/hello')

@blueprint.route('/say', methods=["GET"])
def say_hello():
    return f'Hello World {current_app.config.get('ENV_VAR')}'