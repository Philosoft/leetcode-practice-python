"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
and the median is the mean of the two middle values.

* For example, for arr = [2,3,4], the median is 3.
* For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

* `MedianFinder()` initializes the MedianFinder object.
* `void addNum(int num)` adds the integer num from the data stream to the data structure.
* `double findMedian()` returns the median of all elements so far. Answers within 10-5 of the actual answer will be
accepted.

## Example 1

Input
```
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
```

Output

```
[null, null, null, 1.5, null, 2.0]
```

### Explanation

```
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

## Constraints

* -10^5 <= num <= 10^5
* There will be at least one element in the data structure before calling findMedian.
* At most 5 * 10^4 calls will be made to addNum and findMedian.

## Follow up

* If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
* If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""
from heapq import heappush, heappop
from unittest import TestCase


class MedianFinder:
    def __init__(self):
        # [a, b, c, d | e, f, g, h]
        # ^^^^^^^^^^^^  |  |  |  |
        # self.small    |  |  |  |
        #               ^^^^^^^^^^
        #               self.large
        # d - self.small[0]
        # e - self.large[0]

        self.small = []  # max heap
        self.large = []  # min min heap

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)
        if self.small and self.large and -self.small[0] > self.large[0]:
            heappush(self.large, -heappop(self.small))

        # check size and balance if needed
        if len(self.small) > len(self.large) + 1:
            heappush(self.large, -heappop(self.small))

        if len(self.small) + 1 < len(self.large):
            heappush(self.small, -heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            # left side is bigger
            # take the biggest number from left side
            return -self.small[0]

        if len(self.small) < len(self.large):
            # right side is bigger
            # take the smallest number from right side
            return self.large[0]

        # sides are balanced
        return (-self.small[0] + self.large[0]) / 2


class MedianFinderTest(TestCase):
    def test_it(self):
        mf = MedianFinder();
        mf.addNum(1)
        mf.addNum(2)
        self.assertEqual(1.5, mf.findMedian())
        mf.addNum(3)
        self.assertEqual(2.0, mf.findMedian())
