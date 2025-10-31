from flask import Blueprint, jsonify, request
from ...utils.device import devices, is_busy
from ...job import jobs, Job, JobState
from uuid import UUID

job_blueprint = Blueprint('job', __name__)

@job_blueprint.route("/")
def list():
    id = request.form.get("id")
    if id:
        for j in jobs:
            if j.id != id:
                continue
            
            return jsonify({ "data": [ dict(j) ] })

        return jsonify({ "message": "Could not find the specified job" }), 404
    else:
        return jsonify({ "data": jobs })

@job_blueprint.route("/create", methods=["POST"])
def start():
    if len(devices) == 0:
        return jsonify({ "message": "No devices are available for this job" }), 503

    name = request.form.get("name", "Unknown Disc")
    device = request.form.get("dev", devices[0]["node"])
    if is_busy(device):
        return jsonify({ "message": "The requested device is busy" }), 503
    
    job = Job(name, device)
    jobs.append(job)
    job.process()

    return jsonify({ "message": "Job created", "data": [ dict(job) ] })

@job_blueprint.route("/cancel", methods=["POST"])
def cancel():
    return jsonify({ "message": "Job has been cancelled." })

@job_blueprint.route("/download")
def download():
    id = request.form.get("id")
    if not id:
        return jsonify({ "message": "No job ID provided" }), 400
    
    for j in jobs:
        if j.id != id:
            continue
        
        if j.state != JobState.DONE:
            return jsonify({ "message": "Job is still being processed. Please try again later." }), 400

        break

    return jsonify({ "message": "Not implemented" }), 500