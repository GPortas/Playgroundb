import unittest

from bson import ObjectId
from pymongo import MongoClient

from app.api.services.wrappers.MongoWrapper import MongoWrapper
from app.api.services.wrappers.exceptions.MongoWrapperException import MongoWrapperException
from app.configuration import settings


class MongoWrapperFunctionalTest(unittest.TestCase):

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

        self.sut = MongoWrapper()

    def tearDown(self):
        for collection_name in self.db.collection_names():
            self.db.get_collection(collection_name).drop()

    def test_executeQuery_calledWithFindOneQuery_returnCorrectResult(self):
        self.db.playgroundtest.insert_one({"_id": ObjectId("56a942bfec926681f17f09b6"), "name": "foo"})
        actual = self.sut.execute_query(query="db.playgroundtest.findOne({})")
        expected = {'_id': ObjectId('56a942bfec926681f17f09b6'), 'name': 'foo'}
        self.assertEqual(str(sorted(expected)), str(sorted(actual)))

    def test_executeQuery_calledWithFindQuery_returnCorrectResult(self):
        self.__fill_collection_with_elements()
        actual = self.sut.execute_query(query="db.playgroundtest.find({})")
        expected = [{'_id': ObjectId('56a942bfec926681f17f09b6'), 'name': 'foo'},
                    {'_id': ObjectId('56a941afec926681f17f09b6'), 'name': 'buu'}]
        self.assertEqual(str(expected), str(actual))

    def test_executeQuery_calledWithDeleteOneCommand_returnCorrectResult(self):
        self.__fill_collection_with_elements()
        self.sut.execute_query(query="db.playgroundtest.deleteOne({'name':'foo'})")
        actual = list(self.db.playgroundtest.find({}))
        expected = [{"_id": ObjectId("56a941afec926681f17f09b6"), "name": "buu"}]
        self.assertEqual(str(expected), str(actual))

    def test_executeQuery_calledWithRemoveCommand_returnCorrectResult(self):
        self.__fill_collection_with_elements()
        self.sut.execute_query(query="db.playgroundtest.remove({})")
        actual = list(self.db.playgroundtest.find({}))
        expected = []
        self.assertEqual(str(expected), str(actual))

    def __fill_collection_with_elements(self):
        self.db.playgroundtest.insert_one({"_id": ObjectId("56a942bfec926681f17f09b6"), "name": "foo"})
        self.db.playgroundtest.insert_one({"_id": ObjectId("56a941afec926681f17f09b6"), "name": "buu"})

    def test_executeQuery_calledWithInvalidQueryOrCommand_raiseMongoWrapperException(self):
        self.assertRaises(MongoWrapperException, self.sut.execute_query, "db.playgroundtest.fakecommand({})")

    #TODO: IMPROVE TEST COVERAGE FOR MORE CASES
