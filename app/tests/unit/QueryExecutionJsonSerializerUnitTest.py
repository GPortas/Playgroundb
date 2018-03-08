import unittest

from app.api.domain.models.QueryExecution import QueryExecution
from app.api.ui.utils.serializers.QueryExecutionJsonSerializer import QueryExecutionJsonSerializer


class QueryExecutionJsonSerializerUnitTest(unittest.TestCase):

    def setUp(self):
        self.sut = QueryExecutionJsonSerializer()

    def test_toJsonDict_calledWithQueryExecution_returnCorrectResult(self):
        source_qe = QueryExecution(execution_result="{data: 2}")
        actual = self.sut.to_json_dict(source_qe)
        expected = {'execution_result': "{data: 2}"}
        self.assertEqual(actual, expected)
