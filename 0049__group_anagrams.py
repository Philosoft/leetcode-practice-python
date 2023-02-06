"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.

## Example 1

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

## Example 2

Input: strs = [""]
Output: [[""]]

## Example 3

Input: strs = ["a"]
Output: [["a"]]

## Constraints

* 0 <= strs.length <= 10^4
* 0 <= strs[i].length <= 100
* strs[i] consists of lowercase English letters.
"""
from collections import defaultdict
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        for i in range(len(expected)):
            expected[i].sort()
        expected.sort()

        answer = self.groupAnagrams(strings)
        for i in range(len(answer)):
            answer[i].sort()
        answer.sort()

        self.assertEqual(expected, answer)

    def test_example_2(self):
        self.assertEqual([[""]], self.groupAnagrams([""]))

    def test_example_3(self):
        self.assertEqual([["a"]], self.groupAnagrams(["a"]))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            counter = {}
            for i in range(26):
                char = chr(ord('a') + i)
                counter[char] = 0

            for char in word:
                counter[char] += 1

            key = "".join([f"{letter}#{cnt}" for letter, cnt in counter.items()])

            result[key].append(word)

        return list(result.values())
