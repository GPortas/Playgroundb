from app.api.domain.models.User import User


class UserFixture:
    @staticmethod
    def fixture():
        return [
            User(_id="666f6f2d6261722d71757578", email="user1@test.com", password="testpwd1", nickname="nickname1",
                 role=User.ROLE_MASTER, score=23),
            User(_id="4d128b6ea794fc13a8000001", email="user2@test.com", password="testpwd2", nickname="nickname2",
                 role=User.ROLE_STUDENT, score=500),
            User(_id="4d128b6ea794fc13a8000002", email="user3@test.com", password="testpwd3", nickname="nickname3",
                 role=User.ROLE_STUDENT, score=340),
            User(_id="4d128b6ea794fc13a8000003", email="user4@test.com", password="testpwd4", nickname="nickname4",
                 role=User.ROLE_STUDENT, authtoken='authtoken4', score=341),
        ]

    @staticmethod
    def get_collection_name():
        return "users"
