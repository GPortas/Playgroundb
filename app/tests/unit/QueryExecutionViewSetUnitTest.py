from unittest import mock

from app.api.domain.models.QueryExecution import QueryExecution
from app.api.domain.services.QueryExecutionService import QueryExecutionService
from app.api.domain.services.errors.ServiceError import ServiceError
from app.api.ui.views import QueryExecutionViewSet
from tests.unit.BaseViewSetUnitTest import BaseViewSetUnitTest


class QueryExecutionViewSetUnitTest(BaseViewSetUnitTest):

    def setUp(self):
        self.stub_query_execution_service = mock.Mock(spec=QueryExecutionService)
        self.sut = QueryExecutionViewSet(query_execution_service=self.stub_query_execution_service)

    def test_executeQuery_calledCorrectly_returnCorrectJSONResponse(self):
        json_raw = '{"query":"db.collection.find({})"}'
        request = self._configure_sut_request(json_raw)
        self.stub_query_execution_service.execute_query.return_value = QueryExecution("{'_id': ObjectId('56a942bfec926681f17f09b6'), 'name': 'foo'}")
        expected = '{"code": 0, "data": {"execution_result": "{\'_id\': ObjectId(\'56a942bfec926681f17f09b6\'), \'name\': \'foo\'}"}, "message": "query executed", "field": ""}'
        actual = self.sut.create(request)
        self._parse_and_test_response(actual, expected)

    def test_executeQuery_calledWithInvalidArgument_returnServerError(self):
        json_raw = '{"fake":"db.collection.find({})"}'
        request = self._configure_sut_request(json_raw)
        expected = '{"code": 0, "data": "", "exception_message": "\'query\'", "message": "server error", "field": ""}'
        actual = self.sut.create(request)
        self._parse_and_test_response(actual, expected)

    def test_executeQuery_calledWithInnerServiceWhichRaisesServiceError_returnCorrectJSONResponse(self):
        json_raw = '{"query":"db.collection.find({})"}'
        self.stub_query_execution_service.execute_query.side_effect = ServiceError('error')
        expected = '{"code":0,"data":"","message":"server error","field": "", "exception_message": "error"}'
        request = self._configure_sut_request(json_raw)
        actual = self.sut.create(request)
        self._parse_and_test_response(actual, expected)