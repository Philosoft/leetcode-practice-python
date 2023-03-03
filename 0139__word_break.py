"""
LeetCode: https://leetcode.com/problems/word-break/

[[Blind75]]

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence
 of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

## Example 1

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

## Example 2

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation:
    Return true because "applepenapple" can be segmented as "apple pen apple".
    Note that you are allowed to reuse a dictionary word.

## Example 3

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

## Constraints

* 1 <= s.length <= 300
* 1 <= wordDict.length <= 1000
* 1 <= wordDict[i].length <= 20
* s and wordDict[i] consist of only lowercase English letters.
* All the strings of wordDict are unique.
"""
from typing import List, Set
from unittest import TestCase


class Solution(TestCase):
    def test_it(self):
        options = [
            ('example 1', True, "leetcode", ["leet", "code"]),
            ('example 2', True, "applepenapple", ["apple", "pen"]),
            ('example 3', False, "catsandog", ["cats", "dog", "sand", "and", "cat"]),
        ]

        for name, expected, string, dictionary in options:
            with self.subTest(name):
                self.assertEqual(expected, self.wordBreak(string, dictionary))
                self.assertEqual(expected, self.wordBreakMemo(string, dictionary))

    def wordBreakMemo(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def helper(remainder: str) -> bool:
            if remainder == "":
                return True

            if remainder in cache:
                return cache[remainder]

            for word in wordDict:
                if len(word) <= len(remainder) and word == remainder[:len(word)]:
                    rest_of_word = remainder[len(word):]
                    res = helper(rest_of_word)
                    cache[rest_of_word] = res
                    if res:
                        return True

            cache[remainder] = False
            return False

        return helper(s)


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictionary = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) < len(dp):
                    dp[i] = s[i:i + len(word)] in dictionary and dp[i + len(word)]

                if dp[i]:
                    break

        return dp[0]
