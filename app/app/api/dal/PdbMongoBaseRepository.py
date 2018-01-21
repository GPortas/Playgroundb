from pymongo import MongoClient

from app.configuration import settings


class PdbMongoBaseRepository:

    def __init__(self, connection_uri=None, dbname=None):
        if connection_uri is None:
            raise ValueError("Connection URI cannot be None")
        if dbname is None:
            raise ValueError("DB name cannot be None")
        self.client = MongoClient(connection_uri,
                                  readPreference=settings.PDB_MONGO_CONNECTION_PROPS['READ_PREFERENCE'])
        self.db = self.client[dbname]

    def get_exercises_collection(self):
        return self.db.exercises
