from app.api.ui.utils.serializers.BaseJsonSerializer import BaseJsonSerializer


class UserJsonSerializer(BaseJsonSerializer):
    def to_json_dict(self, model):
        user_dict = super(UserJsonSerializer, self).to_json_dict(model)
        user_dict.pop('password', None)
        return user_dict
