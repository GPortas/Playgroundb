from bson import ObjectId

from app.api.data.command.UserMongoCommandRepository import UserMongoCommandRepository
from app.api.domain.models.User import User
from tests.integration.PdbMongoIntegrationTestBase import PdbMongoIntegrationTestBase


class UserMongoCommandRepositoryIntegrationTest(PdbMongoIntegrationTestBase):
    def setUp(self):
        self.fixtures = []
        super(UserMongoCommandRepositoryIntegrationTest, self).setUp()
        self.sut = UserMongoCommandRepository()

    def tearDown(self):
        self.db.users.delete_many({})

    def test_updateUserAuthToken_calledWithValidAuthToken_authTokenCorrectlyUpdated(self):
        test_id = ObjectId("5aae93045b488007cb4af590")
        self.db.users.insert_one(
            {"email": "student@test.com", "password": "testpwd", "nickname": "jimmy", "role": "student",
             "_id": test_id})
        self.sut.update_user_auth_token(test_id, "testauthtoken")
        actual = User.from_json(self.db.users.find_one({"_id": test_id})).get_authtoken()
        expected = "testauthtoken"
        self.assertEqual(actual, expected)
