import copy


class BaseJsonSerializer:

    def to_json_dict(self, model):
        result = copy.deepcopy(model.__dict__)
        if result.get("_id") is not None:
            result["_id"] = str(result.get("_id"))
        return result
