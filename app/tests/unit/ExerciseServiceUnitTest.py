import unittest
from unittest import mock

from ddt import data, ddt
from django.core.serializers.json import json

from app.api.dal.ExerciseQueryRepository import ExerciseQueryRepository
from app.api.dal.errors.QueryError import QueryError
from app.api.dal.errors.ResourceNotFoundQueryError import ResourceNotFoundQueryError
from app.api.models.Exercise import Exercise
from app.api.services.ExerciseService import ExerciseService
from app.api.services.errors.ResourceNotFoundServiceError import ResourceNotFoundServiceError
from app.api.services.errors.ServiceError import ServiceError


@ddt
class ExerciseServiceUnitTest(unittest.TestCase):

    def setUp(self):
        self.stub_exercise_query_repository = mock.Mock(spec=ExerciseQueryRepository)
        self.sut = ExerciseService(self.stub_exercise_query_repository)

    @data(
        {'exercise_id': None, 'answer': 'testanswer'},
        {'exercise_id': 'testid', 'answer': None},
        {'exercise_id': None, 'answer': None}
    )
    def test_checkIfAnswerIsCorrect_calledWithNoneParams_raiseValueError(self, input):
        self.assertRaises(ValueError, self.sut.check_if_answer_is_correct,
                          exercise_id=input['exercise_id'], answer=input['answer'])

    @data(
        {'solution': {"a": 0, "b": 0, "c": 0}, 'answer': {"a": 0, "b": 0, "c": 0}, 'expected': True},
        {'solution': {"a": 0, "b": 0, "c": 0}, 'answer': {"a": 2, "v": 0}, 'expected': False}
    )
    def test_checkIfAnswerIsCorrect_calledWithValidParams_returnCorrectResult(self, input):
        self.stub_exercise_query_repository.get_exercise_by_id.return_value = Exercise(_id='fakeid',
                                                                                       question='fakequestion',
                                                                                       solution=json.dumps(
                                                                                           input['solution']))
        self.assertEqual(self.sut.check_if_answer_is_correct(exercise_id='fakeid', answer=json.dumps(input['answer'])),
                         input['expected'])

    def test_checkIfAnswerIsCorrect_calledWithQueryRepositoryWhichThrowsQueryError_throwServiceError(self):
        self.stub_exercise_query_repository.get_exercise_by_id.side_effect = QueryError()
        self.assertRaises(ServiceError, self.sut.check_if_answer_is_correct, exercise_id='fakeid',
                          answer='fakeanswer')

    def test_checkIfAnswerIsCorrect_calledWithQueryRepositoryWhichThrowsResourceNotFoundQueryError_throwResourceNotFoundServiceError(
            self):
        self.stub_exercise_query_repository.get_exercise_by_id.side_effect = ResourceNotFoundQueryError()
        self.assertRaises(ResourceNotFoundServiceError, self.sut.check_if_answer_is_correct, exercise_id='fakeid',
                          answer='fakeanswer')

    def test_getExerciseById_calledWithNoneId_raiseValueError(self):
        self.assertRaises(ValueError, self.sut.get_exercise_by_id, exercise_id=None)

    def test_getExerciseById_called_correctCallToInnerQueryRepository(self):
        self.sut.get_exercise_by_id(exercise_id='fakeid')
        self.stub_exercise_query_repository.get_exercise_by_id.assert_called_once_with(exercise_id='fakeid')

    def test_getExerciseById_calledWithQueryRepositoryWhichThrowsQueryError_throwServiceError(self):
        self.stub_exercise_query_repository.get_exercise_by_id.side_effect = QueryError()
        self.assertRaises(ServiceError, self.sut.get_exercise_by_id, exercise_id='fakeid')

    def test_getExerciseById_calledWithQueryRepositoryWhichThrowsResourceNotFoundQueryError_throwResourceNotFoundServiceError(
            self):
        self.stub_exercise_query_repository.get_exercise_by_id.side_effect = ResourceNotFoundQueryError()
        self.assertRaises(ResourceNotFoundServiceError, self.sut.get_exercise_by_id, exercise_id='fakeid')
