"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in
any order.

## Example 1

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

## Example 2

Input: nums = [1], k = 1
Output: [1]

## Constraints

* 1 <= nums.length <= 10^5
* -10^4 <= nums[i] <= 10^4
* k is in the range [1, the number of unique elements in the array].
* It is guaranteed that the answer is unique.

## Follow up

Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from collections import Counter, defaultdict
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual([1, 2], self.topKFrequent([1, 1, 1, 2, 2, 3], 2))

    def test_example_2(self):
        self.assertEqual([1], self.topKFrequent([1], 1))

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq_to_num = defaultdict(list)
        for number, cnt in count.items():
            freq_to_num[cnt].append(number)

        result = []
        targets = list(freq_to_num.keys())
        targets.sort()
        while k > 0:
            t = targets.pop()
            while k > 0 and len(freq_to_num[t]) > 0:
                result.append(freq_to_num[t].pop())
                k -= 1

        return result
