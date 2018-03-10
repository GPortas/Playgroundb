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

    #TODO: Find the correct way to do this
    # def test_createExercise_calledWithExercise_correctInsertion(self):
    #   exercise = self.__exercise_get_exercise_instance()
    #  self.sut.create_exercise(self.__exercise_get_exercise_instance())
    # expected = exercise.get_author()
    # self.assertEqual(expected, actual)

    def test_createExercise_calledWithExistentExercise_throwCommandError(self):
        exercise = self.__exercise_get_exercise_instance()
        self.sut.create_exercise(exercise)
        self.assertRaises(CommandError, self.sut.create_exercise, exercise)

    def __exercise_get_exercise_instance(self):
        return Exercise(_id="666f6f2d6261722d71757578", question="testquestion", solution="testsolution",
                        author="author1")
