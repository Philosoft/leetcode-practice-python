"""
LeetCode: https://leetcode.com/problems/boats-to-save-people/
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(1, self.numRescueBoats([1, 2], 3))

    def test_example_2(self):
        self.assertEqual(3, self.numRescueBoats([3, 2, 2, 1], 3))

    def test_example_3(self):
        self.assertEqual(4, self.numRescueBoats([3, 5, 3, 4], 5))

    def test_case_39(self):
        self.assertEqual(2, self.numRescueBoats([2, 4], 5))

    def test_case_70(self):
        # 2 persons per boat is the limit
        self.assertEqual(3, self.numRescueBoats([3, 2, 3, 2, 2], 6))

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        l, r = 0, len(people) - 1
        while l <= r:
            current_limit = limit
            seats = 2
            while current_limit - people[r] >= 0 and l <= r and seats > 0:
                current_limit -= people[r]
                r -= 1
                seats -= 1

            while current_limit - people[l] >= 0 and l <= r and seats > 0:
                current_limit -= people[l]
                l += 1
                seats -= 1

            boats += 1

        return boats
