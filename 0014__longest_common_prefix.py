"""
LeetCode: https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

## Example 1

Input: strs = ["flower","flow","flight"]
Output: "fl"

## Example 2

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

## Constraints

* 1 <= strs.length <= 200
* 0 <= strs[i].length <= 200
* strs[i] consists of only lowercase English letters.
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual("fl", self.longestCommonPrefix(["flower", "flow", "flight"]))

    def test_example_2(self):
        self.assertEqual("", self.longestCommonPrefix(["dog", "racecar", "car"]))

    def test_only_one_string(self):
        self.assertEqual("foo", self.longestCommonPrefix(["foo"]))

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        buf = ""
        should_continue = True
        ptr = 0
        while should_continue:
            if ptr >= len(strs[0]):
                should_continue = False
                break

            buf = strs[0][ptr]
            for s in strs:
                if ptr >= len(s):
                    should_continue = False
                    break

                if buf != s[ptr]:
                    should_continue = False
                    break

            ptr += 1
            if should_continue:
                prefix.append(buf)

        return "".join(prefix)
