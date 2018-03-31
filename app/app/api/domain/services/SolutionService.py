import re

from demjson import decode

from app.api.domain.models.ExerciseValidation import ExerciseValidation
from app.api.domain.services.data.query.errors.QueryError import QueryError
from app.api.domain.services.data.query.errors.ResourceNotFoundQueryError import ResourceNotFoundQueryError
from app.api.domain.services.errors.ResourceNotFoundServiceError import ResourceNotFoundServiceError
from app.api.domain.services.errors.ServiceError import ServiceError
from app.api.domain.services.factories.ExerciseQueryRepositoryFactory import ExerciseQueryRepositoryFactory


class SolutionService:

    def __init__(self, exercise_query_repository=None):
        if exercise_query_repository is not None:
            self.__exercise_query_repository = exercise_query_repository
        else:
            exercise_query_repository_factory = ExerciseQueryRepositoryFactory()
            self.__exercise_query_repository = exercise_query_repository_factory.create_exercise_query_repository()

    def validate_answer(self, exercise_id, answer):
        if exercise_id is None:
            raise ValueError('id cannot be None')
        if answer is None:
            raise ValueError('answer cannot be None')
        try:
            exercise = self.__exercise_query_repository.get_exercise_by_id(exercise_id=exercise_id)
            return ExerciseValidation(
                self.__compare_solution_and_answer(answer=answer, solution=exercise.get_solution()))
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
