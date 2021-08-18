from dataclasses import dataclass
from datetime import datetime

from api import db

class GoLink(db.Model):
    __tablename__ = "golinks"
    short_link = db.Column(db.String(64), primary_key=True)
    full_link = db.Column(db.Text, nullable=False)
    public = db.Column(db.Boolean)
    description = db.Column(db.Text)

    def __repr__(self):
        return "<GoLink {}>".format(self.short_link)


# dataclass usage: https://stackoverflow.com/a/57732785
@dataclass
class Officer(db.Model):
    id: int
    committee: str
    rit_dce: str
    name: str
    bio: str
    is_primary: bool
    start_date: datetime
    end_date: datetime

    __tablename__ = "officers"
    id = db.Column(db.Integer, primary_key=True)
    committee = db.Column(db.String(64), nullable=False)
    rit_dce = db.Column(db.String(32), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    bio = db.Column(db.Text)
    is_primary = db.Column(db.Boolean)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Officer {}>".format(self.id)

    @classmethod
    def get_active(cls):
        return cls.query.filter(cls.start_date < datetime.now(), cls.end_date > datetime.now()).all()


class Membership(db.Model):
    __tablename__ = "memberships"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    rit_dce = db.Column(db.String(32), nullable=False)
    reason = db.Column(db.Text)
    given = db.Column(db.DateTime, nullable=False)
    expires = db.Column(db.DateTime, nullable=False)
    approved = db.Column(db.Boolean)

    def __repr__(self):
        return "<Membership {}>".format(self.id)
