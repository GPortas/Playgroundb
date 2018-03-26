import json
import unittest
from unittest import mock

from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request


class BaseViewSetUnitTest(unittest.TestCase):

    def _configure_sut_request(self, json_raw):
        request = mock.Mock(spec=Request)
        request.data = json.loads(json_raw)
        request.pdbuser = 'fake'
        return request

    def _parse_and_test_response(self, actual, expected):
        actual = self._get_ordered_json_from_response(actual)
        expected = self._from_string_to_ordered_json(expected)
        self.assertEqual(actual, expected)

    def _get_ordered_json_from_response(self, response):
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'text/json'
        response.renderer_context = response
        decode = response.render().content.decode('utf-8')
        return self._from_string_to_ordered_json(decode)

    def _from_string_to_ordered_json(self, source):
        return self._ordered(json.loads(source))

    def _ordered(self, obj):
        if isinstance(obj, dict):
            return sorted((k, self._ordered(v)) for k, v in obj.items())
        if isinstance(obj, list):
            return sorted(self._ordered(x) for x in obj)
        else:
            return obj
