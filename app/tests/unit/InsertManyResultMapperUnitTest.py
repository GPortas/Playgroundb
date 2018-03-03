import unittest

from bson import ObjectId
from pymongo.results import InsertManyResult

from app.api.services.wrappers.mongo.mappers.resultmappers.InsertManyResultMapper import InsertManyResultMapper


class InsertManyResultMapperUnitTest(unittest.TestCase):

    def setUp(self):
        self.sut = InsertManyResultMapper()

    def test_format_calledWithValidOperationResult_returnCorrectResult(self):
        expected = '{\n\t"acknowledged" : ' + 'true' + ',\n\t"insertedIds" : [\n\t\t' + 'ObjectId("4d128b6ea794fc13a8000002"),\n\t\tObjectId("4d128b6ea794fc13a8000003")\n\t]' + '\n}'
        actual = self.sut.format(InsertManyResult([ObjectId("4d128b6ea794fc13a8000002"), ObjectId("4d128b6ea794fc13a8000003")], True))
        self.assertEqual(actual, expected)
