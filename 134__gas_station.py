import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(3, self.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))

    def test_example_2(self):
        self.assertEqual(-1, self.canCompleteCircuit([2, 3, 4], [3, 4, 3]))

    def test_example_3(self):
        self.assertEqual(-1, self.canCompleteCircuit([4, 5, 3, 1, 4], [5, 4, 3, 4, 2]))

    def test_gigantic_arrays(self):
        self.assertEqual(0, self.canCompleteCircuit([2] * 2 ** 10, [1] * 2 ** 10))

    def test_smallest_input(self):
        self.assertEqual(0, self.canCompleteCircuit([2], [2]))

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [g - c for g, c in zip(gas, cost)]
        # if total gas < total costs. there is no solution
        if sum(diff) < 0:
            return -1

        # if we are here, then 1 solution is guaranteed
        total = 0
        start = 0
        for i in range(len(gas)):
            total += diff[i]
            if total < 0:
                total = 0
                start = i + 1

        return start

    def canCompleteCircuitBrute(self, gas: List[int], cost: List[int]) -> int:
        '''
        Logic seems to be correct, but complexity is O(N ** 2)
        this method passes 33 out of 37 tests on leetcode
        fails with Time Limit Exceeded on 34th (10k arrays)
        '''
        diff = [g - c for g, c in zip(gas, cost)]

        for i in range(len(diff)):
            if diff[i] < 0:
                continue

            ptr = i
            current_gas = 0
            for _ in range(len(diff)):
                current_gas += diff[ptr]
                if current_gas < 0:
                    break
                ptr += 1
                if ptr == len(diff):
                    ptr -= len(diff)
            if ptr == i:
                return i

        return -1
