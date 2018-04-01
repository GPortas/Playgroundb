from bson import ObjectId
import json

from app.api.data.command.ExerciseMongoCommandRepository import ExerciseMongoCommandRepository
from app.api.domain.services.data.command.errors.CommandError import CommandError
from app.api.domain.models.Exercise import Exercise
from tests.integration.PdbMongoIntegrationTestBase import PdbMongoIntegrationTestBase


class ExerciseMongoCommandRepositoryIntegrationTest(PdbMongoIntegrationTestBase):
    def setUp(self):
        self.fixtures = []
        super(ExerciseMongoCommandRepositoryIntegrationTest, self).setUp()
        self.sut = ExerciseMongoCommandRepository()

    def tearDown(self):
        self.db.exercises.delete_many({})

    def test_createExercise_calledWithExercise_correctInsertion(self):
        exercise = self.__get_exercise_instance()
        self.sut.create_exercise(exercise)
        actual = self.db.exercises.find_one({'_id': exercise.get_id()})
        expected = exercise.to_json_dict()
        self.assertEqual(actual, expected)

    def test_createExercise_calledWithExistentExercise_throwCommandError(self):
        exercise = self.__get_exercise_instance()
        self.sut.create_exercise(exercise)
        self.assertRaises(CommandError, self.sut.create_exercise, exercise)

    def __get_exercise_instance(self):
        return Exercise(_id=ObjectId("666f6f2d6261722d71757578"), question="fakequestion_1",
                        solution=json.dumps({'key1': 'value1', 'key2': 'value2'}), author="author1",
                        collection_name="testcollection", collection_data="testdata")
