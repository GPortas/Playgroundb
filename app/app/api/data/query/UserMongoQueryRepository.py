from app.api.data.PdbMongoBaseRepository import PdbMongoBaseRepository
from app.api.domain.models.User import User
from app.api.domain.services.data.query.IUserQueryRepository import IUserQueryRepository
from app.configuration import settings


class UserMongoQueryRepository(IUserQueryRepository, PdbMongoBaseRepository):
    ITEM_REQUIRED_FIELDS = {'_id': 1, 'email': 1, 'password': 1, 'nickname': 1, 'authtoken': 1, 'role': 1, 'score': 1}
    RANKING_LENGTH = 20

    def __init__(self):
        super(UserMongoQueryRepository, self).__init__(
            connection_uri=settings.PDB_MONGO_CONNECTION_PROPS['CONNECTION_URI'],
            db_name=settings.PDB_MONGO_CONNECTION_PROPS['DBNAME'])

    def get_user_by_credentials(self, email, password):
        result = self.db.users.find_one({"email": email, "password": password},
                                        self.ITEM_REQUIRED_FIELDS)
        result = self.__from_json_to_domain_model(result)
        return result

    def get_user_by_id(self, user_id):
        result = self.db.users.find_one({"_id": user_id},
                                        self.ITEM_REQUIRED_FIELDS)
        result = self.__from_json_to_domain_model(result)
        return result

    def get_user_by_auth_token(self, token):
        result = self.db.users.find_one({"authtoken": token},
                                        self.ITEM_REQUIRED_FIELDS)
        result = self.__from_json_to_domain_model(result)
        return result

    def get_user_by_email(self, email):
        result = self.db.users.find_one({"email": email},
                                        self.ITEM_REQUIRED_FIELDS)
        result = self.__from_json_to_domain_model(result)
        return result

    def get_user_by_nickname(self, nickname):
        result = self.db.users.find_one({"nickname": nickname},
                                        self.ITEM_REQUIRED_FIELDS)
        result = self.__from_json_to_domain_model(result)
        return result

    def get_ranking(self, length=RANKING_LENGTH):
        result = self.db.users.find({}, self.ITEM_REQUIRED_FIELDS).limit(length).sort([('score', -1)])
        result_list = []
        for item in result:
            result_list.append(self.__from_json_to_domain_model(item))
        return result_list

    def __from_json_to_domain_model(self, result):
        if result is not None:
            result = User.from_json(result)
        return result
