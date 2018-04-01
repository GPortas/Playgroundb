from app.api.domain.models.Exercise import Exercise


class ExerciseFixture:
    @staticmethod
    def fixture():
        return [
            Exercise(author="author1", collection_name="testcollection", collection_data="testdata",
                     question="fakequestion_1", solution="testsolution", _id="666f6f2d6261722d71757578"),
            Exercise(author="author2", collection_name="testcollection", collection_data="testdata",
                     question="fakequestion_2", solution="testsolution", _id="4d128b6ea794fc13a8000001"),
            Exercise(author="author3", collection_name="testcollection", collection_data="testdata",
                     question="fakequestion_3", solution="testsolution", _id="4d128b6ea794fc13a8000002"),
            Exercise(author="author4", collection_name="testcollection", collection_data="testdata",
                     question="fakequestion_4", solution="testsolution", _id="4d128b6ea794fc13a8000003"),
        ]

    @staticmethod
    def get_collection_name():
        return "exercises"
