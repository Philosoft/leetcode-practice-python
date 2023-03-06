"""
LeetCode: https://leetcode.com/problems/delete-and-earn/

You are given an integer array nums. You want to maximize the number of points you get by performing the following
operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to
nums[i] - 1 and every element equal to nums[i] + 1.

Return the maximum number of points you can earn by applying the above operation some number of times.

## Example 1

Input: nums = [3,4,2]
Output: 6
Explanation:
    You can perform the following operations:
    - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
    - Delete 2 to earn 2 points. nums = [].
    You earn a total of 6 points.

## Example 2

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation:
    You can perform the following operations:
    - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
    - Delete a 3 again to earn 3 points. nums = [3].
    - Delete a 3 once more to earn 3 points. nums = [].
    You earn a total of 9 points.

## Constraints

* 1 <= nums.length <= 2 * 10^4
* 1 <= nums[i] <= 10^4
"""
from collections import Counter
from typing import List, Dict
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(6, self.deleteAndEarn([3, 4, 2]))

    def test_example_2(self):
        self.assertEqual(9, self.deleteAndEarn([2, 2, 3, 3, 3, 4]))

    def test_case_23(self):
        self.assertEqual(3451, self.deleteAndEarn(
            [12, 32, 93, 17, 100, 72, 40, 71, 37, 92, 58, 34, 29, 78, 11, 84, 77, 90, 92, 35, 12, 5, 27, 92, 91, 23, 65,
             91, 85, 14, 42, 28, 80, 85, 38, 71, 62, 82, 66, 3, 33, 33, 55, 60, 48, 78, 63, 11, 20, 51, 78, 42, 37, 21,
             100, 13, 60, 57, 91, 53, 49, 15, 45, 19, 51, 2, 96, 22, 32, 2, 46, 62, 58, 11, 29, 6, 74, 38, 70, 97, 4,
             22, 76, 19, 1, 90, 63, 55, 64, 44, 90, 51, 36, 16, 65, 95, 64, 59, 53, 93]
            ))

    def test_one_element(self):
        self.assertEqual(1, self.deleteAndEarn([1]))

    def test_same_elements(self):
        self.assertEqual(3, self.deleteAndEarn([1, 1, 1]))

    def deleteAndEarn(self, nums: List[int]) -> int:
        data: Dict[int, int] = {}
        for n in nums:
            data[n] = data.get(n, 0) + n
        numbers: List[int] = list(sorted(data.keys()))

        if len(numbers) == 1:
            return data[numbers[0]]

        self.max = 0
        cache = [0] * len(numbers)

        for i in range(len(numbers)):
            cache[i] = data[numbers[i]]
            if i > 0 and numbers[i] - 1 == numbers[i - 1]:
                cache[i] = max(cache[i - 1], cache[i] + (cache[i - 2] if i - 2 >= 0 else 0))
            else:
                cache[i] += cache[i - 1]

        return cache[-1]

    def deleteAndEarnClassicBruteForce(self, nums: List[int]) -> int:
        data = Counter(nums)
        self.max = 0
        cache = {}

        def dfs(data: Dict[int, int]) -> int:
            if len(data) == 0:
                return 0

            keys = frozenset(sorted(data.keys()))
            if keys in cache:
                return cache[keys]

            max_s = 0
            for k, v in data.items():
                s = k * v
                cnt = data.copy()
                del cnt[k]
                if k + 1 in cnt:
                    del cnt[k + 1]

                if k - 1 in cnt:
                    del cnt[k - 1]

                s += dfs(cnt)
                self.max = max(self.max, s)
                max_s = max(max_s, s)

            cache[keys] = max_s
            return max_s

        dfs(data)

        return self.max
