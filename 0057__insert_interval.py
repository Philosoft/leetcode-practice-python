"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start
and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval
newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and intervals still
does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input:
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input:
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

* 0 <= intervals.length <= 10^4
* intervals[i].length == 2
* 0 <= starti <= endi <= 10^5
* intervals is sorted by starti in ascending order.
* newInterval.length == 2
* 0 <= start <= end <= 10^5
"""

from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_examples(self):
        options = [
            ([[1, 5], [6, 9]], [[1, 3], [6, 9]], [2, 5]),
            ([[1, 2], [3, 10], [12, 16]], [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
            ([[1, 2]], [], [1, 2]),
            ([[0, 0], [1, 5]], [[1, 5]], [0, 0]),
            ([[0, 5], [7, 16]], [[0, 5], [9, 12]], [7, 16]),
            ([[3, 5], [6, 6], [12, 15]], [[3, 5], [12, 15]], [6, 6]),
        ]
        for expected, intervals, new_interval in options:
            with self.subTest():
                self.assertEqual(expected, self.insert(intervals, new_interval))
                self.assertEqual(expected, self.insertNew(intervals, new_interval))

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        result = []
        insert_position = None

        for interval in intervals:
            if interval[0] <= new_start <= interval[1] or new_start <= interval[0] <= new_end:
                new_start, new_end = min(interval[0], new_start), max(interval[1], new_end)
                if insert_position is None:
                    result.append([new_start, new_end])
                    insert_position = len(result) - 1
                else:
                    result[insert_position] = [new_start, new_end]
            elif insert_position is None and new_start <= interval[0]:
                result.append([new_start, new_end])
                insert_position = len(result) - 1
                result.append(interval)
            else:
                result.append(interval)

        if insert_position is None:
            result.append(newInterval)

        return result

    def insertNew(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(newInterval) == 0:
            return intervals

        interval_inserted = False
        result = []

        i = 0
        while i < len(intervals):
            if not interval_inserted:
                if len(result) > 0:
                    # intersects with previous
                    if (
                        result[-1][0] <= newInterval[0] <= result[-1][1]
                        or newInterval[0] <= result[-1][0] <= newInterval[1]
                    ):
                        result[-1][0] = min(newInterval[0], result[-1][0])
                        result[-1][1] = max(newInterval[1], result[-1][1])
                        interval_inserted = True
                    # perfect fit
                    elif result[-1][0] < newInterval[0] < intervals[i][0]:
                        result.append(newInterval)
                        interval_inserted = True
                elif newInterval[0] < intervals[i][0]:
                    result.append(newInterval)
                    interval_inserted = True

            # just merge/copy as we go
            if len(result) > 0 and result[-1][0] <= intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])

            i += 1

        if not interval_inserted:
            if (
                len(result) > 0
                and (
                    result[-1][0] <= newInterval[0] <= result[-1][1]
                    or newInterval[0] <= result[-1][0] <= newInterval[1]
                )
            ):
                result[-1][0] = min(result[-1][0], newInterval[0])
                result[-1][1] = max(result[-1][1], newInterval[1])
            else:
                result.append(newInterval)

        return result
