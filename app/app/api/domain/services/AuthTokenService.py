import hashlib
from datetime import datetime

from app.api.domain.services.errors.ServiceError import ServiceError


class AuthTokenService:

    def __init__(self, seed=None):
        if seed is not None:
            self.seed = seed
        else:
            self.seed = str(datetime.now())

    def generate_auth_token(self, user_id):
        if user_id is None:
            raise ServiceError('user_id cannot be None')
        source_str = user_id + self.seed
        md5lib = hashlib.md5()
        md5lib.update(source_str.encode("utf-8"))
        return md5lib.hexdigest()
