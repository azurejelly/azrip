from flask import Blueprint
from .index import index_blueprint

templates_blueprint = Blueprint('templates', __name__)
templates_blueprint.register_blueprint(index_blueprint)