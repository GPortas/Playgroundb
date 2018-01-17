from app.api.services.dalinterfaces.query.IExerciseQueryRepository import IExerciseQueryRepository


class ExerciseMongoQueryRepository(IExerciseQueryRepository):

    def __init__(self):
        pass

    def get_exercise_by_id(self, exercise_id):
        result = {}
        return result
