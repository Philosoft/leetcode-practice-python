import unittest
from collections import defaultdict
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        points = [[1, 1], [2, 2], [3, 3]]
        self.assertEqual(3, self.maxPoints(points))

    def test_example_2(self):
        points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
        self.assertEqual(4, self.maxPoints(points))

    def test_single_point(self):
        self.assertEqual(1, self.maxPoints([[0, 0]]))

    def test_something_complex(self):
        """
        35th out of 37 leetcode tests
        """
        points = [[7, 3], [19, 19], [-16, 3], [13, 17], [-18, 1], [-18, -17], [13, -3], [3, 7], [-11, 12], [7, 19],
                  [19, -12], [20, -18], [-16, -15], [-10, -15], [-16, -18], [-14, -1], [18, 10], [-13, 8], [7, -5],
                  [-4, -9], [-11, 2], [-9, -9], [-5, -16], [10, 14], [-3, 4], [1, -20], [2, 16], [0, 14], [-14, 5],
                  [15, -11], [3, 11], [11, -10], [-1, -7], [16, 7], [1, -11], [-8, -3], [1, -6], [19, 7], [3, 6],
                  [-1, -2], [7, -3], [-6, -8], [7, 1], [-15, 12], [-17, 9], [19, -9], [1, 0], [9, -10], [6, 20],
                  [-12, -4], [-16, -17], [14, 3], [0, -1], [-18, 9], [-15, 15], [-3, -15], [-5, 20], [15, -14],
                  [9, -17], [10, -14], [-7, -11], [14, 9], [1, -1], [15, 12], [-5, -1], [-17, -5], [15, -2], [-12, 11],
                  [19, -18], [8, 7], [-5, -3], [-17, -1], [-18, 13], [15, -3], [4, 18], [-14, -15], [15, 8], [-18, -12],
                  [-15, 19], [-9, 16], [-9, 14], [-12, -14], [-2, -20], [-3, -13], [10, -7], [-2, -10], [9, 10],
                  [-1, 7], [-17, -6], [-15, 20], [5, -17], [6, -6], [-11, -8]]
        self.assertEqual(6, self.maxPoints(points))

    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        hashmap = defaultdict(set)
        m = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue

                p1, p2 = points[i], points[j]
                if p1[0] == p2[0]:
                    key = f'vertical_{p1[0]}'

                else:
                    slope = (p1[1] - p2[1]) / (p1[0] - p2[0])
                    y_intersection = -slope * p1[0] + p1[1]
                    key = f'{slope}-{y_intersection}'
                hashmap[key].add(i)
                hashmap[key].add(j)
                m = max(m, len(hashmap[key]))

        return m

    def maxPointsGCD(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        hashmap = defaultdict(set)
        m = 0

        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue

                p1, p2 = points[i], points[j]

                if p1[0] == p2[0]:
                    # vertical line parallel y-axis
                    key = p1[0]
                else:
                    # ax + bx + c = 0
                    a = p2[1] - p1[1]
                    b = p1[0] - p2[0]
                    c = p2[0] * p1[1] - p1[0] * p2[1]
                    if a < 0:
                        a, b, c = -a, -b, -c

                    def gcd(left: int, right: int) -> int:
                        return gcd(right % left, left) if left != 0 else right

                    g = gcd(gcd(a, b), c)
                    # to keep everything int
                    key = (a / g, b / g, c / g)

                hashmap[key].add(tuple(p1))
                hashmap[key].add(tuple(p2))
                m = max(m, len(hashmap[key]))

        return m
