import unittest

from ddt import data, ddt

from app.api.services.wrappers.mongo.mappers.operationmappers.InsertOneOperationMapper import InsertOneOperationMapper


@ddt
class InsertOneOperationMapperUnitTest(unittest.TestCase):

    def setUp(self):
        self.sut = InsertOneOperationMapper()

    @data(
        {'input': "({data: 1, apples: '23',type: 'fuji'})",
         'expected': "insert_one({'data':1,'apples':'23','type':'fuji'})"},
        {'input': "({ data:    1, apples  : '23'  ,  type:     'fuji'})",
         'expected': "insert_one({'data':1,'apples':'23','type':'fuji'})"}

    )
    def test_format_calledWithValidOperationParams_returnCorrectResult(self, data):
        actual = self.sut.format(data['input'])
        expected = data['expected']
        self.assertEqual(actual, expected)
