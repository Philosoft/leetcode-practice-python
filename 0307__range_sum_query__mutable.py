"""
LeetCode: https://leetcode.com/problems/range-sum-query-mutable/

Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

* `NumArray(int[] nums)` Initializes the object with the integer array nums.
* `void update(int index, int val)` Updates the value of `nums[index]` to be val.
* `int sumRange(int left, int right)` Returns the sum of the elements of nums between indices left and right inclusive
(i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).

## Example 1

Input
    ["NumArray", "sumRange", "update", "sumRange"]
    [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
    [null, 9, null, 8]

Explanation

```
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
```

## Constraints

* 1 <= nums.length <= 3 * 10^4
* -100 <= nums[i] <= 100
* 0 <= index < nums.length
* -100 <= val <= 100
* 0 <= left <= right < nums.length
* At most 3 * 10^4 calls will be made to update and sumRange.
"""
from dataclasses import dataclass
from typing import List, Optional
from unittest import TestCase


@dataclass
class SegmentTreeNode:
    left: Optional['SegmentTreeNode']
    right: Optional['SegmentTreeNode']
    left_boundary: int
    right_boundary: int
    sum: int = 0

    @staticmethod
    def build(nums: List[int], left: int, right: int) -> 'SegmentTreeNode':
        if left == right:
            return SegmentTreeNode(None, None, left, left, nums[left])

        mid = left + (right - left) // 2
        root = SegmentTreeNode(None, None, left, right)
        root.left = SegmentTreeNode.build(nums, left, mid)
        root.right = SegmentTreeNode.build(nums, mid + 1, right)
        root.sum = root.left.sum + root.right.sum

        return root

    def get_sum(self, left: int, right: int) -> int:
        if self.left_boundary == left and self.right_boundary == right:
            return self.sum

        mid = self.left_boundary + (self.right_boundary - self.left_boundary) // 2
        if left > mid:
            # whole segment is on the right
            return self.right.get_sum(left, right)
        elif right <= mid:
            # whole segment is on the right
            return self.left.get_sum(left, right)

        # segment is spread across branches
        return self.left.get_sum(left, mid) + self.right.get_sum(mid + 1, right)

    def update(self, idx: int, val: int) -> None:
        if self.left_boundary == self.right_boundary == idx:
            self.sum = val
            return

        if self.left.left_boundary <= idx <= self.left.right_boundary:
            self.left.update(idx, val)
        else:
            self.right.update(idx, val)

        self.sum = self.left.sum + self.right.sum


class NumArray:
    def __init__(self, nums: List[int]):
        self.tree = SegmentTreeNode.build(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.get_sum(left, right)


class TestNumArray(TestCase):
    def test_example_1(self):
        numArray = NumArray([1, 3, 5])
        self.assertEqual(9, numArray.sumRange(0, 2))
        numArray.update(1, 2)
        self.assertEqual(8, numArray.sumRange(0, 2))

    def test_case_11(self):
        n = NumArray([0, 9, 5, 7, 3])
        self.assertEqual(3, n.sumRange(4, 4))
        self.assertEqual(15, n.sumRange(2, 4))
        self.assertEqual(7, n.sumRange(3, 3))

        n.update(4, 5)
        n.update(1, 7)
        n.update(0, 8)

        self.assertEqual(12, n.sumRange(1, 2))
        n.update(1, 9)

        self.assertEqual(5, n.sumRange(4, 4))

        n.update(3, 4)
