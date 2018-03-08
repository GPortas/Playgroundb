from app.api.ui.utils.serializers.BaseJsonSerializer import BaseJsonSerializer


class QueryExecutionJsonSerializer(BaseJsonSerializer):
    
    def to_json_dict(self, model):
        return super(QueryExecutionJsonSerializer, self).to_json_dict(model)
