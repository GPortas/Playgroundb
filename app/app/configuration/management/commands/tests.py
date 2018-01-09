import unittest
import sys
from unittest import TestSuite
from unittest import TextTestRunner

from django.core.management import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('environment', nargs=1, type=str)
        parser.add_argument('test_case', nargs='?', type=str)

    def handle(self, *args, **options):
        suite = TestSuite()
        env = options['environment'][0]
        if options['test_case'] is not None:
            test_case = options['test_case']
        else:
            test_case = None
        if env == 'unit':
            pattern = '*UnitTest.py'
        elif env == 'integration':
            pattern = '*IntegrationTest.py'
        elif env == 'functional':
            pattern = '*FunctionalTest.py'
        else:
            raise ValueError('Invalid environment')
        if test_case is not None:
            pattern = test_case + ".py"
        for all_test_suite in unittest.defaultTestLoader.discover('tests', pattern=pattern):
            for test_suite in all_test_suite:
                try:
                    suite.addTests(test_suite)
                except Exception as e:
                    print("Error while adding test suite (" + str(test_suite) + "): " + str(e))
                    raise e

        runner = TextTestRunner(verbosity=1)
        result = runner.run(suite)
        sys.exit(not result.wasSuccessful())