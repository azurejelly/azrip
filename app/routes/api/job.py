from flask import Blueprint, jsonify, request
from ...utils.device import devices, is_busy
from ...job import jobs, Job
from uuid import UUID

job_blueprint = Blueprint('job', __name__)

@job_blueprint.route("/", defaults={"job_id": None})
@job_blueprint.route("/<uuid:job_id>")
def get(job_id: UUID):
    if job_id:
        for j in jobs:
            if j.id != str(job_id):
                continue
            
            return jsonify({ "job": dict(j) })
        
        return jsonify({ "message": "Could not find the specified job" }), 404
    else:
        return jsonify({ "jobs": jobs })

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

    return jsonify({ "message": "Job created", "id": job.id })

@job_blueprint.route("/cancel", methods=["POST"])
def cancel():
    return jsonify({ "message": "Job has been cancelled." })

@job_blueprint.route("/download")
def download():
    return jsonify({ "message": "Job incomplete" }), 400