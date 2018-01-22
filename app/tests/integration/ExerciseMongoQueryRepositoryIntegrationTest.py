from app.api.dal.query.ExerciseMongoQueryRepository import ExerciseMongoQueryRepository
from app.api.dal.query.errors.ResourceNotFoundQueryError import ResourceNotFoundQueryError
from tests.integration.PdbMongoIntegrationTestBase import PdbMongoIntegrationTestBase


class ExerciseMongoQueryRepositoryIntegrationTest(PdbMongoIntegrationTestBase):
    def setUp(self):
        self.fixtures = ['Exercise']
        super(ExerciseMongoQueryRepositoryIntegrationTest, self).setUp()
        self.sut = ExerciseMongoQueryRepository()

    def tearDown(self):
        self.db.exercises.delete_many({})

    def test_getExerciseById_calledWithValidId_returnCorrectResult(self):
        exercise = self.sut.get_exercise_by_id(exercise_id='4d128b6ea794fc13a8000003')
        self.assertEqual('fakequestion_4', exercise.get_question())

    def test_getExerciseById_calledWithUnexistentId_throwResourceNotFoundQueryError(self):
        self.assertRaises(ResourceNotFoundQueryError, self.sut.get_exercise_by_id,
                          exercise_id='4d128b6ea794fc13a8000009')
