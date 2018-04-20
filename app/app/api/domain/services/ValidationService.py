import re

from demjson import decode

from app.api.domain.models.ExerciseValidation import ExerciseValidation
from app.api.domain.services.ExerciseEvaluationService import ExerciseEvaluationService
from app.api.domain.services.data.query.errors.QueryError import QueryError
from app.api.domain.services.data.query.errors.ResourceNotFoundQueryError import ResourceNotFoundQueryError
from app.api.domain.services.errors.ResourceNotFoundServiceError import ResourceNotFoundServiceError
from app.api.domain.services.errors.ServiceError import ServiceError
from app.api.domain.services.factories.ExerciseQueryRepositoryFactory import ExerciseQueryRepositoryFactory


class ValidationService:

    def __init__(self, exercise_query_repository=None, exercise_evaluation_service=None):
        if exercise_query_repository is not None:
            self.__exercise_query_repository = exercise_query_repository
        else:
            exercise_query_repository_factory = ExerciseQueryRepositoryFactory()
            self.__exercise_query_repository = exercise_query_repository_factory.create_exercise_query_repository()

        if exercise_evaluation_service is not None:
            self.__exercise_evaluation_service = exercise_evaluation_service
        else:
            self.__exercise_evaluation_service = ExerciseEvaluationService()

    def validate_answer(self, user_id, exercise_id, time_left, answer):
        if user_id is None:
            raise ValueError('user_id cannot be None')
        if exercise_id is None:
            raise ValueError('exercise_id cannot be None')
        if time_left is None:
            raise ValueError('time_left cannot be None')
        if answer is None:
            raise ValueError('answer cannot be None')
        try:
            exercise = self.__exercise_query_repository.get_exercise_by_id(exercise_id=exercise_id)
            is_valid_answer = self.__compare_solution_and_answer(answer=answer, solution=exercise.get_solution())
            if is_valid_answer:
                self.__exercise_evaluation_service.update_exercise_evaluation_as_solved(user_id, exercise_id, time_left)
            return ExerciseValidation(is_valid_answer)
        except ResourceNotFoundQueryError as rnfqe:
            raise ResourceNotFoundServiceError(str(rnfqe))
        except QueryError as qe:
            raise ServiceError(str(qe))

    def __compare_solution_and_answer(self, answer, solution):
        answer = self.__get_dict_list_by_str_representation(answer)
        solution = self.__get_dict_list_by_str_representation(solution)
        return answer == solution

    def __get_dict_list_by_str_representation(self, input):
        str_dicts_list = input.split('\n')
        dicts_list = []
        for str_dict in str_dicts_list:
            # TODO: Remove last elem to avoid this assertion
            if str_dict != str_dicts_list[-1]:
                object_id_re = re.compile('ObjectId\\(["\\\'][0-9a-f]+["\\\']\\)')
                filtered_text = re.findall(object_id_re, str_dict)
                for element in filtered_text:
                    str_dict = str_dict.replace(element, '"' + element[10:-2] + '"')
                dicts_list.append(decode(str_dict))
        return dicts_list
