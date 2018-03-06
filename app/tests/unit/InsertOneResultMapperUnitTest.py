import unittest

from bson import ObjectId
from pymongo.results import InsertOneResult

from app.api.domain.services.wrappers.mongo.mappers.resultmappers.InsertOneResultMapper import InsertOneResultMapper


class InsertOneResultMapperUnitTest(unittest.TestCase):

    def setUp(self):
        self.sut = InsertOneResultMapper()

    def test_format_calledWithValidOperationResult_returnCorrectResult(self):
        expected = '{\n\t"acknowledged" : ' + 'true' + ',\n\t"insertedId" : ' + 'ObjectId("4d128b6ea794fc13a8000002")' + '\n}'
        actual = self.sut.format(InsertOneResult(ObjectId("4d128b6ea794fc13a8000002"), True))
        self.assertEqual(actual, expected)
