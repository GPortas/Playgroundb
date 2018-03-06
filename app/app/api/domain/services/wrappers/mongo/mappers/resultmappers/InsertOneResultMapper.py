from app.api.domain.services.wrappers.mongo.mappers.resultmappers.IResultMapper import IResultMapper


class InsertOneResultMapper(IResultMapper):

    def format(self, operation_result):
        result = '{\n\t"acknowledged" : ' + str(
            operation_result.acknowledged).lower() + ',\n\t"insertedId" : ObjectId("' + str(
            operation_result.inserted_id) + '")\n}'
        return result
