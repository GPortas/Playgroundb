from app.api.services.wrappers.mongo.mappers.resultmappers.IResultMapper import IResultMapper


class InsertOneResultMapper(IResultMapper):

    def format(self, operation_result):
        return 'fake'
