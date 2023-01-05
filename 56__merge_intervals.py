import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]

        self.assertEqual(expected, self.merge(intervals))

    def test_example_2(self):
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]

        self.assertEqual(expected, self.merge(intervals))

    def test_same_intervals(self):
        intervals = [[1, 4], [1, 4]]
        expected = [[1, 4]]

        self.assertEqual(expected, self.merge(intervals))

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        answer = [intervals[0]]
        slide = answer[-1]
        for i in range(1, len(intervals)):
            current = intervals[i]
            if slide[0] <= current[0] <= slide[1]:
                if current[1] > slide[1]:
                    slide[1] = current[1]
            else:
                answer.append(current)

        return answer
