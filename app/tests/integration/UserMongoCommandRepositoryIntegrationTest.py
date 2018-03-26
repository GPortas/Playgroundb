from bson import ObjectId

from app.api.data.command.UserMongoCommandRepository import UserMongoCommandRepository
from app.api.domain.models.User import User
from app.api.domain.services.data.command.errors.CommandError import CommandError
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

    def test_createUser_calledWithValidUser_userCorrectlyInserted(self):
        test_user = self.__get_user_test_instance()
        self.sut.create_user(test_user)
        self.assertEqual(test_user.to_json_dict(), self.db.users.find_one({"email": "testuser@test.com"}))

    def test_createUser_calledWithExistentUser_throwCommandError(self):
        user = self.__get_user_test_instance()
        self.sut.create_user(user)
        self.assertRaises(CommandError, self.sut.create_user, user)

    def __get_user_test_instance(self):
        return User(_id=ObjectId("666f6f2d6261722d71757578"), email="testuser@test.com", password="testpwd",
                    role="master", nickname="testnickname")
