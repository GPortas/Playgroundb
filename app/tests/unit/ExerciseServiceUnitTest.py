import unittest
from unittest import mock

from ddt import data, ddt

from app.api.dal.ExerciseQueryRepository import ExerciseQueryRepository
from app.api.services.ExerciseService import ExerciseService
from app.api.services.errors.ResourceNotFoundServiceError import ResourceNotFoundServiceError


@ddt
class ExerciseServiceUnitTest(unittest.TestCase):

    def setUp(self):
        self.stubExerciseQueryRepository = mock.Mock(spec=ExerciseQueryRepository)
        self.sut = ExerciseService(self.stubExerciseQueryRepository)

    @data(
        {'exercise_id': None, 'answer': 'testanswer'},
        {'exercise_id': 'testid', 'answer': None},
        {'exercise_id': None, 'answer': None}
    )
    def test_checkIfAnswerIsCorrect_calledWithNoneParams_raiseResourceNotFoundServiceError(self, input):
        self.assertRaises(ResourceNotFoundServiceError, self.sut.check_if_answer_is_correct,
                          exercise_id=input['exercise_id'], answer=input['answer'])
