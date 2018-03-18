from app.api.data.command.UserMongoCommandRepository import UserMongoCommandRepository


class UserCommandRepositoryFactory:

    def create_user_command_repository(self):
        return UserMongoCommandRepository()
