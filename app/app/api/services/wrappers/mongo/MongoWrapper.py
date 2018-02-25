from pymongo import MongoClient

from app.api.services.wrappers.mongo.exceptions.MongoWrapperException import MongoWrapperException
from app.api.services.wrappers.mongo.mappers.operationmappers.OperationMapperFactory import OperationMapperFactory
from app.api.services.wrappers.mongo.mappers.errors.InvalidOperationError import InvalidOperationError
from app.api.services.wrappers.mongo.mappers.resultmappers.ResultMapperFactory import ResultMapperFactory
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
        if query_components[0] != 'db':
            raise MongoWrapperException('Please, insert a valid operation')
        else:
            try:
                mongo_op_name = query_components[2].split('(')[0]
                mongo_op_params = '(' + query_components[2].split('(')[1]

                operation_mapper = OperationMapperFactory().create_operation_mapper(mongo_op=mongo_op_name)
                full_operation = operation_mapper.format(operation_params=mongo_op_params)
                pymongo_query = 'self.' + query_components[0] + '.' + query_components[1] + '.' + full_operation

                pymongo_operation_result = eval(pymongo_query)

                result_mapper = ResultMapperFactory().create_result_mapper(mongo_op=mongo_op_name)
                result = result_mapper.format(operation_result=pymongo_operation_result)

                return result
            except InvalidOperationError as ioe:
                raise MongoWrapperException(str(ioe))
