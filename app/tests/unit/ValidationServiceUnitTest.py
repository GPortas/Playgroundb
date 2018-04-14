import unittest
from unittest import mock

from ddt import data, ddt

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
        self.sut = ValidationService(self.stub_exercise_query_repository)

    @data(
        {'exercise_id': None, 'answer': 'testanswer'},
        {'exercise_id': 'testid', 'answer': None},
        {'exercise_id': None, 'answer': None}
    )
    def test_validateAnswer_calledWithNoneParams_raiseValueError(self, input):
        self.assertRaises(ValueError, self.sut.validate_answer,
                          exercise_id=input['exercise_id'], answer=input['answer'])

    #TODO
    def test_validateAnswer_calledWithValidParams_returnCorrectResult(self):
        pass

    def test_validateAnswer_calledWithQueryRepositoryWhichThrowsQueryError_throwServiceError(self):
        self.stub_exercise_query_repository.get_exercise_by_id.side_effect = QueryError()
        self.assertRaises(ServiceError, self.sut.validate_answer, exercise_id='fakeid',
                          answer='fakeanswer')

    def test_validateAnswer_calledWithQueryRepositoryWhichThrowsResourceNotFoundQueryError_throwResourceNotFoundServiceError(
            self):
        self.stub_exercise_query_repository.get_exercise_by_id.side_effect = ResourceNotFoundQueryError()
        self.assertRaises(ResourceNotFoundServiceError, self.sut.validate_answer, exercise_id='fakeid',
                          answer='fakeanswer')
