from app.api.dal import ExerciseQueryRepository
from app.api.services.errors.ResourceNotFoundServiceError import ResourceNotFoundServiceError


class ExerciseService:

    def __init__(self, exercise_query_repository=None):
        if not exercise_query_repository:
            self.__exercise_query_respository = ExerciseQueryRepository()
        else:
            self.__exercise_query_respository = exercise_query_repository

    def get_exercise_by_id(self, exercise_id):
        # access to dal
        pass

    def check_if_answer_is_correct(self, exercise_id, answer):
        if exercise_id is None:
            raise ResourceNotFoundServiceError('id cannot be None')
        if answer is None:
            raise ResourceNotFoundServiceError('answer cannot be None')
        # get exercise in db
        # compare answer to solution
        pass
