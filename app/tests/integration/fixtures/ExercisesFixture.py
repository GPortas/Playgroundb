import json

from app.api.models.Exercise import Exercise


class ExercisesFixture:
    @staticmethod
    def fixture():
        return [
            Exercise(_id="fakeid_1", question="fakequestion_1",
                     solution=json.dumps({'key1': 'value1', 'key2': 'value2'}), author="author1"),
            Exercise(_id="fakeid_2", question="fakequestion_2",
                     solution=json.dumps({'key3': 'value3'}), author="author2"),
            Exercise(_id="fakeid_3", question="fakequestion_3",
                     solution=json.dumps({'key4': 'value4', 'key5': 'value5'}), author="author3"),
            Exercise(_id="fakeid_4", question="fakequestion_4",
                     solution=json.dumps({'key6': 'value6'}), author="author4"),
        ]
