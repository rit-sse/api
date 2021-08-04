from api import app
from flask import jsonify


@app.route("/api/v2/status")
def _get_root():
    return jsonify({"status": "ok"}), 200
