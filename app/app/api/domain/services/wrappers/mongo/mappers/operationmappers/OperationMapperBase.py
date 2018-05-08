import re

from demjson import decode, JSONDecodeError


class OperationMapperBase:
    PYMONGO_OPERATION = ''

    def format(self, operation_params):
        pass

    def _insert_marks(self, operation_params):
        object_id_re = re.compile('ObjectId\\(["\\\'][0-9a-f]+["\\\']\\)')
        filtered_text = re.findall(object_id_re, operation_params)
        for element in filtered_text:
            operation_params = operation_params.replace(element, "'" + element + "'")
        operation_params = str(decode('[' + operation_params + ']'))
        operation_params = operation_params[1:-1]
        for element in filtered_text:
            operation_params = operation_params.replace("'" + element + "'", element)
        return operation_params
