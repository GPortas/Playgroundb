from app.api.data.PdbMongoBaseRepository import PdbMongoBaseRepository
from app.api.domain.models.User import User
from app.api.domain.services.data.query.IUserQueryRepository import IUserQueryRepository
from app.configuration import settings


class UserMongoQueryRepository(IUserQueryRepository, PdbMongoBaseRepository):

    def __init__(self):
        super(UserMongoQueryRepository, self).__init__(
            connection_uri=settings.PDB_MONGO_CONNECTION_PROPS['CONNECTION_URI'],
            db_name=settings.PDB_MONGO_CONNECTION_PROPS['DBNAME'])

    def get_user_by_credentials(self, email, password):
        result = self.db.users.find_one({"email": email, "password": password},
                                        {'_id': 1, 'email': 1, 'password': 1, 'nickname': 1, 'authtoken': 1, 'role': 1})
        if result is not None:
            result = User.from_json(result)
        return result

    def get_user_by_id(self, user_id):
        pass
