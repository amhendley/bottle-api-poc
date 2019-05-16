
import unittest
import app.api as api


class HelloTest(unittest.TestCase):
    def test_empty_name_return_hello_stranger_response(self):
        _name = ''
        self.assertRegex(api.hello(name=_name), '.*({}).*'.format('stranger'),
                         'When no name is supplied, the expected response is not received')

    def test_string_returned_is_expected_value(self):
        _name = 'John'
        self.assertEqual(api.hello(name=_name), "<b>Hello {}</b>!".format(_name),
                         'The returned string is not as expected')


class HelloV2Test(unittest.TestCase):
    def test_empty_name_return_hello_stranger_response(self):
        _name = ''
        self.assertRegex(api.hello2(name=_name), '.*({}).*'.format('stranger'),
                         'When no name is supplied, the expected response is not received')

    def test_string_returned_is_expected_value(self):
        _name = 'John'
        self.assertEqual(api.hello2(name=_name), "<b>Hello {}</b>!".format(_name),
                         'The returned string is not as expected')
