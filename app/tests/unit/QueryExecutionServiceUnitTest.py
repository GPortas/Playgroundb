import unittest
from unittest import mock

from app.api.domain.models.Exercise import Exercise
from app.api.domain.services.ExerciseService import ExerciseService
from app.api.domain.services.QueryExecutionService import QueryExecutionService
from app.api.domain.services.errors.ServiceError import ServiceError
from app.api.domain.services.wrappers.mongo.MongoWrapper import MongoWrapper
from app.api.domain.services.wrappers.mongo.exceptions.MongoWrapperException import MongoWrapperException


class QueryExecutionServiceUnitTest(unittest.TestCase):
    def setUp(self):
        self.stub_mongo_wrapper = mock.Mock(spec=MongoWrapper)
        self.stub_exercise_service = mock.Mock(spec=ExerciseService)
        self.sut = QueryExecutionService(mongo_wrapper=self.stub_mongo_wrapper,
                                         exercise_service=self.stub_exercise_service)

    def test_executeExerciseQuery_called_correctCallToInnerWrapperExecuteQuery(self):
        self.stub_exercise_service.get_exercise_by_id.return_value = self.__get_exercise_test_instance()
        self.sut.execute_exercise_query("fakequery", "666f6f2d6261722d71757578")
        self.stub_mongo_wrapper.execute_query.assert_called_once_with('fakequery')

    def test_executeExerciseQuery_calledWithInnerWrapperWhichRaisesWrapperException_raiseServiceError(self):
        self.stub_exercise_service.get_exercise_by_id.return_value = self.__get_exercise_test_instance()
        self.stub_mongo_wrapper.execute_query.side_effect = MongoWrapperException()
        self.assertRaises(ServiceError, self.sut.execute_exercise_query, query='fakequery',
                          exercise_id='666f6f2d6261722d71757578')

    def test_executeQuery_called_correctCallToInnerWrapperExecuteQuery(self):
        self.sut.execute_query("fakequery")
        self.stub_mongo_wrapper.execute_query.assert_called_once_with('fakequery')

    def test_executeQuery_calledWithInnerWrapperWhichRaisesWrapperException_raiseServiceError(self):
        self.stub_mongo_wrapper.execute_query.side_effect = MongoWrapperException()
        self.assertRaises(ServiceError, self.sut.execute_query, query='fakequery')

    def __get_exercise_test_instance(self):
        return Exercise(author="author1",
                        collection_name="testcollection",
                        collection_data="testdata",
                        question="fakequestion_1",
                        solution="testsolution",
                        _id="666f6f2d6261722d71757578")
