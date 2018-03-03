from app.api.services.wrappers.mongo.mappers.operationmappers.InsertManyOperationMapper import InsertManyOperationMapper
from app.api.services.wrappers.mongo.mappers.operationmappers.InsertOneOperationMapper import InsertOneOperationMapper
from app.api.services.wrappers.mongo.mappers.errors.InvalidOperationError import InvalidOperationError


class OperationMapperFactory:

    OPERATION_INSERT_ONE = 'insertOne'
    OPERATION_INSERT_MANY = 'insertMany'

    def create_operation_mapper(self, mongo_op):
        if mongo_op == self.OPERATION_INSERT_ONE:
            return InsertOneOperationMapper()
        elif mongo_op == self.OPERATION_INSERT_MANY:
            return InsertManyOperationMapper()
        else:
            raise InvalidOperationError('Unsupported operation ' + mongo_op)
