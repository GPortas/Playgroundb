from app.api.domain.services.data.command.errors.CommandError import CommandError
from app.api.domain.services.data.query.errors.QueryError import QueryError
from app.api.domain.services.data.query.errors.ResourceNotFoundQueryError import ResourceNotFoundQueryError
from app.api.domain.services.errors.ResourceNotFoundServiceError import ResourceNotFoundServiceError
from app.api.domain.services.errors.ServiceError import ServiceError
from app.api.domain.services.factories.ExerciseEvaluationCommandRepositoryFactory import \
    ExerciseEvaluationCommandRepositoryFactory
from app.api.domain.services.factories.ExerciseEvaluationQueryRepositoryFactory import \
    ExerciseEvaluationQueryRepositoryFactory


class ExerciseEvaluationService:
    def __init__(self, exercise_evaluation_query_repository=None, exercise_evaluation_command_repository=None):
        if exercise_evaluation_query_repository is not None:
            self.__exercise_evaluation_query_repository = exercise_evaluation_query_repository
        else:
            exercise_evaluation_query_repository_factory = ExerciseEvaluationQueryRepositoryFactory()
            self.__exercise_evaluation_query_repository = exercise_evaluation_query_repository_factory.create_exercise_evaluation_query_repository()

        if exercise_evaluation_command_repository is not None:
            self.__exercise_evaluation_command_repository = exercise_evaluation_command_repository
        else:
            exercise_evaluation_command_repository_factory = ExerciseEvaluationCommandRepositoryFactory()
            self.__exercise_evaluation_command_repository = exercise_evaluation_command_repository_factory.create_exercise_evaluation_command_repository()

    def get_exercise_evaluation(self, user_id, exercise_id):
        if user_id is None:
            raise ValueError('user_id cannot be None')
        if exercise_id is None:
            raise ValueError('exercise_id cannot be None')
        try:
            return self.__exercise_evaluation_query_repository.get_exercise_evaluation(user_id, exercise_id)
        except QueryError as qe:
            raise ServiceError(str(qe))

    def create_exercise_evaluation(self, exercise_evaluation):
        if exercise_evaluation is None:
            raise ValueError('Exercise evaluation cannot be None')
        try:
            self.__exercise_evaluation_command_repository.create_exercise_evaluation(
                exercise_evaluation=exercise_evaluation)
        except CommandError as ce:
            raise ServiceError(str(ce))

    def increment_exercise_evaluation_attempts(self, exercise_evaluation):
        if exercise_evaluation is None:
            raise ValueError('Exercise evaluation cannot be None')
        try:
            self.__exercise_evaluation_command_repository.increment_exercise_evaluation_attempts(
                exercise_evaluation=exercise_evaluation)
        except CommandError as ce:
            raise ServiceError(str(ce))

    def update_exercise_evaluation_as_solved(self, user_id, exercise_id, time_left):
        if user_id is None:
            raise ValueError('user_id cannot be None')
        if exercise_id is None:
            raise ValueError('exercise_id cannot be None')
        if time_left is None:
            raise ValueError('leftover_time cannot be None')
        exercise_evaluation = self.get_exercise_evaluation(user_id, exercise_id)
        score = self.__calculate_exercise_evaluation_score(exercise_evaluation.get_attempt(), time_left)
        try:
            self.__exercise_evaluation_command_repository.update_exercise_evaluation_as_solved(exercise_evaluation,
                                                                                               score)
        except CommandError as ce:
            raise ServiceError(str(ce))

    def __calculate_exercise_evaluation_score(self, attempt, time_left):
        return int(float(time_left) / attempt)
