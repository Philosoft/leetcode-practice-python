import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]
        expected = 2

        self.assertEqual(expected, self.findMinArrowShots(points))

    def test_example_2(self):
        points = [[1, 2], [3, 4], [5, 6], [7, 8]]
        expected = 4

        self.assertEqual(expected, self.findMinArrowShots(points))

    def test_example_3(self):
        points = [[1, 2], [2, 3], [3, 4], [4, 5]]
        expected = 2

        self.assertEqual(expected, self.findMinArrowShots(points))

    def test_first_failure(self):
        """
        failed this test case on first try
        """

        self.assertEqual(2, self.findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]))

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrow_balloon = points[0]
        answer = 1
        for i in range(1, len(points)):
            balloon = points[i]
            balloon_start, balloon_end = balloon
            if balloon_start > arrow_balloon[1]:
                answer += 1
                arrow_balloon = balloon

        return answer
