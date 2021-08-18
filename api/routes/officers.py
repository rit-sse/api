from api import app
from api.models import Officer
from flask import jsonify

@app.route("/api/v2/officers")
def _get_officers():
    return jsonify(Officer.get_active())