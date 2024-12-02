import unittest
from src import day_01

class day_01_test(unittest.TestCase):
    def test_total_distance(self):
        input = """3   4
4   3
2   5
1   3
3   9
3   3"""

        self.assertEqual(day_01.total_distance(input), 11)

class day_02_test(unittest.TestCase):
    def test_total_distance(self):
        input = """3   4
4   3
2   5
1   3
3   9
3   3"""

        self.assertEqual(day_01.similarity_score(input), 31)
