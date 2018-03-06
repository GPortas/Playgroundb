import unittest

from app.api.domain.services.wrappers.mongo.mappers.operationmappers.InsertManyOperationMapper import InsertManyOperationMapper


class InsertManyOperationMapperUnitTest(unittest.TestCase):

    def setUp(self):
        self.sut = InsertManyOperationMapper()

    def test_format_calledWithMultipleDocuments_returnCorrectResult(self):
        actual = self.sut.format("([ { apples  : 67},   {type :   'fuji'}])")
        expected = "insert_many([{'apples': 67}, {'type': 'fuji'}])"
        self.assertEqual(actual, expected)

    def test_format_calledWithDocumentWithInnerArray_returnCorrectResult(self):
        actual = self.sut.format(
            "([ { apples  : [   {  red: 1}, {   green: 2}]},   {type :   'fuji'}, "
            "{_id: ObjectId(\"56fc40f9d735c28df206d078\")}])")
        expected = "insert_many([{'apples': [{'red': 1}, {'green': 2}]}, {'type': 'fuji'}, " \
                   "{'_id': ObjectId(\"56fc40f9d735c28df206d078\")}])"
        self.assertEqual(actual, expected)
