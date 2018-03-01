import unittest
from unittest import mock

from bson import ObjectId
from pymongo.results import InsertOneResult

from app.api.services.wrappers.mongo.mappers.resultmappers.InsertOneResultMapper import InsertOneResultMapper


class InsertOneResultMapperUnitTest(unittest.TestCase):

    def setUp(self):
        self.sut = InsertOneResultMapper()

    def test_format_calledWithValidOperationParams_returnCorrectResult(self):
        # TODO: Mock class property
        stub_insert_one_result = mock.Mock(spec=InsertOneResult)
        stub_insert_one_result.inserted_id = mock.PropertyMock(return_value=ObjectId("4d128b6ea794fc13a8000002"))
        stub_insert_one_result.acknowledged = mock.PropertyMock(return_value=True)

        with mock.patch(InsertOneResult.inserted_id, new_callable=mock.PropertyMock) as mock_my_property:
            mock_my_property.return_value = 'my value'

        expected = '{\n\t"acknowledged" : ' + 'true' + ',\n\t"insertedId" : ObjectId("4d128b6ea794fc13a8000002")\n}'
        actual = self.sut.format(stub_insert_one_result)

        self.assertEqual(actual, expected)
