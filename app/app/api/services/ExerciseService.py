from app.api.dal.ExerciseQueryRepository import ExerciseQueryRepository
from app.api.dal.command.ExerciseCommandRepository import ExerciseCommandRepository
from app.api.dal.command.errors.CommandError import CommandError
from app.api.dal.query.errors.QueryError import QueryError
from app.api.dal.query.errors.ResourceNotFoundQueryError import ResourceNotFoundQueryError
from app.api.services.errors.ResourceNotFoundServiceError import ResourceNotFoundServiceError
from app.api.services.errors.ServiceError import ServiceError


class ExerciseService:

    def __init__(self, exercise_query_repository=None, exercise_command_repository=None):
        if not exercise_query_repository:
            self.__exercise_query_repository = ExerciseQueryRepository()
        else:
            self.__exercise_query_repository = exercise_query_repository

        if not exercise_command_repository:
            self.__exercise_command_repository = ExerciseCommandRepository()
        else:
            self.__exercise_command_repository = exercise_command_repository

    def create_exercise(self, exercise):
        if exercise is None:
            raise ValueError('Exercise cannot be None')
        try:
            self.__exercise_command_repository.create_exercise(exercise=exercise)
        except CommandError as ce:
            raise ServiceError(str(ce))

    def get_exercise_by_id(self, exercise_id):
        if exercise_id is None:
            raise ValueError('id cannot be None')
        try:
            return self.__exercise_query_repository.get_exercise_by_id(exercise_id=exercise_id)
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
            exercise = self.__exercise_query_repository.get_exercise_by_id(exercise_id=exercise_id)
            return exercise.validate_answer(answer=answer)
        except ResourceNotFoundQueryError as rnfqe:
            raise ResourceNotFoundServiceError(str(rnfqe))
        except QueryError as qe:
            raise ServiceError(str(qe))
