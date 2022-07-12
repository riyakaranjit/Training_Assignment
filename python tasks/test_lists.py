import os
from unittest import mock

from lists import rm, starts_with_B
from third_party_package import *
import tempfile
import unittest


class TestUnitTestCases(unittest.TestCase):
    # def setUp(self):
    #     current_dir = os.path.abspath(os.getcwd())
    #     temp_filepath = os.path.join(current_dir, "temp-testfile")
    #     print(temp_filepath)
    #     with open(self.temp_filepath, 'wb') as f:
    #         f.write(b'Delete me!')

    @mock.patch('lists.os')
    def test_rm(self, mock_os):
        """
        Everytime it runs, a temp file is created and then deleted!
        """
        # rm(self.temp_filepath)
        # self.assertEqual(os.path.isfile(self.temp_filepath), False, "Failed to remove the file.")
        mock_os.isfile.return_value = False
        rm("any path")

        self.assertTrue(mock_os.remove.called, "Failed to not remove the file if not present.")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")

    def starts_with_B(self):
        actual = starts_with_B(['Liam', 'Olivia', 'Noah', 'Emma', 'Benjamin', 'Ava', 'Elijah', 'Ben', 'William',
                                'Sophia'])
        expected = ['Benjamin', 'Ben']
        self.assertEqual(actual, expected, 'Names do not starts with B')

    def request_with_retry(self):
        with self.assertRaises(RuntimeError) as e:
            url = 'http://api.open-notify.org/iss-pass.json'
            make_request(url)
        self.assertEqual(str(e.exception), 'HTTP Response Code 400 received from server.')



