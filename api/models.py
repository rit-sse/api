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
    __tablename__ = "officers"
    id: int = db.Column(db.Integer, primary_key=True)
    committee: str = db.Column(db.String(64), nullable=False)
    rit_dce: str = db.Column(db.String(32), nullable=False)
    email: str = db.Column(db.String(128), nullable=False)
    name: str = db.Column(db.String(128), nullable=False)
    bio: str = db.Column(db.Text)
    is_primary: bool = db.Column(db.Boolean)
    start_date: datetime = db.Column(db.DateTime, nullable=False)
    end_date: datetime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Officer {}>".format(self.id)

    @classmethod
    def get_by_id(cls, id: int):
        return cls.query.filter(cls.id == id).first()

    @classmethod
    def get_active(cls):
        return cls.query.filter(
            cls.start_date < datetime.now(), cls.end_date > datetime.now()
        ).all()

    @classmethod
    def is_officer(cls, email: str) -> bool:
        if email.split("@")[1] != "g.rit.edu":
            return False
        dce = email.split("@")[0]
        return (
            len(
                cls.query.filter(
                    cls.start_date < datetime.now(), cls.end_date > datetime.now()
                )
                .filter(cls.rit_dce == dce)
                .all()
            )
            > 0
        )

    @classmethod
    def is_primary_officer(cls, email: str):
        if email.split("@")[1] != "g.rit.edu":
            return False
        dce = email.split("@")[0]
        return (
            len(
                cls.query.filter(
                    cls.start_date < datetime.now(), cls.end_date > datetime.now()
                )
                .filter(cls.rit_dce == dce)
                .filter(cls.is_primary == True)
                .all()
            )
            > 0
        )


@dataclass
class Membership(db.Model):
    __tablename__ = "memberships"
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(128), nullable=False)
    rit_dce: str = db.Column(db.String(32), nullable=False)
    reason: str = db.Column(db.String(256), nullable=False)
    given_by: str = db.Column(db.String(32), nullable=False)
    given: datetime = db.Column(db.DateTime, nullable=False)
    expires: datetime = db.Column(db.DateTime, nullable=False)
    approved: bool = db.Column(db.Boolean)

    def __repr__(self):
        return "<Membership {}>".format(self.id)

    @classmethod
    def get_active(cls):
        return cls.query.filter(
            cls.given < datetime.now(), cls.expires > datetime.now()
        ).filter(
            cls.approved == True
        ).all()

    @classmethod
    def get_unnaproved(cls):
        return cls.query.filter(
            cls.given < datetime.now(), cls.expires > datetime.now()
        ).filter(
            cls.approved == False
        ).all()
