import unittest

from app.api.services.wrappers.mongo.mappers.operationmappers.InsertOneOperationMapper import InsertOneOperationMapper


class InsertOneOperationMapperUnitTest(unittest.TestCase):

    def setUp(self):
        self.sut = InsertOneOperationMapper()

    def test_format_calledWithValidOperationParams_returnCorrectResult(self):
        actual = self.sut.format("({'data': 1, 'apples': '23', 'type': 'fuji'})")
        expected = "insert_one({'data': 1, 'apples': '23', 'type': 'fuji'})"
        self.assertEqual(actual, expected)
