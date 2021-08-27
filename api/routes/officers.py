import re
from datetime import datetime
from api import app, db
from api.models import Officer
from flask import jsonify, request, session


@app.route("/api/v2/officers", methods=["GET"])
def _get_api_v2_officers():
    return jsonify(Officer.get_active())


@app.route("/api/v2/officers", methods=["POST"])
def _post_api_v2_officers():
    if not "user" in session:
        return jsonify({"error": "not logged in"}), 401
    if not Officer.is_primary_officer(session["user"]["email"]):
        return jsonify({"error": "not a primary officer"}), 401

    o: Officer = Officer(**request.json)

    o.start_date = datetime.strptime(o.start_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    o.end_date = datetime.strptime(o.end_date, "%Y-%m-%dT%H:%M:%S.%fZ")

    # TODO: More validation
    dce_regex = re.compile("^[a-z]{2,3}[0-9]{4}$")
    if not dce_regex.match(o.rit_dce):
        raise Exception("dce does not match required format")

    db.session.add(o)
    db.session.commit()

    return jsonify(o)
