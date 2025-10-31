from flask import Blueprint

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route("/")
def main():
    return {"message": "OK"}
