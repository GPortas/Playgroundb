from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import list_route
from rest_framework.response import Response

from app.api.domain.models.BaseModel import BaseModel
from app.api.domain.models.Exercise import Exercise
from app.api.domain.models.User import User
from app.api.domain.services.AuthService import AuthService
from app.api.domain.services.ExerciseService import ExerciseService
from app.api.domain.services.QueryExecutionService import QueryExecutionService
from app.api.domain.services.ValidationService import ValidationService
from app.api.domain.services.UserFormatService import UserFormatService
from app.api.domain.services.UserService import UserService
from app.api.domain.services.errors.ResourceNotFoundServiceError import ResourceNotFoundServiceError
from app.api.domain.services.wrappers.mongo.MongoWrapper import MongoWrapper
from app.api.ui.utils.enums import ResponseType
from app.api.ui.utils.serializers.ExerciseJsonSerializer import ExerciseJsonSerializer
from app.api.ui.utils.serializers.ExerciseValidationJsonSerializer import ExerciseValidationJsonSerializer
from app.api.ui.utils.serializers.QueryExecutionJsonSerializer import QueryExecutionJsonSerializer
from app.api.ui.utils.serializers.UserJsonSerializer import UserJsonSerializer


class BaseViewSet(viewsets.ViewSet):

    def __init__(self, json_serializer, *args, **kwargs):
        self.__json_serializer = json_serializer
        super(BaseViewSet, self).__init__(*args, **kwargs)

    def _create_response_by_inner_service_call(self, function, *args, message=None, **kwargs):
        try:
            result = function(*args, **kwargs)
            data = '{}'
            if result is not None:
                if isinstance(result, list):
                    data = list(map(lambda x: self.__json_serializer.to_json_dict(x), result))
                if isinstance(result, BaseModel):
                    data = self.__json_serializer.to_json_dict(result)
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


class UserViewSet(BaseViewSet):
    def __init__(self, auth_service=None, user_service=None, *args, **kwargs):
        if auth_service is None:
            self.__auth_service = AuthService()
        else:
            self.__auth_service = auth_service
        if user_service is None:
            self.__user_service = UserService()
        else:
            self.__user_service = user_service
        super(UserViewSet, self).__init__(UserJsonSerializer(), *args, **kwargs)

    def list(self, request):
        if request.pdbuser is None:
            return self._create_generic_response(response_type=ResponseType.authentication_error)
        return self._create_response_by_inner_service_call(self.__user_service.get_ranking,
                                                           message='users retrieved')

    def create(self, request):
        nickname = request.data.get('nickname', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        role = request.data.get('role', None)
        if email is None or password is None or nickname is None or role is None:
            return self._create_generic_response(response_type=ResponseType.missing_request_field)
        try:
            user = User.from_json(request.data)
        except Exception as e:
            return self._create_generic_response(response_type=ResponseType.server_error, exception=e)
        if UserFormatService().has_valid_fields(user):
            return self._create_response_by_inner_service_call(self.__user_service.create_user,
                                                               user,
                                                               message='user created')
        else:
            return self._create_generic_response(response_type=ResponseType.invalid_field_format)

    @list_route(methods=['POST'], url_path='login')
    def login(self, request, pk=None):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        if email is None or password is None:
            return self._create_generic_response(response_type=ResponseType.missing_request_field)
        user = self.__user_service.get_user_by_credentials(email=email, password=password)
        if user is None:
            return self._create_generic_response(response_type=ResponseType.authentication_error)
        else:
            return self._create_response_by_inner_service_call(self.__auth_service.authenticate,
                                                               user.get_id(),
                                                               message='user authenticated')


class ExerciseViewSet(BaseViewSet):
    # todo: permissions
    def __init__(self, exercise_service=None, *args, **kwargs):
        if exercise_service is None:
            self.__exercise_service = ExerciseService()
        else:
            self.__exercise_service = exercise_service
        super(ExerciseViewSet, self).__init__(ExerciseJsonSerializer(), *args, **kwargs)

    def create(self, request):
        if request.pdbuser is None:
            return self._create_generic_response(response_type=ResponseType.authentication_error)
        try:
            exercise = Exercise.from_json(request.data)
            exercise.set_collection_data(MongoWrapper().get_collection_data(request.data["collection_name"]))
        except Exception as e:
            return self._create_generic_response(response_type=ResponseType.server_error, exception=e)

        return self._create_response_by_inner_service_call(self.__exercise_service.create_exercise,
                                                           exercise,
                                                           message='exercise created')

    def list(self, request):
        if request.pdbuser is None:
            return self._create_generic_response(response_type=ResponseType.authentication_error)
        return self._create_response_by_inner_service_call(self.__exercise_service.get_unsolved_exercises_by_user_id,
                                                           request.pdbuser.get_id(),
                                                           message='exercises retrieved')


class ExerciseValidationViewSet(BaseViewSet):
    # todo: permissions
    def __init__(self, solution_service=None, *args, **kwargs):
        if solution_service is None:
            self.__solution_service = ValidationService()
        else:
            self.__solution_service = solution_service
        super(ExerciseValidationViewSet, self).__init__(ExerciseValidationJsonSerializer(), *args, **kwargs)

    def create(self, request):
        if request.pdbuser is None:
            return self._create_generic_response(response_type=ResponseType.authentication_error)
        answer = request.data["answer"]
        exercise_id = request.data["exercise_id"]
        time_left = request.data["time_left"]
        return self._create_response_by_inner_service_call(self.__solution_service.validate_answer,
                                                           user_id=request.pdbuser.get_id(),
                                                           exercise_id=exercise_id,
                                                           time_left=time_left,
                                                           answer=answer,
                                                           message='exercise answer validated')


class QueryExecutionViewSet(BaseViewSet):
    # todo: permissions
    def __init__(self, query_execution_service=None, *args, **kwargs):
        if query_execution_service is not None:
            self.__query_execution_service = query_execution_service
        else:
            self.__query_execution_service = None
        super(QueryExecutionViewSet, self).__init__(QueryExecutionJsonSerializer(), *args, **kwargs)

    def create(self, request):
        user = request.pdbuser
        if user is None or user.get_role() != 'master':
            return self._create_generic_response(response_type=ResponseType.authentication_error)
        try:
            raw_query = request.data["query"]
        except Exception as e:
            return self._create_generic_response(response_type=ResponseType.server_error, exception=e)
        if self.__query_execution_service is None:
            self.__query_execution_service = QueryExecutionService()
        return self._create_response_by_inner_service_call(self.__query_execution_service.execute_query,
                                                           raw_query,
                                                           message='query executed')

    @list_route(methods=['POST'], url_path='execute-exercise-query')
    def execute_exercise_query(self, request):
        user = request.pdbuser
        if user is None:
            return self._create_generic_response(response_type=ResponseType.authentication_error)
        try:
            raw_query = request.data["query"]
            exercise_id = request.data["exercise_id"]

        except Exception as e:
            return self._create_generic_response(response_type=ResponseType.server_error, exception=e)
        if self.__query_execution_service is None:
            self.__query_execution_service = QueryExecutionService(
                mongo_wrapper=MongoWrapper(db_name=str(user.get_id())))
        return self._create_response_by_inner_service_call(self.__query_execution_service.execute_exercise_query,
                                                           raw_query,
                                                           exercise_id,
                                                           message='query executed')
