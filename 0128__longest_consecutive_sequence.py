"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

## Example 1

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation:
    The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

## Example 2

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

## Constraints

* 0 <= nums.length <= 10^5
* -10^9 <= nums[i] <= 10^9
"""
from collections import defaultdict
from typing import List, Dict
from unittest import TestCase


class UnionFind:
    def __init__(self):
        self.roots: Dict[int, int] = defaultdict(int)
        self.longest_seq = 0
        self.root_to_len: Dict[int, int] = defaultdict(int)

    def union(self, x: int) -> None:
        if x in self.roots:
            return

        self.roots[x] = x
        self.root_to_len[x] += 1
        if x - 1 in self.roots:
            # this is a sequence in the making
            parent = self.roots[x - 1]
            while parent != self.roots[parent]:
                parent = self.roots[parent]

            self.roots[x] = parent
            self.root_to_len[parent] += self.root_to_len[x]
            del self.root_to_len[x]

        if x + 1 in self.roots:
            # another part of sequence in the making
            parent = self.roots[x]
            while parent != self.roots[parent]:
                parent = self.roots[parent]

            self.roots[x + 1] = parent
            self.root_to_len[parent] += self.root_to_len[x + 1]
            del self.root_to_len[x + 1]

        xroot = self.roots[x]
        while xroot != self.roots[xroot]:
            xroot = self.roots[xroot]

        self.longest_seq = max([
            self.root_to_len[xroot],
            self.longest_seq,
        ])


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(4, self.longestConsecutive([100, 4, 200, 1, 3, 2]))

    def test_example_2(self):
        self.assertEqual(9, self.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))

    def test_whole_array(self):
        self.assertEqual(5, self.longestConsecutive([1, 3, 5, 2, 4]))

    def test_leetcode_56(self):
        self.assertEqual(5, self.longestConsecutive([-2, -3, -3, 7, -3, 0, 5, 0, -8, -4, -1, 2]))

    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind()
        for n in nums:
            uf.union(n)

        return uf.longest_seq
