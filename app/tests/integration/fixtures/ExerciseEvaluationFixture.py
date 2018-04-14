from app.api.domain.models.ExerciseEvaluation import ExerciseEvaluation


class ExerciseEvaluationFixture:
    @staticmethod
    def fixture():
        return [
            ExerciseEvaluation(exercise_id="4d128b6ea794fc13a8000003", user_id="4d128b6ea794fc13a8000002",
                               _id="666f6f2d6261722d71757578", score=123),
            ExerciseEvaluation(exercise_id="507f1f77bcf86cd799439011", user_id="4cdfb11e1f3c000000007822",
                               _id="54759eb3c090d83494e2d804", score=123)
        ]

    @staticmethod
    def get_collection_name():
        return "evaluations"
