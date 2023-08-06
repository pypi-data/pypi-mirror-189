import unittest
import sys
import os
import json
from datetime import datetime

sys.path.append(os.path.join(os.getcwd(), '..'))
from config.utils import get_message, send_message
from config.variables import ENCODING


class MySocket:
    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        json_test_message = json.dumps(self.test_dict)
        self.encoded_message = json_test_message.encode(ENCODING)
        self.received_message = message_to_send

    def recv(self, max_length):
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(ENCODING)


class TestUtils(unittest.TestCase):
    ok_server_response = {'response': 200}
    err_server_response = {'response': 400, 'error': 'Bad Request'}
    client_message = {
        'action': 'presence',
        'time': datetime.now().strftime('%X %x'),
        'user': {
            'account_name': 'test_account'
        }
    }

    def test_get_message_ok(self):
        test_sock_ok = MySocket(self.ok_server_response)
        self.assertEqual(get_message(test_sock_ok, 1024, ENCODING), self.ok_server_response)

    def test_get_message_err(self):
        test_sock_err = MySocket(self.err_server_response)
        self.assertEqual(get_message(test_sock_err, 1024, ENCODING), self.err_server_response)

    def test_send_message(self):
        test_sock = MySocket(self.client_message)
        send_message(test_sock, self.client_message, ENCODING)
        self.assertEqual(test_sock.encoded_message, test_sock.received_message)


if __name__ == '__main__':
    unittest.main()
