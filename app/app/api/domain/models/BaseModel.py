import copy

from bson import ObjectId


class BaseModel:

    def to_json_dict(self):
        result = copy.deepcopy(self.__dict__)
        if result.get("_id") is not None:
            result["_id"] = ObjectId(result.get("_id"))
        return result
