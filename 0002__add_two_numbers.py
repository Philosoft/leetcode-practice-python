"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Example 1

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

## Example 2

Input: l1 = [0], l2 = [0]
Output: [0]

## Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

## Constraints

* The number of nodes in each linked list is in the range [1, 100].
* 0 <= Node.val <= 9
* It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional
from unittest import TestCase

from lib.ListNode import ListNode, build_list, flatten_list


class Solution(TestCase):
    def test_example_1(self):
        l1 = build_list([2, 4, 3])
        l2 = build_list([5, 6, 4])

        self.assertEqual([7, 0, 8], flatten_list(self.addTwoNumbers(l1, l2)))

    def test_example_2(self):
        self.assertEqual([0], flatten_list(self.addTwoNumbers(build_list([0]), build_list([0]))))

    def test_example_3(self):
        l1 = build_list([9, 9, 9, 9, 9, 9, 9])
        l2 = build_list([9, 9, 9, 9])

        self.assertEqual([8, 9, 9, 9, 0, 0, 0, 1], flatten_list(self.addTwoNumbers(l1, l2)))

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        overflow = 0

        while l1 or l2:
            step = overflow
            if l1:
                step += l1.val
                l1 = l1.next
            if l2:
                step += l2.val
                l2 = l2.next

            if step >= 10:
                step -= 10
                overflow = 1
            else:
                overflow = 0

            node = ListNode(step)
            tail.next, tail = node, node

        if overflow == 1:
            tail.next = ListNode(1)

        return head.next
