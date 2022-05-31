import unittest
from test_unitest_mocking_practice import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch


class TestCalendar(unittest.TestCase):
    # Using patch as decorator
    @patch('test_unitest_mocking_practice.requests')
    def test_get_holidays_timeout_decorator(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()

    # Using patch as context manager
    def test_get_holidays_timeout(self):
        with patch('test_unitest_mocking_practice.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
