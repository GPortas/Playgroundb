from app.api.services.wrappers.mongo.mappers.resultmappers.IResultMapper import IResultMapper


class InsertManyResultMapper(IResultMapper):

    def format(self, operation_result):
        result = '{\n\t"acknowledged" : ' + str(
            operation_result.acknowledged).lower() + ',\n\t"insertedIds" : [\n\t\t'
        for object_id in operation_result.inserted_ids:
            result = result + 'ObjectId("' + str(object_id) + '")' + ",\n\t\t"
        result = result[:-4]
        result = result + '\n\t]\n}'
        return result
