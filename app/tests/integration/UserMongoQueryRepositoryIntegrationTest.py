from bson import ObjectId

from app.api.data.query.UserMongoQueryRepository import UserMongoQueryRepository
from tests.integration.PdbMongoIntegrationTestBase import PdbMongoIntegrationTestBase


class UserMongoQueryRepositoryIntegrationTest(PdbMongoIntegrationTestBase):
    def setUp(self):
        self.fixtures = ['User']
        super(UserMongoQueryRepositoryIntegrationTest, self).setUp()
        self.sut = UserMongoQueryRepository()

    def tearDown(self):
        self.db.users.delete_many({})

    def test_getUserByCredentials_calledWithValidCredentials_returnCorrectUser(self):
        actual = self.sut.get_user_by_credentials(email="user1@test.com", password="testpwd1")
        self.assertEqual(actual.get_email(), "user1@test.com")

    def test_getUserByCredentials_calledWithInvalidCredentials_returnNone(self):
        actual = self.sut.get_user_by_credentials(email="invalidmail@test.com", password="testpwd1")
        self.assertEqual(actual, None)

    def test_getUserById_calledWithExistentUserId_returnCorrectUser(self):
        actual = self.sut.get_user_by_id(user_id=ObjectId("666f6f2d6261722d71757578"))
        self.assertEqual(actual.get_email(), "user1@test.com")

    def test_getUserByAuthToken_calledWithValidAuthToken_returnCorrectUser(self):
        actual = self.sut.get_user_by_auth_token(token='authtoken4')
        self.assertEqual(actual.get_email(), "user4@test.com")

    def test_getUserByAuthToken_calledWithInvalidAuthToken_returnNone(self):
        actual = self.sut.get_user_by_auth_token(token="invalidtoken")
        self.assertEqual(actual, None)
