import unittest
from unittest import mock

from app.api.domain.services.data.command.errors.CommandError import CommandError
from app.api.domain.services.data.query.errors.QueryError import QueryError
from app.api.domain.services.data.query.errors.ResourceNotFoundQueryError import ResourceNotFoundQueryError
from app.api.domain.models.Exercise import Exercise
from app.api.domain.services.ExerciseService import ExerciseService
from app.api.domain.services.data.command.IExerciseCommandRepository import IExerciseCommandRepository
from app.api.domain.services.data.query.IExerciseQueryRepository import IExerciseQueryRepository
from app.api.domain.services.errors.ResourceNotFoundServiceError import ResourceNotFoundServiceError
from app.api.domain.services.errors.ServiceError import ServiceError


class ExerciseServiceUnitTest(unittest.TestCase):

    def setUp(self):
        self.stub_exercise_query_repository = mock.Mock(spec=IExerciseQueryRepository)
        self.stub_exercise_command_repository = mock.Mock(spec=IExerciseCommandRepository)
        self.sut = ExerciseService(self.stub_exercise_query_repository, self.stub_exercise_command_repository)

    def test_getExerciseById_calledWithNoneId_raiseValueError(self):
        self.assertRaises(ValueError, self.sut.get_exercise_by_id, exercise_id=None)

    def test_getExerciseById_called_correctCallToInnerQueryRepository(self):
        self.sut.get_exercise_by_id(exercise_id='fakeid')
        self.stub_exercise_query_repository.get_exercise_by_id.assert_called_once_with(exercise_id='fakeid')

    def test_getExerciseById_calledWithQueryRepositoryWhichThrowsQueryError_throwServiceError(self):
        self.stub_exercise_query_repository.get_exercise_by_id.side_effect = QueryError()
        self.assertRaises(ServiceError, self.sut.get_exercise_by_id, exercise_id='fakeid')

    def test_getExerciseById_calledWithQueryRepositoryWhichThrowsResourceNotFoundQueryError_throwResourceNotFoundServiceError(
            self):
        self.stub_exercise_query_repository.get_exercise_by_id.side_effect = ResourceNotFoundQueryError()
        self.assertRaises(ResourceNotFoundServiceError, self.sut.get_exercise_by_id, exercise_id='fakeid')

    def test_createExercise_calledWithNoneExercise_raiseValueError(self):
        self.assertRaises(ValueError, self.sut.create_exercise, exercise=None)

    def test_createExercise_calledWithValidExercise_innerCommandRepositoryCalledOnce(self):
        self.sut.create_exercise(exercise=Exercise(author='fakeauthor'))
        actual = self.stub_exercise_command_repository.create_exercise.call_count
        self.assertEqual(actual, 1)

    def test_createExercise_calledWithCommandRepositoryWhichThrowsCommandError_throwServiceError(self):
        self.stub_exercise_command_repository.create_exercise.side_effect = CommandError()
        self.assertRaises(ServiceError, self.sut.create_exercise, exercise=Exercise(author='fakeauthor'))

    def test_getAllExercises_called_correctCallToInnerQueryRepository(self):
        self.sut.get_all_exercises()
        self.stub_exercise_query_repository.get_all_exercises.assert_called_once_with()
