import unittest

from tests.integration.fixtures.ExerciseFixture import *
from tests.integration.fixtures.UserFixture import *
from tests.integration.fixtures.ExerciseEvaluationFixture import *


class IntegrationTestBase(unittest.TestCase):
    def setUp(self):
        self.tearDown()
        for item in self.fixtures:
            objects = eval(item + 'Fixture').fixture()
            for objectItem in objects:
                self.saveObject(objectItem)

    def tearDown(self):
        pass

    def saveObject(self, object_item):
        pass
