import unittest
from typing import Optional

from lib.ListNode import build_list, ListNode, flatten_list


class Solution(unittest.TestCase):
    def test_example_1(self):
        head = build_list([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 5]

        self.assertEqual(expected, flatten_list(self.removeNthFromEnd(head, 2)))

    def test_example_2(self):
        self.assertEqual([], flatten_list(self.removeNthFromEnd(build_list([1]), 1)))

    def test_example_3(self):
        self.assertEqual([1], flatten_list(self.removeNthFromEnd(build_list([1, 2]), 1)))

    def test_empty(self):
        self.assertIsNone(self.removeNthFromEnd(None, 0))

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            n -= 1
            right = right.next

        while right:
            right, left = right.next, left.next

        left.next = left.next.next

        return dummy.next

    def removeNthFromEndTwoPass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 0
        h = head
        while h:
            length += 1
            h = h.next

        target = length - n
        ptr, prev = head, None
        while target:
            target -= 1
            ptr, prev = ptr.next, ptr

        # deletion of head
        if not prev:
            return head.next

        # general case
        prev.next = ptr.next
        return head
