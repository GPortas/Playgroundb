from pymongo import MongoClient

from app.configuration import settings
from tests.integration.IntegrationTestBase import IntegrationTestBase

from tests.integration.fixtures.ExerciseFixture import *
from tests.integration.fixtures.UserFixture import *


class PdbMongoIntegrationTestBase(IntegrationTestBase):
    def setUp(self):
        self.connection_uri = settings.PDB_MONGO_CONNECTION_PROPS['CONNECTION_URI']
        self.db_name = settings.PDB_MONGO_CONNECTION_PROPS['DBNAME']

        if self.connection_uri is None:
            raise ValueError("Connection URI cannot be None")
        if self.db_name is None:
            raise ValueError("DB name cannot be None")

        client = MongoClient(self.connection_uri,
                             readPreference=settings.PDB_MONGO_CONNECTION_PROPS['READ_PREFERENCE'])
        self.db = client[self.db_name]
        self.tearDown()
        super(PdbMongoIntegrationTestBase, self).setUp()

    def tearDown(self):
        for item in self.fixtures:
            collection = eval("self.db." + eval(item).get_collection_name())
            collection.delete_many({})

    def saveObject(self, object_item):
        collection = eval("self.db." + eval(object_item.__class__.__name__ + "Fixture").get_collection_name())
        json_object = object_item.to_json_dict()
        collection.insert_one(json_object)
