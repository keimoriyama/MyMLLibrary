import unittest
import sys
sys.path.append('../src/')

from utils import get_elapsed_time

class Testuilts(unittest.TestCase):

    def test_seconds(self):
        start, end = 0, 50
        result = get_elapsed_time(start, end)
        estimate_result = [0, 0, 50]
        self.assertEqual(result, estimate_result)

    def test_minutes(self):
        start, end = 0, 70
        result = get_elapsed_time(start, end)
        estimate_result = [0, 1, 10]
        self.assertEqual(result, estimate_result)

    def test_hours(self):
        start, end = 0, 3700
        result = get_elapsed_time(start, end)
        estimate_result = [1, 1, 40]
        self.assertEqual(result, estimate_result)

if __name__ == '__main__':
    unittest.main()
