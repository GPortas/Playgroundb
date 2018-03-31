from app.api.ui.utils.serializers.BaseJsonSerializer import BaseJsonSerializer


class ExerciseValidationJsonSerializer(BaseJsonSerializer):

    def to_json_dict(self, model):
        return super(ExerciseValidationJsonSerializer, self).to_json_dict(model)
