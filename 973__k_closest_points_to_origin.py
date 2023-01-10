import unittest
from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        points = [[1, 3], [-2, 2]]
        k = 1
        expected = [[-2, 2]]

        self.assertEqual(expected, self.kClosest(points, k))

    def test_example_2(self):
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 2
        expected = [[3, 3], [-2, 4]]
        expected.sort()

        answer = self.kClosest(points, k)
        answer.sort()

        self.assertEqual(expected, answer)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        distance_to_points = defaultdict(list)

        p = points.pop()
        x, y = p
        distance = x ** 2 + y ** 2
        distance_to_points[-distance].append(p)
        heap.append(-distance)
        del x, y, distance

        for p in points:
            x, y = p
            distance = x ** 2 + y ** 2
            distance_to_points[-distance].append(p)

            heappush(heap, -distance)
            if len(heap) > k:
                to_remove = heappop(heap)
                distance_to_points[to_remove].pop()

        answer = []
        while k > 0:
            target_distance = heappop(heap)
            while distance_to_points[target_distance] and k > 0:
                k -= 1
                answer.append(distance_to_points[target_distance].pop())

        return answer
