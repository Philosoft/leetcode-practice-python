"""
LeetCode: https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted
in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

## Example 1

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

## Example 2

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

## Constraints

* 1 <= flowerbed.length <= 2 * 10^4
* flowerbed[i] is 0 or 1.
* There are no two adjacent flowers in flowerbed.
* 0 <= n <= flowerbed.length
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertTrue(self.canPlaceFlowers([1, 0, 0, 0, 1], 1))

    def test_example_2(self):
        self.assertFalse(self.canPlaceFlowers([1, 0, 0, 0, 1], 2))

    def test_ample_space(self):
        self.assertTrue(self.canPlaceFlowers([0, 0, 1, 0, 0], 1))

    def test_case_108(self):
        self.assertFalse(self.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        prev_flower = -2
        for ptr in range(len(flowerbed)):
            if flowerbed[ptr]:
                prev_flower = ptr
            if (
                flowerbed[ptr] == 0 and ptr - prev_flower >= 2
                and (ptr + 1 < len(flowerbed) and flowerbed[ptr + 1] != 1 or ptr + 1 >= len(flowerbed))
            ):
                n -= 1
                if n == 0:
                    return True
                prev_flower = ptr

        return n == 0
