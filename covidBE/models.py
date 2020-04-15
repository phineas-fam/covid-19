from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)


class Answers(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    question = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
