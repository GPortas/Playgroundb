from app.api.domain.services.wrappers.mongo.mappers.operationmappers.OperationMapperBase import OperationMapperBase


class FindOperationMapper(OperationMapperBase):

    def __init__(self):
        self.PYMONGO_OPERATION = 'find'

    def format(self, operation_params):
        docs = operation_params[1:-1].split(",")
        for element in docs:
            operation_params = operation_params.replace(element, self._insert_marks(element))
        return self.PYMONGO_OPERATION + operation_params
