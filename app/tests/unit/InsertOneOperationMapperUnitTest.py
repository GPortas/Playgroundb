import unittest

from ddt import data, ddt

from app.api.services.wrappers.mongo.mappers.operationmappers.InsertOneOperationMapper import InsertOneOperationMapper


@ddt
class InsertOneOperationMapperUnitTest(unittest.TestCase):

    def setUp(self):
        self.sut = InsertOneOperationMapper()

    @data(
        {'input': "({_id: ObjectId(\"56fc40f9d735c28df206d078\")})",
         'expected': "insert_one({'_id': ObjectId(\"56fc40f9d735c28df206d078\")})"},
        {'input': "({  apples  : 67   , type :   'fuji'})",
         'expected': "insert_one({'apples': 67, 'type': 'fuji'})"})
    def test_format_calledWithValidOperationParams_returnCorrectResult(self, data):
        actual = self.sut.format(data['input'])
        expected = data['expected']

        print('###############')
        print("act:" + actual)
        print("exp:" + data['expected'])
        self.assertEqual(actual, expected)
