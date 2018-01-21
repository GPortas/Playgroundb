import unittest


class IntegrationTestBase(unittest.TestCase):
    def setUp(self):
        self.tearDown()
        for item in self.fixtures:
            objects = item.fixture()
            for objectItem in objects:
                self.saveObject(objectItem)

    def tearDown(self):
        pass

    def saveObject(self, object_item):
        pass
