from flask import Flask
from .routes.api import api_blueprint

def create():
    app = Flask(__name__)
    app.register_blueprint(api_blueprint, url_prefix="/api")
    return app