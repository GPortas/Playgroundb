from bson import ObjectId

from app.api.data.command.ExerciseEvaluationMongoCommandRepository import ExerciseEvaluationMongoCommandRepository
from app.api.domain.models.ExerciseEvaluation import ExerciseEvaluation
from app.api.domain.services.data.command.errors.CommandError import CommandError
from tests.integration.PdbMongoIntegrationTestBase import PdbMongoIntegrationTestBase


class ExerciseEvaluationMongoCommandRepositoryIntegrationTest(PdbMongoIntegrationTestBase):

    def setUp(self):
        self.fixtures = []
        super(ExerciseEvaluationMongoCommandRepositoryIntegrationTest, self).setUp()
        self.sut = ExerciseEvaluationMongoCommandRepository()

    def tearDown(self):
        self.db.evaluations.delete_many({})

    def test_createExerciseEvaluation_calledWithExerciseEvaluation_correctInsertion(self):
        exercise_evaluation = self.__get_exercise_evaluation_test_instance()
        self.sut.create_exercise_evaluation(exercise_evaluation)
        actual = self.db.evaluations.find_one({'_id': exercise_evaluation.get_id()})
        expected = exercise_evaluation.to_json_dict()
        self.assertEqual(actual, expected)

    def test_createExerciseEvaluation_calledWithExistentExerciseEvaluation_throwCommandError(self):
        exercise_evaluation = self.__get_exercise_evaluation_test_instance()
        self.sut.create_exercise_evaluation(exercise_evaluation)
        self.assertRaises(CommandError, self.sut.create_exercise_evaluation, exercise_evaluation)

    def test_incrementExerciseEvaluationAttempts_calledWithExerciseEvaluation_attemptNumberCorrectlyUpdated(self):
        exercise_evaluation = self.__create_and_insert_exercise_evaluation_test_instance()
        self.sut.increment_exercise_evaluation_attempts(exercise_evaluation)
        actual = ExerciseEvaluation.from_json(
            self.db.evaluations.find_one({'_id': exercise_evaluation.get_id()})).get_attempt()
        expected = 2
        self.assertEqual(actual, expected)

    def test_updateExerciseEvaluationAsSolved_calledWithValidParams_exerciseEvaluationCorrectlyUpdated(self):
        exercise_evaluation = self.__create_and_insert_exercise_evaluation_test_instance()
        self.sut.update_exercise_evaluation_as_solved(exercise_evaluation, 200)
        exercise_evaluation_returned_from_db = ExerciseEvaluation.from_json(
            self.db.evaluations.find_one({'_id': exercise_evaluation.get_id()}))
        actual_score = exercise_evaluation_returned_from_db.get_score()
        expected_score = 200
        actual_status = exercise_evaluation_returned_from_db.get_status()
        expected_status = ExerciseEvaluation.STATUS_SOLVED
        self.assertEqual(actual_score, expected_score)
        self.assertEqual(actual_status, expected_status)

    def __create_and_insert_exercise_evaluation_test_instance(self):
        exercise_evaluation = self.__get_exercise_evaluation_test_instance()
        self.db.evaluations.insert_one(exercise_evaluation.to_json_dict())
        return exercise_evaluation

    def __get_exercise_evaluation_test_instance(self):
        return ExerciseEvaluation(ObjectId('54759eb3c090d83494e2d804'), ObjectId('507f1f77bcf86cd799439011'),
                                  _id=ObjectId("666f6f2d6261722d71757578"))
