from app.api.domain.services.AuthTokenService import AuthTokenService
from app.api.domain.services.data.command.errors.CommandError import CommandError
from app.api.domain.services.data.query.errors.QueryError import QueryError
from app.api.domain.services.errors.ServiceError import ServiceError
from app.api.domain.services.factories.UserCommandRepositoryFactory import UserCommandRepositoryFactory
from app.api.domain.services.factories.UserQueryRepositoryFactory import UserQueryRepositoryFactory


class AuthService:

    def __init__(self, auth_token_service=None, user_command_repository=None, user_query_repository=None):
        if auth_token_service is None:
            self.auth_token_service = AuthTokenService()
        else:
            self.auth_token_service = auth_token_service
        if user_command_repository is None:
            user_command_repository_factory = UserCommandRepositoryFactory()
            self.user_command_repository = user_command_repository_factory.create_user_command_repository()
        else:
            self.user_command_repository = user_command_repository

        if user_query_repository is None:
            user_query_repository_factory = UserQueryRepositoryFactory()
            self.user_query_repository = user_query_repository_factory.create_user_query_repository()
        else:
            self.user_query_repository = user_query_repository

    def authenticate(self, user_id):
        try:
            auth_token = self.auth_token_service.generate_auth_token(user_id)
            self.user_command_repository.update_user_auth_token(user_id, auth_token)
            user = self.user_query_repository.get_user_by_id(user_id)
        except CommandError as ce:
            raise ServiceError(str(ce))
        except QueryError as qe:
            raise ServiceError(str(qe))
        except ServiceError as se:
            raise ServiceError(str(se))
        return user

