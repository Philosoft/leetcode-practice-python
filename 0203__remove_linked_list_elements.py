"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
and return the new head.

## Example 1

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

## Example 2

Input: head = [], val = 1
Output: []

## Example 3:

Input: head = [7,7,7,7], val = 7
Output: []

## Constraints

* The number of nodes in the list is in the range [0, 104].
* 1 <= Node.val <= 50
* 0 <= val <= 50
"""
from typing import Optional
from unittest import TestCase

from lib.ListNode import ListNode, build_list, flatten_list


class Solution(TestCase):
    def test_example_1(self):
        head = build_list([1, 2, 6, 3, 4, 5, 6])

        self.assertEqual([1, 2, 3, 4, 5], flatten_list(self.removeElements(head, 6)))

    def test_example_2(self):
        self.assertEqual([], flatten_list(self.removeElements(None, 1)))

    def test_example_3(self):
        self.assertEqual([], flatten_list(self.removeElements(build_list([7, 7, 7, 7]), 7)))

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(666, head)
        head = dummy
        while head:
            while head.next and head.next.val == val:
                head.next = head.next.next
            head = head.next

        return dummy.next
