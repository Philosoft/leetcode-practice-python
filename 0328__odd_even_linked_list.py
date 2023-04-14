"""
LeetCode: https://leetcode.com/problems/odd-even-linked-list/
"""
from typing import Optional
from unittest import TestCase

from lib.ListNode import ListNode, build_list, flatten_list


class Solution(TestCase):
    def test_example_1(self):
        head = build_list([1, 2, 3, 4, 5])
        self.assertEqual([1, 3, 5, 2, 4], flatten_list(self.oddEvenList(head)))

    def test_example_2(self):
        head = build_list([2, 1, 3, 5, 6, 4, 7])
        expected = [2, 3, 6, 7, 1, 5, 4]

        self.assertEqual(expected, flatten_list(self.oddEvenList(head)))

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # lists with 0, 1 or 2 nodes do not require any work
        if not head or not head.next or not head.next.next:
            return head

        odd_tail, even_head, even_tail = head, head.next, head.next
        pointer = head.next.next
        while pointer:
            odd_tail.next, even_tail.next = pointer, pointer.next
            odd_tail, even_tail = odd_tail.next, even_tail.next

            if pointer.next:
                pointer = pointer.next.next
            else:
                pointer = None

        odd_tail.next = even_head

        return head
