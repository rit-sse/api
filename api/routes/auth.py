from flask import session, redirect, url_for
from flask.json import jsonify
from api import app, oauth


@app.route("/api/v2/login")
def _get_api_v2_login():
    redirect_uri = url_for("_get_api_v2_redirect", _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route("/api/v2/redirect")
def _get_api_v2_redirect():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token)
    session["user"] = user
    return redirect("/api/v2/whoami")


@app.route("/api/v2/logout")
def _get_api_v2_logout():
    session.pop("user", None)
    return redirect("/")


@app.route("/api/v2/whoami")
def _get_api_v2_whoami():
    try:
        return jsonify(session["user"])
    except:
        return jsonify({"error": "not logged in"})
