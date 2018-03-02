import unittest

from app.api.services.wrappers.mongo.mappers.operationmappers.InsertOneOperationMapper import InsertOneOperationMapper


class InsertOneOperationMapperUnitTest(unittest.TestCase):

    def setUp(self):
        self.sut = InsertOneOperationMapper()

    def test_format_calledWithSingleObjectIdDocument_returnCorrectResult(self):
        actual = self.sut.format("({_id: ObjectId(\"56fc40f9d735c28df206d078\")})")
        expected = "insert_one({'_id': ObjectId(\"56fc40f9d735c28df206d078\")})"
        self.assertEqual(actual, expected)

    def test_format_calledWithMultipleKeysDocument_returnCorrectResult(self):
        actual = self.sut.format("({  apples  : 67   , type :   'fuji'})")
        expected1 = "insert_one({'apples': 67, 'type': 'fuji'})"
        expected2 = "insert_one({'type': 'fuji', 'apples': 67})"
        #TODO: Improve mapper to return always ordered dicts to avoid this kind of assertion
        self.assertTrue(actual == expected1 or actual == expected2)
