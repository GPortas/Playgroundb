import unittest

from app.api.domain.services.wrappers.mongo.mappers.operationmappers.FindOperationMapper import FindOperationMapper


class FindOperationMapperUnitTest(unittest.TestCase):

    def setUp(self):
        self.sut = FindOperationMapper()

    def test_format_calledWithEmptyQuery_returnCorrectResult(self):
        actual = self.sut.format("({})")
        expected = "find({})"
        self.assertEqual(actual, expected)

    def test_format_calledWithFilledQuery_returnCorrectResult(self):
        actual = self.sut.format("({ qty: { $gt: 4 } })")
        expected = "find({'qty': {'$gt': 4}})"
        self.assertEqual(actual, expected)

    def test_format_calledWithFilledQueryAndProjection_returnCorrectResult(self):
        actual = self.sut.format("({ qty: { $gt: 4 } },{  type     : 1})")
        expected = "find({'qty': {'$gt': 4}},{'type': 1})"
        self.assertEqual(actual, expected)
