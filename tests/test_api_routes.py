from bottle import Bottle
from webtest import TestApp
import unittest
from app.managed_routes import web_app


class HelloV1Test(unittest.TestCase):
    def setUp(self):
        self.webApp = web_app
        self.testApp = TestApp(self.webApp)

    def test_that_no_name_throws_Exception(self):
        _expected_status_code = 404

        resp = self.testApp.get(url='http://localhost:9000/v1/hello/', expect_errors=True)
        self.assertEqual(resp.status_int, _expected_status_code,
                         "Return status code should be {}".format(_expected_status_code))


class HelloV2Test(unittest.TestCase):
    def setUp(self):
        self.webApp = web_app
        self.testApp = TestApp(self.webApp)

    def test_that_no_name_returns_a_valid_response(self):
        _expected_status_code = 200

        resp = self.testApp.get(url='http://localhost:9000/v2/hello/', expect_errors=True)
        self.assertEqual(resp.status_int, _expected_status_code,
                         "Return status code should be {}".format(_expected_status_code))
