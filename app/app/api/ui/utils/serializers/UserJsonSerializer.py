from app.api.ui.utils.serializers.BaseJsonSerializer import BaseJsonSerializer


class UserJsonSerializer(BaseJsonSerializer):
    def to_json_dict(self, model):
        return super(UserJsonSerializer, self).to_json_dict(model)
