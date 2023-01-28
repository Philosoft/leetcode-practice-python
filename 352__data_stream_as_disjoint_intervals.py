"""
Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of
disjoint intervals.

Implement the SummaryRanges class:

SummaryRanges() Initializes the object with an empty stream.
void addNum(int value) Adds the integer value to the stream.
int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals
[starti, endi]. The answer should be sorted by starti.


## Example 1:

Input
    [
    "SummaryRanges",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals",
    "addNum",
    "getIntervals"
    ]
    [[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
    [
        null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]],
        null, [[1, 3], [6, 7]]
    ]

## Explanation
    SummaryRanges summaryRanges = new SummaryRanges();
    summaryRanges.addNum(1);      // arr = [1]
    summaryRanges.getIntervals(); // return [[1, 1]]
    summaryRanges.addNum(3);      // arr = [1, 3]
    summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
    summaryRanges.addNum(7);      // arr = [1, 3, 7]
    summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
    summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
    summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
    summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
    summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]

## Constraints:

* 0 <= value <= 10^4
* At most 3 * 10^4 calls will be made to addNum and getIntervals.

Follow up: What if there are lots of merges and the number of disjoint intervals is small compared to the size of the
data stream?
"""
from typing import List, Dict, Optional
from unittest import TestCase


class UnionFind:
    def __init__(self):
        self.parents: Dict[int, int] = {}
        self.intervals: Dict[int, List[int]] = {}

    def exists(self, n: int) -> bool:
        return n in self.parents

    def add(self, n: int) -> None:
        self.parents[n] = n
        self.intervals[n] = [n, n]

    def find(self, n: int) -> Optional[int]:
        if not self.exists(n):
            return None

        if self.parents[n] != n:
            self.parents[n] = self.find(self.parents[n])

        return self.parents[n]

    def union(self, a: int, b: int) -> None:
        a_root = self.find(a)
        b_root = self.find(b)

        if a_root is None or b_root is None:
            return

        self.parents[a_root] = b_root

        # interval adjusting
        a_interval = self.intervals[a_root]
        del self.intervals[a_root]

        self.intervals[b_root] = [min(self.intervals[b_root][0], a_interval[0]),
                                  max(self.intervals[b_root][1], a_interval[1])]


class SummaryRanges:
    def __init__(self):
        self.uf = UnionFind()

    def addNum(self, val: int) -> None:
        if self.uf.exists(val):
            return

        self.uf.add(val)

        self.uf.union(val, val - 1)
        self.uf.union(val, val + 1)

    def getIntervals(self) -> List[List[int]]:
        return sorted(self.uf.intervals.values())


class TestSummaryRanges(TestCase):
    def test_it(self):
        sr = SummaryRanges()
        sr.addNum(1)  # arr = [1]
        self.assertEqual([[1, 1]], sr.getIntervals())
        sr.addNum(3)  # arr = [1, 3]
        self.assertEqual([[1, 1], [3, 3]], sr.getIntervals())
        sr.addNum(7)  # arr = [1, 3, 7]
        self.assertEqual([[1, 1], [3, 3], [7, 7]], sr.getIntervals())
        sr.addNum(2)  # arr = [1, 2, 3, 7]
        self.assertEqual([[1, 3], [7, 7]], sr.getIntervals())
        sr.addNum(6)  # arr = [1, 2, 3, 6, 7]
        self.assertEqual([[1, 3], [6, 7]], sr.getIntervals())
