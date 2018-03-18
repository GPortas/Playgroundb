from app.api.domain.models.BaseModel import BaseModel


class User(BaseModel):

    def __init__(self, email, password, nickname=None, _id=None):
        if _id is not None:
            self._id = _id
        self.email = email
        self.password = password
        self.nickname = nickname

    def get_id(self):
        return self._id

    def get_nickname(self):
        return self.nickname

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    @staticmethod
    def from_json(json_source):
        user = User(email=json_source["email"], _id=json_source.get("_id"),
                    password=json_source["password"],
                    nickname=json_source.get("nickname"))
        return user
