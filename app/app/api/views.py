import json

from rest_framework import permissions, viewsets
from rest_framework import status
from rest_framework.response import Response

from app.api.models.BaseModel import BaseModel
from app.api.models.Exercise import Exercise
from app.api.services.ExerciseService import ExerciseService
from app.api.services.errors.ResourceNotFoundServiceError import ResourceNotFoundServiceError
from app.api.utils.enums import ResponseType


class BaseViewSet(viewsets.ViewSet):

    def __init__(self, *args, **kwargs):
        super(BaseViewSet, self).__init__(*args, **kwargs)

    def _create_response_by_inner_service_call(self, function, *args, message=None, **kwargs):
        try:
            result = function(*args, **kwargs)
            data = '{}'
            if result is not None:
                if isinstance(result, list):
                    data = list(map(lambda x: x.to_json_dict_raw(), result))
                if isinstance(result, BaseModel):
                    data = result.to_json_dict()
            return self._create_api_response(code=0, message=message, data=data)
        except ResourceNotFoundServiceError:
            return self._create_generic_response(response_type=ResponseType.resource_not_found)
        except Exception as e:
            return self._create_generic_response(response_type=ResponseType.server_error, exception=e)

    def _create_generic_response(self, response_type=None, data='', field='', exception=None):
        if response_type is None:
            raise ValueError('Response type is needed')
        if not isinstance(response_type, ResponseType):
            raise TypeError('Invalid response type')

        status = response_type.value[0]
        code = response_type.value[1]
        message = response_type.value[2]

        return self._create_api_response(status=status, code=code, message=message, data=data, field=field,
                                         exception=exception)

    def _create_api_response(self, status=status.HTTP_200_OK, code=0, message='', data='', field='', exception=None):
        response_status = status
        response_code = code
        response_message = message
        response_field = field
        response_data = data
        response_body = {'code': response_code,
                         'message': response_message,
                         'field': response_field,
                         'data': response_data}

        exception_message = None
        if exception is not None:
            exception_message = str(exception)
        if exception_message is not None:
            response_body['exception_message'] = exception_message

        return Response(response_body, status=response_status)


class ExerciseViewSet(BaseViewSet):
    # todo: permissions
    def __init__(self, exercise_service=None, *args, **kwargs):
        if exercise_service is None:
            self.__exercise_service = ExerciseService()
        else:
            self.__exercise_service = exercise_service
        super(ExerciseViewSet, self).__init__(*args, **kwargs)

    def create(self, request):
        try:
            exercise = Exercise.from_json(request.data)
        except Exception as e:
            return self._create_generic_response(response_type=ResponseType.server_error, exception=e)

        return self._create_response_by_inner_service_call(self.__exercise_service.create_exercise,
                                                           exercise,
                                                           message='exercise created')
