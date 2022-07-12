import unittest
import requests
from requests.exceptions import Timeout
from unittest.mock import Mock

# Mocking the requests behaviour
requests = Mock()


def get_holidays():
    url = 'http://restapi.adequateshop.com/api/Tourist?page=2'
    # url = 'http://localhost/api/holidays'
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


class TestCalendar(unittest.TestCase):

    @staticmethod
    def log_request(url):
        # Log a fake request for test output purposes
        print(f'Making a request to {url}.')
        print('Request received!')

        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        return response_mock

    def test_get_holidays_timeout(self):
        # Test a connection timeout
        requests.get.side_effect = Timeout
        # The assertRaises() verifies that the get_holiday() raises an exception given the new side effect of get().
        with self.assertRaises(Timeout):
            get_holidays()

    def test_get_holidays_logging(self):
        # Test a successful, logged request
        requests.get.side_effect = self.log_request
        assert get_holidays()['12/25'] == 'Christmas'


if __name__ == "__main__":
    unittest.main()
