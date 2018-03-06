import unittest
from unittest import mock

from app.api.domain.services.wrappers.mongo.MongoWrapper import MongoWrapper
from app.api.domain.services.wrappers.mongo.PymongoExecutor import PymongoExecutor
from app.api.domain.services.wrappers.mongo.exceptions.MongoWrapperException import MongoWrapperException
from app.api.domain.services.wrappers.mongo.mappers.operationmappers.OperationMapperBase import OperationMapperBase
from app.api.domain.services.wrappers.mongo.mappers.resultmappers.IResultMapper import IResultMapper


class MongoWrapperUnitTest(unittest.TestCase):

    def setUp(self):
        self.stub_operation_mapper = mock.Mock(spec=OperationMapperBase)
        self.stub_result_mapper = mock.Mock(spec=IResultMapper)
        self.stub_pymongo_executor = mock.Mock(spec=PymongoExecutor)
        self.sut = MongoWrapper()

    def test_executeQuery_calledWithInvalidFirstQueryComponent_raiseMongoWrapperException(self):
        self.assertRaises(MongoWrapperException, self.sut.execute_query, query='dx.collection.find({})')

    def test_executeQuery_calledWithInvalidSecondQueryComponent_raiseMongoWrapperException(self):
        pass

    def test_executeQuery_calledWithInvalidThirdQueryComponent_raiseMongoWrapperException(self):
        self.assertRaises(MongoWrapperException, self.sut.execute_query, query='db.collection.unsupportedOp({})')

    def test_executeQuery_calledWithInsertOneOperation_correctCallToInnerOperationMapperWithRightParams(self):
        self.__exercise_insert_one()
        self.stub_operation_mapper.format.assert_called_once_with(
            operation_params="({'data':'test', '_id': ObjectId(\"5a9442ad15b81e04322f0726\")})")

    def test_executeQuery_calledWithInsertOneOperation_correctCallToInnerResultMapperWithRightParams(self):
        self.__exercise_insert_one()
        self.stub_result_mapper.format.assert_called_once_with(
            operation_result="test_result")

    def __exercise_insert_one(self):
        self.stub_operation_mapper.format.return_value = "test"
        self.stub_pymongo_executor.execute.return_value = "test_result"
        self.sut.execute_query(
            "db.testcollection.insertOne({'data':'test', '_id': ObjectId(\"5a9442ad15b81e04322f0726\")})",
            operation_mapper=self.stub_operation_mapper, result_mapper=self.stub_result_mapper,
            pymongo_executor=self.stub_pymongo_executor)
