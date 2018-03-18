import unittest

from app.api.domain.services.AuthTokenService import AuthTokenService
from app.api.domain.services.errors.ServiceError import ServiceError


class AuthTokenServiceUnitTest(unittest.TestCase):

    def setUp(self):
        self.sut = AuthTokenService(seed="testseed")

    def test_generateAuthToken_calledWithNoneUser_raiseServiceError(self):
        self.assertRaises(ServiceError, self.sut.generate_auth_token, None)

    def test_generateAuthToken_calledWithValidUser_returnCorrectResult(self):
        actual = self.sut.generate_auth_token("666f6f2d6261722d71757578")
        expected = "4dc757b637455caf880d775192d6040d"
        self.assertEqual(actual.get_hash(), expected)
