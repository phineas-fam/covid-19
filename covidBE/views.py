from covidBE.main import db
from covidBE.models import Answers, Questions
from covidBE.schemas import answer_schema, question_schema
from flask import Blueprint, jsonify, request


api_blueprint = Blueprint("api", "api")


@api_blueprint.route("/answer", methods=["POST"])
def add_answer():
    answers = request.json["answers"]
    for answer_item in answers.values():
        answer = answer_item
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


@api_blueprint.route("/answers/", methods=["GET"])
def get_answers():
    answers = Answers.query.all()
    result = answer_schema.dump(answers, many=True)
    return jsonify({"answers": result})


@api_blueprint.route("/questions/", methods=["GET"])
def get_questions():
    questions = Questions.query.all()
    result = answer_schema.dump(questions, many=True)
    return jsonify({"questions": result})