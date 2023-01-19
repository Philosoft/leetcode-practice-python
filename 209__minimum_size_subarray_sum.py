"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

### Example 1:

Input:
    target = 7
    nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

### Example 2:

Input:
    target = 4
    nums = [1,4,4]
Output: 1

### Example 3:

Input:
    target = 11
    nums = [1,1,1,1,1,1,1,1]
Output: 0


## Constraints:

* 1 <= target <= 10^9
* 1 <= nums.length <= 10^5
* 1 <= nums[i] <= 10^4

## Follow up

If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(2, self.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))

    def test_example_2(self):
        self.assertEqual(1, self.minSubArrayLen(4, [1, 4, 4]))

    def test_example_3(self):
        self.assertEqual(0, self.minSubArrayLen(11, [1] * 8))

    def test_leetcode_100(self):
        self.assertEqual(3, self.minSubArrayLen(11, [1, 2, 3, 4, 5]))

    def test_leetcode_200(self):
        self.assertEqual(1, self.minSubArrayLen(7, [1, 1, 1, 1, 7]))

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        length = len(nums)
        min_size = length + 1
        window_sum = nums[0]
        max_index = length - 1
        while (left != max_index and right != length) or target != 0:
            if window_sum >= target:
                min_size = min(right - left + 1, min_size)
                window_sum -= nums[left]
                left = min(left + 1, max_index)
            else:
                if right + 1 < length:
                    right += 1
                    window_sum += nums[right]
                else:
                    break

        return min_size if min_size != length + 1 else 0
