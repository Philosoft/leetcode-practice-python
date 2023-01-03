import unittest
from collections import defaultdict
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        answer = self.minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4])
        self.assertEqual(answer, 4)

    def test_example_2(self):
        self.assertEqual(self.minimumRounds([2, 3, 3]), -1)

    def minimumRounds(self, tasks: List[int]) -> int:
        data = defaultdict(lambda: 0)

        for t in tasks:
            data[t] += 1

        rounds = 0
        for t in data.values():
            if t == 1:
                return -1

            if t in [2, 3]:
                rounds += 1
            else:
                # don't ask me about math here
                rounds += (t + 2) // 3

        return rounds
