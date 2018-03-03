from app.api.services.wrappers.mongo.mappers.errors.InvalidOperationError import InvalidOperationError
from app.api.services.wrappers.mongo.mappers.resultmappers.InsertManyResultMapper import InsertManyResultMapper
from app.api.services.wrappers.mongo.mappers.resultmappers.InsertOneResultMapper import InsertOneResultMapper


class ResultMapperFactory:
    OPERATION_INSERT_ONE = 'insertOne'
    OPERATION_INSERT_MANY = 'insertMany'

    def create_result_mapper(self, mongo_op):
        if mongo_op == self.OPERATION_INSERT_ONE:
            return InsertOneResultMapper()
        elif mongo_op == self.OPERATION_INSERT_MANY:
            return InsertManyResultMapper()
        else:
            raise InvalidOperationError('Unsupported operation ' + mongo_op)
