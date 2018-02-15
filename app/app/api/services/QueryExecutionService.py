from app.api.models.QueryExecution import QueryExecution
from app.api.services.errors.ServiceError import ServiceError
from app.api.services.wrappers.MongoWrapper import MongoWrapper
from app.api.services.wrappers.exceptions.MongoWrapperException import MongoWrapperException


class QueryExecutionService:

    def __init__(self, mongo_wrapper=None):
        if mongo_wrapper is None:
            self.__mongo_wrapper = MongoWrapper()
        else:
            self.__mongo_wrapper = mongo_wrapper

    def execute_query(self, query):
        try:
            result = self.__mongo_wrapper.execute_query(query)
            return QueryExecution(result)
        except MongoWrapperException as mwe:
            raise ServiceError(str(mwe))
