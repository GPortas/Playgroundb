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