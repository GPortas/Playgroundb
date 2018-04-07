from app.api.domain.models.QueryExecution import QueryExecution
from app.api.domain.services.ExerciseService import ExerciseService
from app.api.domain.services.errors.ServiceError import ServiceError
from app.api.domain.services.wrappers.mongo.MongoWrapper import MongoWrapper
from app.api.domain.services.wrappers.mongo.exceptions.MongoWrapperException import MongoWrapperException


class QueryExecutionService:

    def __init__(self, mongo_wrapper=None, exercise_service=None):
        if mongo_wrapper is None:
            self.__mongo_wrapper = MongoWrapper()
        else:
            self.__mongo_wrapper = mongo_wrapper

        if exercise_service is None:
            self.__exercise_service = ExerciseService()
        else:
            self.__exercise_service = exercise_service

    def execute_exercise_query(self, query, exercise_id):
        try:
            exercise = self.__exercise_service.get_exercise_by_id(exercise_id)
            self.__mongo_wrapper.set_collection_data(exercise.get_collection_name(), exercise.get_collection_data())
            return self.execute_query(query)
        except MongoWrapperException as mwe:
            raise ServiceError(str(mwe))

    def execute_query(self, query):
        try:
            result = self.__mongo_wrapper.execute_query(query)
            return QueryExecution(result)
        except MongoWrapperException as mwe:
            raise ServiceError(str(mwe))
