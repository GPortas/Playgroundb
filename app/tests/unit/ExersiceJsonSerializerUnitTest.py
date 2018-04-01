import unittest

from bson import ObjectId

from app.api.domain.models.Exercise import Exercise
from app.api.ui.utils.serializers.ExerciseJsonSerializer import ExerciseJsonSerializer


class ExersiceJsonSerializerUnitTest(unittest.TestCase):

    def setUp(self):
        self.sut = ExerciseJsonSerializer()

    def test_toJsonDict_calledWithExercise_returnCorrectResult(self):
        source_exercise = Exercise(author="testauthor", _id=ObjectId("666f6f2d6261722d71757578"),
                                   collection_name='testcollection', collection_data='testdata',
                                   question='testquestion', solution='testsolution')
        actual = self.sut.to_json_dict(source_exercise)
        expected = {"author": "testauthor", "_id": "666f6f2d6261722d71757578",
                    "collection_name": "testcollection", "collection_data": "testdata",
                    "question": "testquestion", "solution": "testsolution"}
        self.assertEqual(actual, expected)
