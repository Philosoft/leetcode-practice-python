import unittest
from collections import deque
from typing import Optional

from lib.ListNode import ListNode, build_list


class Solution(unittest.TestCase):
    def test(self):
        options = [
            (6, [5, 4, 2, 1]),
            (7, [4, 2, 2, 3]),
            (100001, [1, 100000]),
        ]

        for expected, list_definition in options:
            with self.subTest(str(list_definition)):
                self.assertEqual(expected, self.pairSum(build_list(list_definition)))

    # O(n) time, O(1) space
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        # find the middle
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next

        # slow is in the beginning of second half now
        # reverse second half
        h = slow
        prev = None
        while h:
            h.next, prev, h = prev, h, h.next

        # now, just traverse both
        left, right = head, prev
        m = 0
        while left:
            m = max(m, left.val, right.val)
            left = left.next
            right = right.next

        return m

    # O(n) time, O(n) space, more complicated
    # 2 passes, but half the memory
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        m = 0
        stack = []
        length = 0
        fast, slow = head, head
        while fast:
            stack.append(slow.val)
            length += 1
            fast = fast.next.next
            slow = slow.next

        while slow:
            m = max(m, slow.val + stack.pop())
            slow = slow.next

        return m

    # O(n) time, O(n) space, simple
    def pairSumBrute(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        d = deque([])
        h = head
        while h:
            d.append(h.val)
            h = h.next

        m = 0
        while d:
            m = max(m, d.popleft() + d.pop())

        return m
