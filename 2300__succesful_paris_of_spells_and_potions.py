"""
LeetCode: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/

Idea: sort potions, use binary search to find the lowest acceptable combo, just count the rest of the array
"""

from math import ceil
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual([4, 0, 3], self.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))

    def test_example_2(self):
        self.assertEqual([2, 0, 2], self.successfulPairs([3, 1, 2], [8, 5, 8], 16))

    def test_no_pairs_possible(self):
        self.assertEqual([0, 0, 0], self.successfulPairs([1, 2, 3], [3, 2, 1, 5, 6, 7, 8, 9], 666))

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        pairs: List[int] = []
        for spell in spells:
            min_potion_strength = ceil(success / spell)
            left, right = 0, len(potions) - 1
            target_idx = -1
            while left <= right:
                mid = left + (right - left) // 2

                if potions[mid] < min_potion_strength:
                    left = mid + 1
                else:
                    target_idx = mid
                    right = mid - 1

            possible_pairs = 0
            if target_idx != -1:
                possible_pairs = len(potions) - target_idx

            pairs.append(possible_pairs)

        return pairs
