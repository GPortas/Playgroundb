from app.api.domain.models.BaseModel import BaseModel


class AuthToken(BaseModel):

    def __init__(self, hash):
        self.hash = hash

    def get_hash(self):
        return self.hash
