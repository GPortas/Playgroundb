from app.api.services.wrappers.mongo.mappers.operationmappers.InsertOneOperationMapper import InsertOneOperationMapper
from app.api.services.wrappers.mongo.mappers.errors.InvalidOperationError import InvalidOperationError


class OperationMapperFactory:

    OPERATION_INSERT_ONE = 'insertOne'
    OPERATION_INSERT_MANY = 'find'

    def create_operation_mapper(self, mongo_op):
        if mongo_op == self.OPERATION_INSERT_ONE:
            return InsertOneOperationMapper()
        else:
            raise InvalidOperationError('Unsupported operation ' + mongo_op)
