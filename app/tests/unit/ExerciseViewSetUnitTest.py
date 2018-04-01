from unittest import mock

from app.api.domain.services.ExerciseService import ExerciseService
from app.api.domain.services.errors.ResourceNotFoundServiceError import ResourceNotFoundServiceError
from app.api.ui.views import ExerciseViewSet
from tests.unit.BaseViewSetUnitTest import BaseViewSetUnitTest


class ExerciseViewSetUnitTest(BaseViewSetUnitTest):

    def setUp(self):
        self.stub_exercise_service = mock.Mock(spec=ExerciseService)
        self.sut = ExerciseViewSet(exercise_service=self.stub_exercise_service)

    def test_create_called_returnCorrectJSONResponse(self):
        json_raw = '{"author": "author1", "question": "this is a question", "solution": {"item1": "item1", "item2": "item2"}, "collection_name": "testcollection"}'
        request = self._configure_sut_request(json_raw)
        expected = '{"code": 0, "data": "{}", "message": "exercise created", "field": ""}'
        self.__exercise_create_exercise(expected, request)

    def test_create_calledWithInvalidArgument_returnServerError(self):
        json_raw = '{"question": "this is a question", "solution": {"item1": "item1", "item2": "item2"}, "collection_name": "testcollection"}'
        request = self._configure_sut_request(json_raw)
        expected = '{"code": 0, "data": "", "exception_message": "\'author\'", "message": "server error", "field": ""}'
        self.__exercise_create_exercise(expected, request)

    def test_create_calledWithInnerServiceWhichRaisesResourceNotFoundServiceError_returnCorrectJSONResponse(self):
        json_raw = '{"author": "author1", "question": "this is a question", "solution": {"item1": "item1", "item2": "item2"}, "collection_name": "testcollection"}'
        self.stub_exercise_service.create_exercise.side_effect = ResourceNotFoundServiceError('error')
        expected = '{"code":0,"data":"","message":"resource not found","field": ""}'
        request = self._configure_sut_request(json_raw)
        self.__exercise_create_exercise(expected, request)

    def test_create_calledWithUserWithNoPermission_returnCorrectJSONResponse(self):
        # todo: no permissions yet
        pass

    def test_list_calledWithUserWithNoPermission_returnCorrectJSONResponse(self):
        # todo: no permissions yet
        pass

    def test_list_called_returnCorrectJSONResponse(self):
        # todo
        pass

    def __exercise_create_exercise(self, expected, request):
        actual = self.sut.create(request)
        self._parse_and_test_response(actual, expected)
