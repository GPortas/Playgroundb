from app.api.services.wrappers.mongo.mappers.operationmappers.OperationMapperBase import OperationMapperBase


class InsertOneOperationMapper(OperationMapperBase):

    def __init__(self):
        self.PYMONGO_OPERATION = 'insert_one'

    def format(self, operation_params):
        operation_params = "(" + self._insert_marks(operation_params[1:-1]) + ")"
        return self.PYMONGO_OPERATION + operation_params
