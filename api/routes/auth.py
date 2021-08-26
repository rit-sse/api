from flask import session, redirect, url_for
from flask.json import jsonify
from api import app, oauth
from api import models


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
        return jsonify(
            {
                "google": session["user"],
                "officer": models.Officer.is_officer(
                    session["user"]["email"].split("@")[0]
                ),
                "primary": models.Officer.is_primary(
                    session["user"]["email"].split("@")[0]
                ),
                "rit_student": session["user"]["email"].split("@")[1] == "g.rit.edu",
            }
        )
    except:
        return jsonify({"error": "not logged in"})
