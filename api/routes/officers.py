from api import app
from api.models import Officer
from flask import jsonify


@app.route("/api/v2/officers", methods=["GET"])
def _get_api_v2_officers():
    return jsonify(Officer.get_active())
