import unittest
from unittest import mock

from ddt import data, ddt

from app.api.domain.models.Exercise import Exercise
from app.api.domain.services.ExerciseEvaluationService import ExerciseEvaluationService
from app.api.domain.services.ValidationService import ValidationService
from app.api.domain.services.data.query.IExerciseQueryRepository import IExerciseQueryRepository
from app.api.domain.services.data.query.errors.QueryError import QueryError
from app.api.domain.services.data.query.errors.ResourceNotFoundQueryError import ResourceNotFoundQueryError
from app.api.domain.services.errors.ResourceNotFoundServiceError import ResourceNotFoundServiceError
from app.api.domain.services.errors.ServiceError import ServiceError


@ddt
class ValidationServiceUnitTest(unittest.TestCase):

    def setUp(self):
        self.stub_exercise_query_repository = mock.Mock(spec=IExerciseQueryRepository)
        self.stub_exercise_evaluation_service = mock.Mock(spec=ExerciseEvaluationService)
        self.sut = ValidationService(self.stub_exercise_query_repository, self.stub_exercise_evaluation_service)

    @data(
        {'user_id': 'test', 'exercise_id': 'test', 'time_left': 'test', 'answer': None},
        {'user_id': 'test', 'exercise_id': 'test', 'time_left': None, 'answer': 'test'},
        {'user_id': 'test', 'exercise_id': None, 'time_left': 'test', 'answer': 'test'},
        {'user_id': None, 'exercise_id': 'test', 'time_left': 'test', 'answer': 'test'},

    )
    def test_validateAnswer_calledWithNoneParams_raiseValueError(self, input):
        self.assertRaises(ValueError, self.sut.validate_answer, user_id=input['user_id'],
                          exercise_id=input['exercise_id'], time_left=input['time_left'],
                          answer=input['answer'])

    def test_validateAnswer_calledWithQueryRepositoryWhichThrowsQueryError_throwServiceError(self):
        self.stub_exercise_query_repository.get_exercise_by_id.side_effect = QueryError()
        self.assertRaises(ServiceError, self.sut.validate_answer, user_id='test_id', exercise_id='fakeid', time_left=10,
                          answer='fakeanswer')

    def test_validateAnswer_calledWithQueryRepositoryWhichThrowsResourceNotFoundQueryError_throwResourceNotFoundServiceError(
            self):
        self.stub_exercise_query_repository.get_exercise_by_id.side_effect = ResourceNotFoundQueryError()
        self.assertRaises(ResourceNotFoundServiceError, self.sut.validate_answer, user_id='test_id',
                          exercise_id='fakeid', time_left=10,
                          answer='fakeanswer')

    def test_validateAnswer_calledWithValidAnswer_innerExerciseEvaluationServiceUpdateExerciseEvaluationAsSolvedCalledWithRightParams(
            self):
        self.stub_exercise_query_repository.get_exercise_by_id.return_value = self.__get_exercise_test_instance()
        self.sut.validate_answer('test_id', 'exercise_id', 10, 'solution')
        actual = self.stub_exercise_evaluation_service.update_exercise_evaluation_as_solved.call_count
        self.assertEqual(actual, 1)

    def test_validateAnswer_calledWithInvalidAnswer_innerExerciseEvaluationServiceUpdateExerciseEvaluationAsSolvedNeverCalled(
            self):
        self.stub_exercise_query_repository.get_exercise_by_id.return_value = self.__get_exercise_test_instance()
        self.sut.validate_answer('test_id', 'exercise_id', 10, 'wrong_solution')
        actual = self.stub_exercise_evaluation_service.update_exercise_evaluation_as_solved.call_count
        self.assertEqual(actual, 1)

    def __get_exercise_test_instance(self):
        return Exercise('test_author', 'test_collection',
                        'test_question',
                        'solution')
