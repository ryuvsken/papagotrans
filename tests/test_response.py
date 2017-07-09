import unittest
import simplejson
from papagotrans.response import Response


class TestResponse(unittest.TestCase):
    def setUp(self):
        pass

    def test_parse_json(self):
        body = simplejson.dumps({'message': {'result': {'translatedText': 'Hello', 'srcLangType': 'ko'}}})
        response = Response.parse_json(body)
        self.assertEqual(response.code, Response.SUCCESS_CODE)

    def test_parse_failed_json(self):
        body = simplejson.dumps({'errorCode': 405, 'errorMessage': 'Not Found Resources'})
        response = Response.parse_json(body)
        self.assertNotEqual(response.code, Response.SUCCESS_CODE)