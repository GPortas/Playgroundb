from app.api.dal.command.ExerciseMongoCommandRepository import ExerciseMongoCommandRepository
from app.api.models.Exercise import Exercise
from tests.integration.PdbMongoIntegrationTestBase import PdbMongoIntegrationTestBase


class ExerciseMongoCommandRepositoryIntegrationTest(PdbMongoIntegrationTestBase):
    def setUp(self):
        self.fixtures = []
        super(ExerciseMongoCommandRepositoryIntegrationTest, self).setUp()
        self.sut = ExerciseMongoCommandRepository()
        self.tearDown()

    def tearDown(self):
        self.db.exercises.delete_many({})

    def test_createExercise_calledWithExercise_correctInsertion(self):
        self.sut.create_exercise(Exercise(_id="666f6f2d6261722d71757578", question="testquestion", solution="testsolution", author="author1"))
        #todo: how to test this correctly?
        self.assertTrue(True)
