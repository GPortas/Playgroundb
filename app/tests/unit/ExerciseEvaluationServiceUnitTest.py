import unittest
from unittest import mock

from app.api.domain.models.ExerciseEvaluation import ExerciseEvaluation
from app.api.domain.services.ExerciseEvaluationService import ExerciseEvaluationService
from app.api.domain.services.data.command.IExerciseEvaluationCommandRepository import \
    IExerciseEvaluationCommandRepository
from app.api.domain.services.data.command.errors.CommandError import CommandError
from app.api.domain.services.data.query.IExerciseEvaluationQueryRepository import IExerciseEvaluationQueryRepository
from app.api.domain.services.data.query.errors.QueryError import QueryError
from app.api.domain.services.data.query.errors.ResourceNotFoundQueryError import ResourceNotFoundQueryError
from app.api.domain.services.errors.ResourceNotFoundServiceError import ResourceNotFoundServiceError
from app.api.domain.services.errors.ServiceError import ServiceError


class ExerciseEvaluationServiceUnitTest(unittest.TestCase):

    def setUp(self):
        self.stub_exercise_evaluation_query_repository = mock.Mock(spec=IExerciseEvaluationQueryRepository)
        self.stub_exercise_evaluation_command_repository = mock.Mock(spec=IExerciseEvaluationCommandRepository)
        self.sut = ExerciseEvaluationService(self.stub_exercise_evaluation_query_repository,
                                             self.stub_exercise_evaluation_command_repository)

    def test_getExerciseEvaluation_calledWithNoneUserId_raiseValueError(self):
        self.assertRaises(ValueError, self.sut.get_exercise_evaluation, None, 'exercise_id')

    def test_getExerciseEvaluation_calledWithNoneExerciseId_raiseValueError(self):
        self.assertRaises(ValueError, self.sut.get_exercise_evaluation, 'user_id', None)

    def test_getExerciseEvaluation_called_innerQueryRepositoryCalledWithRightParams(self):
        self.sut.get_exercise_evaluation('fake_user_id', 'fake_exercise_id')
        self.stub_exercise_evaluation_query_repository.get_exercise_evaluation.assert_called_once_with(
            'fake_user_id', 'fake_exercise_id')

    def test_getExerciseEvaluation_calledWithQueryRepositoryWhichThrowsQueryError_throwServiceError(self):
        self.stub_exercise_evaluation_query_repository.get_exercise_evaluation.side_effect = QueryError()
        self.assertRaises(ServiceError, self.sut.get_exercise_evaluation, 'fake', 'fake')

    def test_createExerciseEvaluation_calledWithNoneExerciseEvaluation_raiseValueError(self):
        self.assertRaises(ValueError, self.sut.create_exercise_evaluation, None)

    def test_createExerciseEvaluation_calledWithValidExerciseEvaluation_innerCommandRepositoryCalledOnce(self):
        self.sut.create_exercise_evaluation(exercise_evaluation=self.__get_exercise_evaluation_test_instance())
        actual = self.stub_exercise_evaluation_command_repository.create_exercise_evaluation.call_count
        self.assertEqual(actual, 1)

    def test_createExerciseEvaluation_calledWithCommandRepositoryWhichThrowsCommandError_throwServiceError(self):
        self.stub_exercise_evaluation_command_repository.create_exercise_evaluation.side_effect = CommandError()
        self.assertRaises(ServiceError, self.sut.create_exercise_evaluation,
                          exercise_evaluation=self.__get_exercise_evaluation_test_instance())

    def test_incrementExerciseEvaluationAttempts_calledWithNoneUserId_raiseValueError(self):
        self.assertRaises(ValueError, self.sut.increment_exercise_evaluation_attempts, None, 'exercise_id')

    def test_incrementExerciseEvaluationAttempts_calledWithNoneExerciseId_raiseValueError(self):
        self.assertRaises(ValueError, self.sut.increment_exercise_evaluation_attempts, 'user_id', None)

    def test_incrementExerciseEvaluationAttempts_calledWithParams_innerCommandRepositoryCalledOnce(self):
        self.sut.increment_exercise_evaluation_attempts('user_id', 'exercise_id')
        actual = self.stub_exercise_evaluation_command_repository.increment_exercise_evaluation_attempts.call_count
        self.assertEqual(actual, 1)

    def test_incrementExerciseEvaluationAttempts_calledWithCommandRepositoryWhichThrowsCommandError_throwServiceError(
            self):
        self.stub_exercise_evaluation_command_repository.increment_exercise_evaluation_attempts.side_effect = CommandError()
        self.assertRaises(ServiceError, self.sut.increment_exercise_evaluation_attempts,
                          'user_id', 'exercise_id')

    def test_updateExerciseEvaluationAsSolved_calledWithNoneUserId_raiseValueError(self):
        self.assertRaises(ValueError, self.sut.update_exercise_evaluation_as_solved, None, 'exercise_id', 200)

    def test_updateExerciseEvaluationAsSolved_calledWithNoneExerciseId_raiseValueError(self):
        self.assertRaises(ValueError, self.sut.update_exercise_evaluation_as_solved, 'user_id', None, 200)

    def test_updateExerciseEvaluationAsSolved_calledWithNoneTimeLeft_raiseValueError(self):
        self.assertRaises(ValueError, self.sut.update_exercise_evaluation_as_solved, 'user_id', 'exercise_id', None)

    def test_updateExerciseEvaluationAsSolved_calledWithCommandRepositoryWhichThrowsCommandError_throwServiceError(
            self):
        self.stub_exercise_evaluation_query_repository.get_exercise_evaluation.return_value = self.__get_exercise_evaluation_test_instance()
        self.stub_exercise_evaluation_command_repository.update_exercise_evaluation_as_solved.side_effect = CommandError()
        self.assertRaises(ServiceError, self.sut.update_exercise_evaluation_as_solved,
                          'fake', 'fake', 200)

    def test_updateExerciseEvaluationAsSolved_calledWithParams_innerCommandRepositoryCalledOnce(self):
        self.stub_exercise_evaluation_query_repository.get_exercise_evaluation.return_value = self.__get_exercise_evaluation_test_instance()
        self.sut.update_exercise_evaluation_as_solved('user_id', 'exercise_id', 200)
        actual = self.stub_exercise_evaluation_command_repository.update_exercise_evaluation_as_solved.call_count
        self.assertEqual(actual, 1)

    def __get_exercise_evaluation_test_instance(self):
        return ExerciseEvaluation('fake_user_id', 'fake_exercise_id')
