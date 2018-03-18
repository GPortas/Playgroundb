from app.api.data.query.UserMongoQueryRepository import UserMongoQueryRepository


class UserQueryRepositoryFactory:

    def create_user_query_repository(self):
        return UserMongoQueryRepository()
