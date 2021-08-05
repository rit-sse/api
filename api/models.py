from api import db


class GoLink(db.Model):
    __tablename__ = "golinks"
    short_link = db.Column(db.String(64), primary_key=True)
    full_link = db.Column(db.Text, nullable=False)
    public = db.Column(db.Boolean)
    description = db.Column(db.Text)

    def __repr__(self):
        return "<GoLink {}>".format(self.short_link)


class Officer(db.Model):
    __tablename__ = "officers"
    id = db.Column(db.Integer, primary_key=True)
    committee = db.Column(db.String(64), nullable=False)
    rit_email = db.Column(db.String(32), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    bio = db.Column(db.Text)
    is_primary = db.Column(db.Boolean)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Officer {}>".format(self.id)
