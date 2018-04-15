from app.api.data.query.ExerciseEvaluationMongoQueryRepository import ExerciseEvaluationMongoQueryRepository
from tests.integration.PdbMongoIntegrationTestBase import PdbMongoIntegrationTestBase


class ExerciseEvaluationMongoQueryRepositoryIntegrationTest(PdbMongoIntegrationTestBase):

    def setUp(self):
        self.fixtures = ['ExerciseEvaluation']
        super(ExerciseEvaluationMongoQueryRepositoryIntegrationTest, self).setUp()
        self.sut = ExerciseEvaluationMongoQueryRepository()

    def tearDown(self):
        self.db.evaluations.delete_many({})

    def test_getExerciseEvaluationById_calledWithValidValues_returnCorrectResult(self):
        exercise_evaluation = self.sut.get_exercise_evaluation(exercise_id='4d128b6ea794fc13a8000003',
                                                               user_id='4d128b6ea794fc13a8000002')
        self.assertEqual(123, exercise_evaluation.get_score())

    def test_getExerciseEvaluationById_calledWithUnexistentExerciseEvaluationInfo_returnNone(self):
        exercise_evaluation = self.sut.get_exercise_evaluation(exercise_id='505bd76785ebb509fc183733',
                                                               user_id='4d128b6ea794fc13a8000002')
        self.assertIsNone(exercise_evaluation)
