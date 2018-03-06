from pymongo import MongoClient

from app.configuration import settings


class PdbMongoBaseRepository:

    def __init__(self, connection_uri=None, db_name=None):
        if connection_uri is None:
            raise ValueError("Connection URI cannot be None")
        if db_name is None:
            raise ValueError("DB name cannot be None")
        self.client = MongoClient(connection_uri,
                                  readPreference=settings.PDB_MONGO_CONNECTION_PROPS['READ_PREFERENCE'])
        self.db = self.client[db_name]

    def get_exercises_collection(self):
        return self.db.exercises
