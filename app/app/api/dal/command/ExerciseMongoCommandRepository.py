from app.api.services.dalinterfaces.command.IExerciseCommandRepository import IExerciseCommandRepository


class ExerciseMongoCommandRepository(IExerciseCommandRepository):

    def __init__(self):
        pass

    def create_exercise(self, exercise):
        # todo: create exercise in db
        pass
