import unittest
import sys
import os

sys.path.append(os.path.join(os.getcwd(), '..'))
from client import create_presence, process_ans


class TestClient(unittest.TestCase):
    def test_create_presence(self):
        out = create_presence('test')
        out['time'] = 1
        self.assertEqual(out, {
            'action': 'presence',
            'time': 1,
            'user': {
                'account_name': 'test'
            }
        })

    def test_process_ans_200(self):
        out = process_ans({'response': 200})
        self.assertEqual(out, '200 : OK')

    def test_process_ans_400(self):
        out = process_ans({'response': 400, 'error': 'Bad Request'})
        self.assertEqual(out, '400 : Bad Request')


if __name__ == '__main__':
    unittest.main()
