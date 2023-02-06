from typing import Optional
from unittest import TestCase

from lib.ListNode import ListNode, build_list


class Solution(TestCase):
    def test_example_1(self):
        head = build_list([3, 2, 0, -4])
        head.next.next.next.next = head.next

        self.assertTrue(self.hasCycle(head))

    def test_example_2(self):
        head = build_list([1, 2])
        head.next.next = head

        self.assertTrue(self.hasCycle(head))

    def test_example_3(self):
        self.assertFalse(self.hasCycle(build_list([1])))

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
