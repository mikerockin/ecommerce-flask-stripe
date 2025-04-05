from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )
    email = db.Column(
        db.String(40),
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=True
	)

    def get_id(self):
        return self.username

class VisitCounter(db.Model):
    __tablename__ = 'visit_counter'

    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f'<VisitCounter {self.count}>'


