import os
import secrets
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "".join(secrets.token_hex(16))
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(dirname(__file__), "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
