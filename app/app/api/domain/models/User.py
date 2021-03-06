from app.api.domain.models.BaseModel import BaseModel


class User(BaseModel):
    ROLE_MASTER = "master"
    ROLE_STUDENT = "student"

    def __init__(self, email, password, role, nickname, _id=None, authtoken=None, score=None):
        if _id is not None:
            self._id = _id
        self.email = email.lower()
        self.password = password
        self.nickname = nickname
        self.role = role
        self.authtoken = authtoken
        if score is not None:
            self.score = score
        else:
            self.score = 0

    def get_id(self):
        return self._id

    def get_nickname(self):
        return self.nickname

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_authtoken(self):
        return self.authtoken

    def get_role(self):
        return self.role

    def get_score(self):
        return self.score

    @staticmethod
    def from_json(json_source):
        user = User(email=json_source["email"], _id=json_source.get("_id"),
                    password=json_source["password"],
                    role=json_source["role"],
                    nickname=json_source["nickname"],
                    authtoken=json_source.get("authtoken"),
                    score=json_source.get("score"))
        return user
