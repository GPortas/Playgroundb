from app.api.services.wrappers.mongo.mappers.operationmappers.IOperationMapper import IOperationMapper


class InsertOneOperationMapper(IOperationMapper):

    def __init__(self):
        self.PYMONGO_OPERATION = 'insert_one'

    def format(self, operation_params):
        return self.PYMONGO_OPERATION + operation_params

