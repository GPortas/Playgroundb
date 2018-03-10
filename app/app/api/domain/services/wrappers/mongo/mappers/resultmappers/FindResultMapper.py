from app.api.domain.services.wrappers.mongo.mappers.resultmappers.IResultMapper import IResultMapper


class FindResultMapper(IResultMapper):

    def format(self, operation_result):
        print(str(operation_result))
        result = ''
        for document in operation_result:
            result += str(document) + '\n'
        result = result.replace("'", '"')
        return result
