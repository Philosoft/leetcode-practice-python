import unittest
from heapq import heapify, heappop, heappush
from typing import List


class KthLargestTest(unittest.TestCase):
    def test(self):
        o = KthLargest(3, [4, 5, 8, 2])

        extra_vals = [3, 5, 10, 9, 4]
        expected_output = [4, 5, 5, 8, 8]

        for expected, val in zip(expected_output, extra_vals):
            self.assertEqual(expected, o.add(val))


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pq = nums
        self.k = k
        heapify(self.pq)
        while len(self.pq) > self.k:
            heappop(self.pq)

    def add(self, val: int) -> int:
        heappush(self.pq, val)
        while len(self.pq) > self.k:
            heappop(self.pq)

        return self.pq[0]
