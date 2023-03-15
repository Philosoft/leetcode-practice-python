"""
LeetCode: https://leetcode.com/problems/target-sum/

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and
then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the
expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.


## Example 1

Input: nums = [1,1,1,1,1], target = 3
Output: 5

Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.

```
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
```

## Example 2

Input: nums = [1], target = 1
Output: 1

## Constraints

* 1 <= nums.length <= 20
* 0 <= nums[i] <= 1000
* 0 <= sum(nums[i]) <= 1000
* -1000 <= target <= 1000
"""
from typing import List, Dict, Tuple
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(5, self.findTargetSumWays([1, 1, 1, 1, 1], 3))

    def test_example_2(self):
        self.assertEqual(1, self.findTargetSumWays([1], 1))

    def test_impossible(self):
        self.assertEqual(0, self.findTargetSumWays([1], 2))

    def test_case_7(self):
        self.assertEqual(2, self.findTargetSumWays([1, 2, 1], 0))

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache: Dict[Tuple[int, int], int] = {}

        def explore(ptr: int, current_sum: int) -> int:
            if ptr >= len(nums):
                return 1 if current_sum == target else 0

            key = (ptr, current_sum)
            if key in cache:
                return cache[key]

            ways = explore(ptr + 1, nums[ptr] + current_sum) + explore(ptr + 1, -nums[ptr] + current_sum)
            cache[key] = ways

            return ways

        return explore(0, 0)
