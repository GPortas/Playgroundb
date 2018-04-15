from app.api.domain.models.ExerciseEvaluation import ExerciseEvaluation
from app.api.domain.services.ExerciseEvaluationService import ExerciseEvaluationService
from app.api.domain.services.data.command.errors.CommandError import CommandError
from app.api.domain.services.data.query.errors.QueryError import QueryError
from app.api.domain.services.data.query.errors.ResourceNotFoundQueryError import ResourceNotFoundQueryError
from app.api.domain.services.errors.ResourceNotFoundServiceError import ResourceNotFoundServiceError
from app.api.domain.services.errors.ServiceError import ServiceError
from app.api.domain.services.factories.ExerciseCommandRepositoryFactory import ExerciseCommandRepositoryFactory
from app.api.domain.services.factories.ExerciseQueryRepositoryFactory import ExerciseQueryRepositoryFactory


class ExerciseService:

    def __init__(self, exercise_query_repository=None, exercise_command_repository=None,
                 exercise_evaluation_service=None):
        if exercise_query_repository is not None:
            self.__exercise_query_repository = exercise_query_repository
        else:
            exercise_query_repository_factory = ExerciseQueryRepositoryFactory()
            self.__exercise_query_repository = exercise_query_repository_factory.create_exercise_query_repository()

        if exercise_command_repository is not None:
            self.__exercise_command_repository = exercise_command_repository
        else:
            exercise_command_repository_factory = ExerciseCommandRepositoryFactory()
            self.__exercise_command_repository = exercise_command_repository_factory.create_exercise_command_repository()

        if exercise_evaluation_service is not None:
            self.__exercise_evaluation_service = exercise_evaluation_service
        else:
            self.__exercise_evaluation_service = ExerciseEvaluationService()

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

    def get_unsolved_exercises_by_user_id(self, user_id):
        if user_id is None:
            raise ValueError('user id cannot be None')
        exercises_list = self.__exercise_query_repository.get_exercises_list()
        unsolved_exercises_list = []
        for exercise in exercises_list:
            exercise_evaluation = self.__exercise_evaluation_service.get_exercise_evaluation(user_id=user_id,
                                                                                             exercise_id=exercise.get_id())
            if exercise_evaluation is not None:
                if exercise_evaluation.get_status() == ExerciseEvaluation.STATUS_UNSOLVED:
                    self.__exercise_evaluation_service.increment_exercise_evaluation_attempts(exercise_evaluation)
                    unsolved_exercises_list.append(exercise)
            else:
                self.__exercise_evaluation_service.create_exercise_evaluation(
                    ExerciseEvaluation(user_id, exercise.get_id()))
                unsolved_exercises_list.append(exercise)
        return unsolved_exercises_list
