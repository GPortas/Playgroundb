import json

from app.api.domain.models.Exercise import Exercise


class ExerciseFixture:
    @staticmethod
    def fixture():
        return [
            Exercise(_id="666f6f2d6261722d71757578", question="fakequestion_1",
                     solution=json.dumps({'key1': 'value1', 'key2': 'value2'}), author="author1"),
            Exercise(_id="4d128b6ea794fc13a8000001", question="fakequestion_2",
                     solution=json.dumps({'key3': 'value3'}), author="author2"),
            Exercise(_id="4d128b6ea794fc13a8000002", question="fakequestion_3",
                     solution=json.dumps({'key4': 'value4', 'key5': 'value5'}), author="author3"),
            Exercise(_id="4d128b6ea794fc13a8000003", question="fakequestion_4",
                     solution=json.dumps({'key6': 'value6'}), author="author4"),
        ]

    @staticmethod
    def get_collection_name():
        return "exercises"
