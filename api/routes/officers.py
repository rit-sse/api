import re
from datetime import datetime
from api import app, db
from api.models import Officer
from flask import jsonify, request, session
from typing import AnyStr, List, Pattern


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
    dce_regex: Pattern[AnyStr@compile] = re.compile("^[a-z]{2,3}[0-9]{4}$")
    if not dce_regex.match(o.rit_dce):
        raise Exception("dce does not match required format")

    # TODO: there's a better way to do this
    # TODO: the time check here has to be fixed. currently it prevents adding an officer
    # if they're currently active, but it should check that the new start date isn't 
    # before the existing officer's end date
    current_officers: List[Officer] = Officer.get_active()
    for officer in current_officers:
        if officer.rit_dce == o.rit_dce:
            return jsonify({"error": "an officer with that DCE already exists"}), 400

    db.session.add(o)
    db.session.commit()

    return jsonify(o)
