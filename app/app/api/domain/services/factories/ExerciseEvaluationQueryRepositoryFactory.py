from app.api.data.query.ExerciseEvaluationMongoQueryRepository import ExerciseEvaluationMongoQueryRepository


class ExerciseEvaluationQueryRepositoryFactory:
    def create_exercise_evaluation_query_repository(self):
        return ExerciseEvaluationMongoQueryRepository()
