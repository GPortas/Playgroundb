class IUserCommandRepository:

    def create_user(self, user):
        pass

    def update_user_auth_token(self, user_id, auth_token):
        pass

    def increment_user_score(self, user_id, score):
        pass
