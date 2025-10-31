from flask import Blueprint, jsonify
from ...utils.device import devices

devices_blueprint = Blueprint('devices', __name__)

@devices_blueprint.route("/devices")
def get_devices():
    count = len(devices)
    return jsonify({ "count": count, "drives": devices })