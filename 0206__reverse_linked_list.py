"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

## Example 1

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

## Example 2

Input: head = [1,2]
Output: [2,1]

## Example 3

Input: head = []
Output: []

## Constraints

* The number of nodes in the list is the range [0, 5000].
* -5000 <= Node.val <= 5000

## Follow up

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import Optional
from unittest import TestCase

from lib.ListNode import ListNode, build_list, flatten_list


class Solution(TestCase):
    def test_example_1(self):
        head = build_list([1, 2, 3, 4, 5])

        self.assertEqual([5, 4, 3, 2, 1], flatten_list(self.reverseList(head)))

    def test_example_2(self):
        self.assertEqual([2, 1], flatten_list(self.reverseList(build_list([1, 2]))))

    def test_example_3(self):
        self.assertEqual([], flatten_list(self.reverseList(None)))

    def test_single_node(self):
        self.assertEqual([1], flatten_list(self.reverseList(build_list([1]))))

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        parent = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return parent
