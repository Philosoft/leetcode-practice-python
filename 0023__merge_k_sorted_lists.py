"""
LeetCode link https://leetcode.com/problems/merge-k-sorted-lists/description/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

## Example 1

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation:
    The linked-lists are:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6

## Example 2

Input: lists = []
Output: []

## Example 3

Input: lists = [[]]
Output: []

## Constraints

* k == lists.length
* 0 <= k <= 10^4
* 0 <= lists[i].length <= 500
* -10^4 <= lists[i][j] <= 10^4
* lists[i] is sorted in ascending order.
* The sum of lists[i].length will not exceed 10^4.
"""
import math
from typing import List, Optional
from unittest import TestCase

from lib.ListNode import ListNode, build_list, flatten_list


class Solution(TestCase):
    def test_example_1(self):
        lists = list(map(build_list, [[1, 4, 5], [1, 3, 4], [2, 6]]))
        expected = [1, 1, 2, 3, 4, 4, 5, 6]

        self.assertEqual(expected, flatten_list(self.mergeKLists(lists)))

    def test_example_2(self):
        self.assertEqual([], flatten_list(self.mergeKLists([])))

    def test_example_3(self):
        self.assertEqual(None, self.mergeKLists([None]))

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        while True:
            min_index = -1
            min_val = math.inf
            for idx, l in enumerate(lists):
                if not l:
                    continue

                if lists[idx].val < min_val:
                    min_val = lists[idx].val
                    min_index = idx

            if min_index == -1:
                break

            head.next = lists[min_index]
            lists[min_index] = lists[min_index].next
            head = head.next

        return dummy.next
