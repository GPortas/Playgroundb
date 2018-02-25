import unittest

from app.api.services.wrappers.mongo.MongoWrapper import MongoWrapper
from app.api.services.wrappers.mongo.exceptions.MongoWrapperException import MongoWrapperException


class MongoWrapperUnitTest(unittest.TestCase):

    def setUp(self):
        self.sut = MongoWrapper()

    def test_executeQuery_calledWithInvalidFirstQueryComponent_raiseMongoWrapperException(self):
        self.assertRaises(MongoWrapperException, self.sut.execute_query, query='dx.collection.find({})')

    def test_executeQuery_calledWithInvalidSecondQueryComponent_raiseMongoWrapperException(self):
        pass

    def test_executeQuery_calledWithInvalidThirdQueryComponent_raiseMongoWrapperException(self):
        self.assertRaises(MongoWrapperException, self.sut.execute_query, query='db.collection.unsupportedOp({})')

    def test_executeQuery_calledWithInsertOneOperation_returnCorrectResult(self):
        actual = self.sut.execute_query("db.testcollection.insertOne({'data':'test'})")
        self.assertEqual(str(actual), "fake")
