from flask import Flask
from .routes.api import api_blueprint
from .routes.templates import templates_blueprint

def create():
    app = Flask(__name__)

    app.register_blueprint(api_blueprint, url_prefix="/api")
    app.register_blueprint(templates_blueprint)

    return app