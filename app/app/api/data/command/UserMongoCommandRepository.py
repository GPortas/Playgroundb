from app.api.data.PdbMongoBaseRepository import PdbMongoBaseRepository
from app.api.domain.services.data.command.IUserCommandRepository import IUserCommandRepository
from app.configuration import settings


class UserMongoCommandRepository(PdbMongoBaseRepository, IUserCommandRepository):

    def __init__(self):
        super(UserMongoCommandRepository, self).__init__(
            connection_uri=settings.PDB_MONGO_CONNECTION_PROPS['CONNECTION_URI'],
            db_name=settings.PDB_MONGO_CONNECTION_PROPS['DBNAME'])

    def update_user_auth_token(self, user_id, auth_token):
        self.db.users.update_one({"_id": user_id}, {"$set": {"authtoken": auth_token}})