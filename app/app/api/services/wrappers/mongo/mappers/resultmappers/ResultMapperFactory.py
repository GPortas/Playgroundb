from app.api.services.wrappers.mongo.mappers.errors.InvalidOperationError import InvalidOperationError
from app.api.services.wrappers.mongo.mappers.resultmappers.InsertOneResultMapper import InsertOneResultMapper


class ResultMapperFactory:
    OPERATION_INSERT_ONE = 'insertOne'

    def create_result_mapper(self, mongo_op):
        if mongo_op == self.OPERATION_INSERT_ONE:
            return InsertOneResultMapper()
        else:
            raise InvalidOperationError('Unsupported operation ' + mongo_op)
