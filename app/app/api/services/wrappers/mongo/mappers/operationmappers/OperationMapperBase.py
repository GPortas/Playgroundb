import re


class OperationMapperBase:
    PYMONGO_OPERATION = ''

    REGEX_UNMARKED_VARIABLES = '[^\s,{]+[:]'

    def format(self, operation_params):
        pass

    def _insert_marks(self, operation_params):
        operation_params = operation_params.replace(" ", "")
        pattern = re.compile(self.REGEX_UNMARKED_VARIABLES)
        filtered_text = re.findall(pattern, operation_params)
        for element in filtered_text:
            operation_params = operation_params.replace(element, "\'" + element[:-1] + "\':")
        return operation_params

