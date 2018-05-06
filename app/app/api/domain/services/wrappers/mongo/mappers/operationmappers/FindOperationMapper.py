import re

from app.api.domain.services.wrappers.mongo.mappers.operationmappers.OperationMapperBase import OperationMapperBase


class FindOperationMapper(OperationMapperBase):

    def __init__(self):
        self.PYMONGO_OPERATION = 'find'

    def format(self, operation_params):
        operation_params = operation_params[1:-1]
        dict_re = re.compile(r"{.*}")
        filtered_dicts = re.findall(dict_re, operation_params)
        for element in filtered_dicts:
            operation_params = operation_params.replace(element, self._insert_marks(element))
        return self.PYMONGO_OPERATION + "(" + operation_params + ")"
