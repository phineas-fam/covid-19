from covidbe.main import ma


class QuestionSchema(ma.Schema):
    class Meta:
        fields = (
            "text",
            "id",
        )


class AnswersSchema(ma.Schema):
    class Meta:
        fields = (
            "province",
            "id",
            "q1",
            "q2",
            "q3",
            "q4",
            "q5",
            "q6",
            "q7",
            "q8",
        )


question_schema = QuestionSchema()
answer_schema = AnswersSchema()
