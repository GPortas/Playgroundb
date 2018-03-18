import unittest
from unittest import mock

from app.api.domain.services.AuthService import AuthService
from app.api.domain.services.AuthTokenService import AuthTokenService
from app.api.domain.services.data.command.IUserCommandRepository import IUserCommandRepository
from app.api.domain.services.data.command.errors.CommandError import CommandError
from app.api.domain.services.data.query.IUserQueryRepository import IUserQueryRepository
from app.api.domain.services.data.query.errors.QueryError import QueryError
from app.api.domain.services.errors.ServiceError import ServiceError


class AuthServiceUnitTest(unittest.TestCase):

    def setUp(self):
        self.stub_auth_token_service = mock.Mock(spec=AuthTokenService)
        self.stub_user_command_repository = mock.Mock(spec=IUserCommandRepository)
        self.stub_user_query_repository = mock.Mock(spec=IUserQueryRepository)
        self.sut = AuthService(user_command_repository=self.stub_user_command_repository,
                               auth_token_service=self.stub_auth_token_service,
                               user_query_repository=self.stub_user_query_repository)

    def test_authenticate_calledWithUserCommandRepositoryWhichRaisesCommandError_raiseServiceError(self):
        self.stub_auth_token_service.generate_auth_token.return_value = "fake"
        self.stub_user_command_repository.update_user_auth_token.side_effect = CommandError()
        self.assertRaises(ServiceError, self.sut.authenticate, "666f6f2d6261722d71757578")

    def test_authenticate_calledWithAuthTokenServiceWhichRaisesServiceError_raiseServiceError(self):
        self.stub_auth_token_service.generate_auth_token.side_effect = ServiceError()
        self.assertRaises(ServiceError, self.sut.authenticate, "666f6f2d6261722d71757578")

    def test_authenticate_calledWithUserQueryRepositoryWhichRaisesQueryError_raiseServiceError(self):
        self.stub_auth_token_service.generate_auth_token.return_value = "fake"
        self.stub_user_query_repository.get_user_by_id.side_effect = QueryError()
        self.assertRaises(ServiceError, self.sut.authenticate, "666f6f2d6261722d71757578")
