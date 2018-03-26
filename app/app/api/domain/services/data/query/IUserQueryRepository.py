class IUserQueryRepository:

    def get_user_by_credentials(self, email, password):
        pass

    def get_user_by_id(self, user_id):
        pass

    def get_user_by_auth_token(self, token):
        pass

    def get_user_by_email(self, email):
        pass

    def get_user_by_nickname(self, nickname):
        pass
