"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
i-th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

## Example 1

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation:
    The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
    (blue section) the container can contain is 49.

## Example 2

Input: height = [1,1]
Output: 1

## Constraints

* n == height.length
* 2 <= n <= 10^5
* 0 <= height[i] <= 10^4
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(49, self.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

    def test_example_2(self):
        self.assertEqual(1, self.maxArea([1, 1]))

    def test_random_input(self):
        self.assertEqual(66, self.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7, 3, 5, 6, 6, 3, 2, 3, 4, 4, 2]))

    def test_random_input_with_couple_of_really_tall_walls(self):
        self.assertEqual(1965, self.maxArea([1, 8, 131, 6, 2, 5, 4, 8, 3, 7, 3, 5, 6, 6, 3, 2, 3, 666, 4, 4, 2]))

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        m = 0
        while left < right:
            m = max(m, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return m
