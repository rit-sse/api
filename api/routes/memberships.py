import re
from datetime import datetime
from api import app, db
from api.models import Membership, Officer
from flask import jsonify, request, session
from typing import AnyStr, List, Pattern


@app.route("/api/v2/memberships", methods=["GET"])
def _get_api_v2_memberships():
    return jsonify(Membership.get_active())

@app.route("/api/v2/memberships/unnaproved", methods=["GET"])
def _get_api_v2_memberships_unnaproved():
    if not "user" in session:
        return jsonify({"error": "not logged in"}), 401
    if not Officer.is_primary_officer(session["user"]["email"]):
        return jsonify({"error": "not a primary officer"}), 403

    return jsonify(Membership.get_unnaproved())
