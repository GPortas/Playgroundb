from app.api.ui.utils.serializers.BaseJsonSerializer import BaseJsonSerializer


class ExerciseJsonSerializer(BaseJsonSerializer):

    def to_json_dict(self, model):
        result = super(ExerciseJsonSerializer, self).to_json_dict(model)
        result.pop('collection_data', None)
        return result

