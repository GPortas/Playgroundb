from app.api.domain.services.data.query.errors.QueryError import QueryError
from app.api.domain.services.errors.ServiceError import ServiceError
from app.api.domain.services.factories.UserCommandRepositoryFactory import UserCommandRepositoryFactory
from app.api.domain.services.factories.UserQueryRepositoryFactory import UserQueryRepositoryFactory


class UserService:
    def __init__(self, user_query_repository=None, user_command_repository=None):
        if user_query_repository is not None:
            self.__user_query_repository = user_query_repository
        else:
            user_query_repository_factory = UserQueryRepositoryFactory()
            self.__user_query_repository = user_query_repository_factory.create_user_query_repository()

        if user_command_repository is not None:
            self.__user_command_repository = user_command_repository
        else:
            user_command_repository_factory = UserCommandRepositoryFactory()
            self.__user_command_repository = user_command_repository_factory.create_user_command_repository()

    def get_user_by_credentials(self, email, password):
        if email is None:
            raise ValueError('email cannot be None')
        if password is None:
            raise ValueError('password cannot be None')
        try:
            return self.__user_query_repository.get_user_by_credentials(email, password)
        except QueryError as qe:
            raise ServiceError(str(qe))
