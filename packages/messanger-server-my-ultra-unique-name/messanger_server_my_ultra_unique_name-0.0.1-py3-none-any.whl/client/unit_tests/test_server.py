import unittest
import sys
import os
from datetime import datetime

sys.path.append(os.path.join(os.getcwd(), '..'))
from server import process_client_message


class TestServer(unittest.TestCase):
    error_dict = {
        'response': 400,
        'error': 'Bad Request'
    }
    success_dict = {'response': 200}

    def test_process_client_message_200(self):
        message = {
            'action': 'presence',
            'time': datetime.now().strftime('%X %x'),
            'user': {
                'account_name': 'test'
            }
        }
        out = process_client_message(message)
        self.assertEqual(out, self.success_dict)

    def test_process_client_message_no_action(self):
        message = {
            'time': datetime.now().strftime('%X %x'),
            'user': {
                'account_name': 'test'
            }
        }
        out = process_client_message(message)
        self.assertNotEqual(out, self.success_dict)

    def test_process_client_message_no_user(self):
        message = {
            'action': 'presence',
            'time': datetime.now().strftime('%X %x'),
        }
        out = process_client_message(message)
        self.assertEqual(out, self.error_dict)

    def test_process_client_message_empty_message(self):
        message = {}
        out = process_client_message(message)
        self.assertEqual(out, self.error_dict)


if __name__ == '__main__':
    unittest.main()
