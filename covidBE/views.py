from flask import Blueprint, jsonify, request
import json

from covidBE.main import db
from covidBE.models import Questions, Answers
from covidBE.schemas import answer_schema, question_schema


api_blueprint = Blueprint("api", "api")


@api_blueprint.route("/answer", methods=["POST"])
def add_answer():

    answer = request.json["answer"]
    new_answer = Answers(**answer)
    db.session.add(new_answer)
    db.session.commit()
    return answer_schema.jsonify(new_answer)


@api_blueprint.route("/question", methods=["POST"])
def add_question():

    question = request.json["question"]
    new_question = Questions(**question)
    db.session.add(new_question)
    db.session.commit()
    return question_schema.jsonify(new_question)


@api_blueprint.route("/survey/", methods=["GET"])
def view_answer():
    answers = Answers.query.get.all()
