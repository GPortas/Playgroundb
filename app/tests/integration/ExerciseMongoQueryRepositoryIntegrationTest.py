from app.api.data.query.ExerciseMongoQueryRepository import ExerciseMongoQueryRepository
from app.api.domain.services.data.query.errors.ResourceNotFoundQueryError import ResourceNotFoundQueryError
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

    def test_getAllExercises_called_returnCorrectResult(self):
        actual = self.sut.get_all_exercises()
        actual_map = list(map(lambda x: x.get_question(), actual))
        expected = ['fakequestion_1', 'fakequestion_2', 'fakequestion_3', 'fakequestion_4']
        self.assertEqual(actual_map, expected)
