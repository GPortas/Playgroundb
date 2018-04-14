from app.api.data.command.ExerciseEvaluationMongoCommandRepository import ExerciseEvaluationMongoCommandRepository


class ExerciseEvaluationCommandRepositoryFactory:
    def create_exercise_evaluation_command_repository(self):
        return ExerciseEvaluationMongoCommandRepository()