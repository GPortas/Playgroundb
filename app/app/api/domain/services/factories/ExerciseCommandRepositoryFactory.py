from app.api.data.command.ExerciseMongoCommandRepository import ExerciseMongoCommandRepository


class ExerciseCommandRepositoryFactory:

    def create_exercise_command_repository(self):
        return ExerciseMongoCommandRepository()
