import unittest

from cron_parser import process_comma, process_hyphen
from utils import get_stringified_values


class TestCronParser(unittest.TestCase):

    def test_process_comma(self):
        self.assertEqual(process_comma('1,3,5'), [1, 3, 5])

    def test_process_hyphen(self):
        self.assertEqual(process_hyphen('1-5'), [1, 2, 3, 4, 5])

    def test_get_stringified_values(self):
        self.assertEqual(get_stringified_values([1, 2, 3, 4, 5]), "1 2 3 4 5")
