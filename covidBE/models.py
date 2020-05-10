import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Enum
from sqlalchemy.sql import func

db = SQLAlchemy()


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)


class Answers(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    q1 = db.Column(Enum("Yes", "No", name="Answer"))
    q2 = db.Column(Enum("Yes", "No", name="Answer"))
    q3 = db.Column(Enum("Yes", "No", name="Answer"))
    q4 = db.Column(Enum("Yes", "No", name="Answer"))
    q5 = db.Column(Enum("Yes", "No", name="Answer"))
    q6 = db.Column(Enum("Yes", "No", name="Answer"))
    q7 = db.Column(Enum("Yes", "No", name="Answer"))
    q8 = db.Column(Enum("Yes", "No", name="Answer"))
    date = db.Column(db.DateTime, server_default=func.current_timestamp())
    province = db.Column(db.Text)
    longitude = db.Column(db.Numeric)
    latitude = db.Column(db.Numeric)
