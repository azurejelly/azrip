from flask import Blueprint
from .devices import devices_blueprint
from .job import job_blueprint

api_blueprint = Blueprint('api', __name__)
api_blueprint.register_blueprint(devices_blueprint)
api_blueprint.register_blueprint(job_blueprint, url_prefix="/jobs")