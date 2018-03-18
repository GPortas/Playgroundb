from app.api.domain.services.AuthTokenService import AuthTokenService
from app.api.domain.services.data.command.errors.CommandError import CommandError
from app.api.domain.services.errors.ServiceError import ServiceError
from app.api.domain.services.factories.UserCommandRepositoryFactory import UserCommandRepositoryFactory


class AuthService:

    def __init__(self, auth_token_service=None, user_command_repository=None):
        if auth_token_service is None:
            self.auth_token_service = AuthTokenService()
        else:
            self.auth_token_service = auth_token_service
        if user_command_repository is None:
            user_command_repository_factory = UserCommandRepositoryFactory()
            self.user_command_repository = user_command_repository_factory.create_user_command_repository()
        else:
            self.user_command_repository = user_command_repository

    def authenticate(self, user_id):
        try:
            auth_token = self.auth_token_service.generate_auth_token(user_id)
            self.user_command_repository.update_user_auth_token(auth_token)
        except CommandError as ce:
            raise ServiceError(str(ce))
        except ServiceError as se:
            raise ServiceError(str(se))
        return auth_token
