"""
LeetCode: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
"""
from dataclasses import dataclass
from typing import Optional, List
from unittest import TestCase

from lib.ListNode import flatten_list


@dataclass
class Node:
    val: int = 0
    prev: 'Node' = None
    next: 'Node' = None
    child: 'Node' = None


class Solution(TestCase):
    def create_from_list(self, l: List[int]):
        dummy = Node()
        tail = dummy
        for n in l:
            node = Node(n, tail)
            tail.next = node
            tail = tail.next

        if dummy.next:
            dummy.next.prev = None

        return dummy.next

    def test_empty_list(self):
        self.assertIsNone(self.flatten(None))

    def test_just_head(self):
        head = Node()
        self.assertEqual(head, self.flatten(head))

    def test_linear_list(self):
        self.assertEqual([1, 2, 3], flatten_list(self.flatten(self.create_from_list([1, 2, 3]))))

    def test_two_levels(self):
        first_level_head = self.create_from_list([1, 2, 3])
        second_level_head = self.create_from_list([4, 5, 6])
        first_level_head.next.child = second_level_head

        self.assertEqual([1, 2, 4, 5, 6, 3], flatten_list(self.flatten(first_level_head)))

    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        dummy = Node()
        tail = dummy
        while head:
            tail.next, head.prev = head, tail
            tail = tail.next
            nxt = head.next
            if head.child:
                # gateway to next level
                next_part = self.flatten(head.child)
                if next_part:
                    tail.next, next_part.prev = next_part, tail
                    while tail.next:
                        tail = tail.next
                head.child = None
            head = nxt

        if dummy.next:
            dummy.next.prev = None

        return dummy.next
