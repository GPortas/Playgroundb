from app.api.data.query.ExerciseMongoQueryRepository import ExerciseMongoQueryRepository


class ExerciseQueryRepositoryFactory:

    def create_exercise_query_repository(self):
        return ExerciseMongoQueryRepository()
