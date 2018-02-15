import unittest
from unittest import mock

from app.api.services.QueryExecutionService import QueryExecutionService
from app.api.services.errors.ServiceError import ServiceError
from app.api.services.wrappers.MongoWrapper import MongoWrapper
from app.api.services.wrappers.exceptions.MongoWrapperException import MongoWrapperException


class QueryExecutionServiceUnitTest(unittest.TestCase):
    def setUp(self):
        self.stub_mongo_wrapper = mock.Mock(spec=MongoWrapper)
        self.sut = QueryExecutionService(mongo_wrapper=self.stub_mongo_wrapper)

    def test_executeQuery_called_correctCallToInnerWrapperExecuteQuery(self):
        self.sut.execute_query("fakequery")
        self.stub_mongo_wrapper.execute_query.assert_called_once_with('fakequery')

    def test_executeQuery_calledWithInnerWrapperWhichRaisesWrapperException_raiseServiceError(self):
        self.stub_mongo_wrapper.execute_query.side_effect = MongoWrapperException()
        self.assertRaises(ServiceError, self.sut.execute_query, query='fakequery')
