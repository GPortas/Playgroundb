import unittest

from bson import ObjectId
from pymongo.cursor import Cursor

from app.api.domain.services.wrappers.mongo.mappers.resultmappers.FindResultMapper import FindResultMapper

#TODO: Cover test case
class FindResultMapperUnitTest(unittest.TestCase):

    def setUp(self):
        self.sut = FindResultMapper()

    def test_format_calledWithValidOperationParams_returnCorrectResult(self):
        # actual = self.sut.format(Cursor([{'_id': ObjectId('5a984e8115b81e070bc1e265'), 'data': 1},
        #                                 {'_id': ObjectId('5a9ac89f15b81e19636947d3'), 'kaki': 1}]))
        # expected = "{'_id': ObjectId('5a984e8115b81e070bc1e265'), 'data': 1}\n" \
        #           "{'_id': ObjectId('5a9ac89f15b81e19636947d3'), 'kaki': 1}"
        # self.assertEqual(actual, expected)
        pass
