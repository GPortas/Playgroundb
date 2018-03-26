import unittest
from unittest import mock

from ddt import ddt, data

from app.api.domain.models.User import User
from app.api.domain.services.UserService import UserService
from app.api.domain.services.data.command.IUserCommandRepository import IUserCommandRepository
from app.api.domain.services.data.command.errors.CommandError import CommandError
from app.api.domain.services.data.query.IUserQueryRepository import IUserQueryRepository
from app.api.domain.services.data.query.errors.QueryError import QueryError
from app.api.domain.services.errors.ServiceError import ServiceError


@ddt
class UserServiceUnitTest(unittest.TestCase):

    def setUp(self):
        self.stub_user_query_repository = mock.Mock(spec=IUserQueryRepository)
        self.stub_user_command_repository = mock.Mock(spec=IUserCommandRepository)
        self.sut = UserService(self.stub_user_query_repository, self.stub_user_command_repository)

    @data(
        {'email': None, 'password': 'testpwd'},
        {'email': 'test@test.com', 'password': None},
        {'email': None, 'password': None}
    )
    def test_getUserByCredentials_calledWithNoneParams_raiseValueError(self, input):
        self.assertRaises(ValueError, self.sut.get_user_by_credentials,
                          email=input['email'], password=input['password'])

    def test_getUserByCredentials_calledWithQueryRepositoryWhichRaisesQueryError_raiseServiceError(self):
        self.stub_user_query_repository.get_user_by_credentials.side_effect = QueryError()
        self.assertRaises(ServiceError, self.sut.get_user_by_credentials, email='test@test.com', password='testpwd')

    def test_getUserByCredentials_calledWithValidParams_innerQueryRepositoryCalledWithValidParams(self):
        self.sut.get_user_by_credentials('test@test.com', 'testpwd')
        self.stub_user_query_repository.get_user_by_credentials.assert_called_once_with('test@test.com',
                                                                                        'testpwd')

    def test_getUserByAuthToken_calledWithNoneParams_raiseValueError(self):
        self.assertRaises(ValueError, self.sut.get_user_by_auth_token,
                          token=None)

    def test_getUserByAuthToken_calledWithQueryRepositoryWhichRaisesQueryError_raiseServiceError(self):
        self.stub_user_query_repository.get_user_by_auth_token.side_effect = QueryError()
        self.assertRaises(ServiceError, self.sut.get_user_by_auth_token, token='faketoken')

    def test_getUserByAuthToken_calledWithValidParams_innerQueryRepositoryCalledWithValidParams(self):
        self.sut.get_user_by_auth_token('faketoken')
        self.stub_user_query_repository.get_user_by_auth_token.assert_called_once_with('faketoken')

    def test_createUser_calledWithNoneUser_raiseValueError(self):
        self.assertRaises(ValueError, self.sut.create_user, None)

    def test_createUser_calledWithExistentEmail_raiseServiceError(self):
        self.stub_user_query_repository.get_user_by_nickname.return_value = None
        self.stub_user_query_repository.get_user_by_email.return_value = self.__get_user_test_instance()
        self.assertRaises(ServiceError, self.sut.create_user, self.__get_user_test_instance())

    def test_createUser_calledWithCommandRepositoryWhichRaisesCommandError_raiseServiceError(self):
        self.stub_user_command_repository.create_user.side_effect = CommandError()
        self.assertRaises(ServiceError, self.sut.create_user, self.__get_user_test_instance())

    def test_createUser_calledWithValidParams_correctCallToInnerCommandRepositoryWithRightParams(self):
        self.stub_user_query_repository.get_user_by_nickname.return_value = None
        self.stub_user_query_repository.get_user_by_email.return_value = None
        test_user = self.__get_user_test_instance()
        self.sut.create_user(test_user)
        self.stub_user_command_repository.create_user.assert_called_once_with(test_user)

    def test_createUser_calledWithExistentNickname_raiseServiceError(self):
        self.stub_user_query_repository.get_user_by_nickname.return_value = self.__get_user_test_instance()
        self.stub_user_query_repository.get_user_by_email.return_value = None
        self.assertRaises(ServiceError, self.sut.create_user, self.__get_user_test_instance())

    def __get_user_test_instance(self):
        return User("fakeemail1@test.com", "pwdpwdpwd", "master", "testnickname")
