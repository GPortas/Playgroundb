from app.api.dal.ExerciseQueryRepository import ExerciseQueryRepository
from app.api.dal.errors.QueryError import QueryError
from app.api.dal.errors.ResourceNotFoundQueryError import ResourceNotFoundQueryError
from app.api.services.errors.ResourceNotFoundServiceError import ResourceNotFoundServiceError
from app.api.services.errors.ServiceError import ServiceError


class ExerciseService:

    def __init__(self, exercise_query_repository=None):
        if not exercise_query_repository:
            self.__exercise_query_respository = ExerciseQueryRepository()
        else:
            self.__exercise_query_respository = exercise_query_repository

    def get_exercise_by_id(self, exercise_id):
        if exercise_id is None:
            raise ValueError('id cannot be None')
        try:
            return self.__exercise_query_respository.get_exercise_by_id(exercise_id=exercise_id)
        except ResourceNotFoundQueryError as rnfqe:
            raise ResourceNotFoundServiceError(str(rnfqe))
        except QueryError as qe:
            raise ServiceError(str(qe))

    def check_if_answer_is_correct(self, exercise_id, answer):
        if exercise_id is None:
            raise ValueError('id cannot be None')
        if answer is None:
            raise ValueError('answer cannot be None')
        try:
            exercise = self.__exercise_query_respository.get_exercise_by_id(exercise_id=exercise_id)
            return exercise.validate_answer(answer=answer)
        except ResourceNotFoundQueryError as rnfqe:
            raise ResourceNotFoundServiceError(str(rnfqe))
        except QueryError as qe:
            raise ServiceError(str(qe))
