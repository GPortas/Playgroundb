import unittest

from bson import ObjectId
from pymongo import MongoClient

from app.api.domain.services.wrappers.mongo.MongoWrapper import MongoWrapper
from app.api.domain.services.wrappers.mongo.exceptions.MongoWrapperException import MongoWrapperException
from app.configuration import settings


class MongoWrapperIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.connection_uri = settings.PDB_PLAYGROUND_MONGO_CONNECTION_PROPS['CONNECTION_URI']
        self.db_name = settings.PDB_PLAYGROUND_MONGO_CONNECTION_PROPS['DBNAME']

        if self.connection_uri is None:
            raise ValueError("Connection URI cannot be None")
        if self.db_name is None:
            raise ValueError("DB name cannot be None")

        client = MongoClient(self.connection_uri,
                             readPreference=settings.PDB_MONGO_CONNECTION_PROPS['READ_PREFERENCE'])
        self.db = client[self.db_name]
        self.tearDown()
        super(MongoWrapperIntegrationTest, self).setUp()
        self.sut = MongoWrapper()

    def tearDown(self):
        self.db.testcollection.delete_many({})

    def test_getCollectionData_calledWithCorrectCollectionName_returnCollectionData(self):
        self.db.testcollection.insert_many(self.__get_test_data())
        actual = self.sut.get_collection_data('testcollection')
        expected = self.__get_test_data()
        self.assertEqual(actual, expected)

    def test_getCollectionData_calledWithUnexistentCollectionName_returnEmptyList(self):
        actual = self.sut.get_collection_data('unexistentcollection')
        expected = []
        self.assertEqual(actual, expected)

    def test_setCollectionData_calledWithValidNameAndData_dataCorreclyInsertedInCollection(self):
        data = self.__get_test_data()
        self.sut.set_collection_data(collection_name='testcollection', data=data)
        actual = self.__from_cursor_to_doc_list(self.db.testcollection.find({}))
        expected = data
        self.assertEqual(actual, expected)

    def test_setCollectionData_calledWithInvalidDataSingleDocument_raiseMongoWrapperException(self):
        self.assertRaises(MongoWrapperException, self.sut.set_collection_data, collection_name='testcollection',
                          data={"foo": 1})

    def test_setCollectionData_calledWithInvalidDataNumber_raiseMongoWrapperException(self):
        self.assertRaises(MongoWrapperException, self.sut.set_collection_data, collection_name='testcollection', data=1)

    def test_setCollectionData_calledWithInvalidDataString_raiseMongoWrapperException(self):
        self.assertRaises(MongoWrapperException, self.sut.set_collection_data, collection_name='testcollection',
                          data='test')

    def __get_test_data(self):
        return [{"foo": 1, "buu": "test1", "_id": ObjectId("4d128b6ea794fc13a8000001")},
                {"foo": 3, "buu": "test2", "_id": ObjectId("4d128b6ea794fc13a8000002")}]

    def __from_cursor_to_doc_list(self, cursor):
        result = []
        for elem in cursor:
            result.append(elem)
        return result
