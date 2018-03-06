from app.api.domain.services.wrappers.mongo.mappers.operationmappers.OperationMapperBase import OperationMapperBase


# TODO: Support "ordered" query param
class InsertManyOperationMapper(OperationMapperBase):

    def __init__(self):
        self.PYMONGO_OPERATION = 'insert_many'

    def format(self, operation_params):
        array_dict_str = operation_params[len('['):-len(']')]
        formatted_array_dict_str = self._insert_marks(array_dict_str)
        operation_params = operation_params.replace(array_dict_str, formatted_array_dict_str)
        return self.PYMONGO_OPERATION + operation_params
