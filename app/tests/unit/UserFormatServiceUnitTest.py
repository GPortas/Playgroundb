import unittest

from ddt import data, ddt

from app.api.domain.models.User import User
from app.api.domain.services.UserFormatService import UserFormatService


@ddt
class UserFormatServiceUnitTest(unittest.TestCase):

    def setUp(self):
        self.sut = UserFormatService()

    @data(
        {'user': User(email="test1@test.com", password="test84848", role="master", nickname="jackietest")},
        {'user': User(email="O'Reilly+tag@ejyjyjjy.com", password="test84848", role="master", nickname="jackietest")},
        {'user': User(email="a@a.aa", password="testt", role="master", nickname="jac")}
    )
    def test_hasValidFields_calledWithValidUser_returnTrue(self, input):
        self.assertTrue(self.sut.has_valid_fields(input['user']))

    @data(
        {'user': User(email="test1@.com", password="test84848", role="master", nickname="jackietest")},
        {'user': User(email="assdsddad", password="test84848", role="master", nickname="jackietest")},
        {'user': User(email="aaa@aaa.a", password="testt", role="master", nickname="jac")},
        {'user': User(email="test1@test.com", password="test", role="master", nickname="jackietest")},
        {'user': User(email="test1@test.com", password="test84", role="master", nickname="ja")},
        {'user': User(email="", password="", role="master", nickname="")},
    )
    def test_hasValidFields_calledWithInvalidUser_returnFalse(self, input):
        self.assertFalse(self.sut.has_valid_fields(input['user']))
