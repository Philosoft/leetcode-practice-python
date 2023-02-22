"""
LeetCode: https://leetcode.com/problems/non-overlapping-intervals/description/

[[Blind75]]

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you
need to remove to make the rest of the intervals non-overlapping.

## Example 1

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

## Example 2

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

## Example 3

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


## Constraints

* 1 <= intervals.length <= 10^5
* intervals[i].length == 2
* -5 * 10^4 <= starti < endi <= 5 * 10^4
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_it(self):
        options = [
            ('example 1', 1, [[1, 2], [2, 3], [3, 4], [1, 3]]),
            ('example 2', 2, [[1, 2], [1, 2], [1, 2]]),
            ('example 3', 0, [[1, 2], [2, 3]]),
        ]

        for name, expected, intervals in options:
            with self.subTest(name):
                self.assertEqual(expected, self.eraseOverlapIntervals(intervals))

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        answer = 0
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            current = intervals[i]
            if current[0] < right:
                answer += 1
                right = min(right, current[1])
            else:
                right = current[1]

        return answer
