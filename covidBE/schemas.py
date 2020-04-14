from covidBE.main import ma


class QuestionSchema(ma.Schema):
    class Meta:
        fields = (
            "text",
            "id",
        )


class AnswersSchema(ma.Schema):
    class Meta:
        fields = (
            "question",
            "text",
            "id",
        )


question_schema = QuestionSchema()
answer_schema = AnswersSchema()
