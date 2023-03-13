"""
LeetCode: https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

You are given two 0-indexed integer arrays nums and multipliers of size n and m respectively, where n >= m.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (0-indexed) you will:

* Choose one integer x from either the start or the end of the array nums.
* Add multipliers[i] * x to your score.
* Remove x from nums.
* Return the maximum score after performing m operations.

Note that multipliers[0] corresponds to the first operation, multipliers[1] to the second operation, and so on.

## Example 1

Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation:

An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.

## Example 2

Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102

Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score.
The total score is 50 + 15 - 9 + 4 + 42 = 102.

## Constraints

* n == nums.length
* m == multipliers.length
* 1 <= m <= 300
* m <= n <= 10^5
* -1000 <= nums[i], multipliers[i] <= 1000
"""
from typing import List, Dict, Tuple
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(14, self.maximumScoreTopDown([1, 2, 3], [3, 2, 1]))
        self.assertEqual(14, self.maximumScoreBottomUp([1, 2, 3], [3, 2, 1]))

    def test_example_2(self):
        self.assertEqual(102, self.maximumScoreTopDown([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]))
        self.assertEqual(102, self.maximumScoreBottomUp([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]))

    def test_gigantic_example(self):
        self.assertEqual(555, self.maximumScoreTopDown([1] * 555, [1] * 555))
        self.assertEqual(555, self.maximumScoreBottomUp([1] * 555, [1] * 555))

    def maximumScoreBottomUp(self, nums: List[int], multipliers: List[int]) -> int:
        dp = []  # first index -> multi pointer, second index -> left
        for m in range(len(multipliers) + 1):
            dp.append([0] * (len(nums) + 1))

        for m in range(len(multipliers) - 1, -1, -1):
            multi = multipliers[m]
            for left in range(m, -1, -1):
                right = len(nums) - 1 - (m - left)

                option1 = multi * nums[left]
                option2 = multi * nums[right]

                dp[m][left] = max(
                    option1 + dp[m + 1][left + 1],
                    option2 + dp[m + 1][left]
                )

        return dp[0][0]

    def maximumScoreTopDown(self, nums: List[int], multipliers: List[int]) -> int:
        cache: Dict[Tuple[int, int, int]] = {}

        def dfs(left: int, right: int, multi_ptr: int) -> int:
            if multi_ptr >= len(multipliers):
                return 0

            if left > right:
                return 0

            key = (left, right, multi_ptr)
            if key in cache:
                return cache[key]

            multi = multipliers[multi_ptr]

            option1 = nums[left] * multi + dfs(left + 1, right, multi_ptr + 1)
            option2 = nums[right] * multi + dfs(left, right - 1, multi_ptr + 1)
            cache[key] = max(option1, option2)

            return cache[key]

        return dfs(0, len(nums) - 1, 0)
