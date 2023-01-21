"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

## Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

## Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

## Constraints:

* 1 <= s1.length, s2.length <= 10^4
* s1 and s2 consist of lowercase English letters.
"""
from collections import Counter
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertTrue(self.checkInclusion("ab", "eidbaooo"))

    def test_example_2(self):
        self.assertFalse(self.checkInclusion("ab", "eidboaoo"))

    def test_leetcode_fail(self):
        self.assertTrue(self.checkInclusion("abc", "cccccbabbbaaaa"))

    def test_hello(self):
        self.assertFalse(self.checkInclusion("hello", "ooolleoooleh"))

    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        left, right = 0, 0
        matched_letters = 0
        while right < len(s2):
            while right < len(s2) and s2[right] not in counter:
                right += 1

            # found first matching letter
            # let's try to match as much as we can
            left = right
            while right < len(s2) and s2[right] in counter:
                # count
                counter[s2[right]] -= 1
                matched_letters += 1
                if counter[s2[right]] == -1:
                    # not a match
                    # shrink window from left until it fits
                    while counter[s2[right]] != 0:
                        counter[s2[left]] += 1
                        matched_letters -= 1
                        left += 1
                if matched_letters == len(s1):
                    return True
                right += 1
            # if we are here, then we didn't find a full match
            # move left -> right and restore counter
            while left < right:
                counter[s2[left]] += 1
                left += 1
                matched_letters -= 1
        return matched_letters == len(s1)

    def checkInclusionUnoptimized(self, s1: str, s2: str) -> bool:
        original = Counter(s1)
        cnt = original.copy()
        i = 0
        while i < len(s2):
            while i < len(s2) and s2[i] not in cnt:
                i += 1
            cnt = original.copy()

            rewind = i + 1
            while i < len(s2) and s2[i] in cnt:
                cnt[s2[i]] -= 1
                if all(map(lambda x: x == 0, cnt.values())):
                    return True
                if cnt[s2[i]] < 0:
                    cnt = original.copy()
                    i = rewind
                    break
                i += 1
        return all(map(lambda x: x == 0, cnt.values()))
