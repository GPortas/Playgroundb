import re
from bson import Code
from pymongo import MongoClient
from pymongo.errors import OperationFailure

from app.api.services.wrappers.exceptions.MongoWrapperException import MongoWrapperException
from app.configuration import settings


class MongoWrapper:

    def __init__(self):
        self.connection_uri = settings.PDB_PLAYGROUND_MONGO_CONNECTION_PROPS['CONNECTION_URI']
        self.db_name = settings.PDB_PLAYGROUND_MONGO_CONNECTION_PROPS['DBNAME']

        if self.connection_uri is None:
            raise ValueError("Connection URI cannot be None")
        if self.db_name is None:
            raise ValueError("DB name cannot be None")

        client = MongoClient(self.connection_uri,
                             readPreference=settings.PDB_MONGO_CONNECTION_PROPS['READ_PREFERENCE'])
        self.db = client[self.db_name]

    def execute_query(self, query):
        query_components = query.split(".")
        not_eval_ops = re.compile('find\(')
        try:
            if not_eval_ops.search(query_components[2]):
                result = list(eval("self." + query))
            else:
                result = self.db.eval(Code('function () { return ' + query + ' }'))
            return result
        except OperationFailure as of:
            raise MongoWrapperException(str(of))
