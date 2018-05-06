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
        expected = "find({'qty': {'$gt': 4}}, {'type': 1})"
        self.assertEqual(actual, expected)

    def test_format_calledWithQueryWithTwoQuantityConditions_returnCorrectResult(self):
        actual = self.sut.format("({dinero: { $gte: 22356 }, edad: {$gte: 38} })")
        expected_results = ["find({'edad': {'$gte': 38}, 'dinero': {'$gte': 22356}})", "find({'dinero': {'$gte': 22356}, 'edad': {'$gte': 38}})"]
        self.assertTrue(expected_results.__contains__(actual))

    def test_format_calledWithFilledQueryAndProjectionWith1sand0s_returnCorrectResult(self):
        actual = self.sut.format('({"autor.apellidos":"DATE"},{autor: 1, _id:0})')
        expected_results = ["find({'autor.apellidos': 'DATE'}, {'_id': 0, 'autor': 1})","find({'autor.apellidos': 'DATE'}, {'autor': 1, '_id': 0})"]
        self.assertTrue(expected_results.__contains__(actual))

    def test_format_calledWithQueryWithQuantityConditionsAndProjectionWith1sand0s_returnCorrectResult(self):
        actual = self.sut.format('({"precio": {$gt:50}},{titulo:1, _id:0})')
        expected_results = ["find({'precio': {'$gt': 50}}, {'titulo': 1, '_id': 0})","find({'precio': {'$gt': 50}}, {'_id': 0, 'titulo': 1})"]
        self.assertTrue(expected_results.__contains__(actual))
