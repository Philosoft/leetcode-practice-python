from typing import Optional
from unittest import TestCase

from lib.ListNode import ListNode, build_list, flatten_list


class Solution(TestCase):
    def test_example_1(self):
        head = build_list([1, 1, 2])
        self.assertEqual([1, 2], flatten_list(self.deleteDuplicates(head)))

    def test_example_2(self):
        head = build_list([1, 1, 2, 3, 3])
        self.assertEqual([1, 2, 3], flatten_list(self.deleteDuplicates(head)))

    def test_empty_list(self):
        self.assertIsNone(self.deleteDuplicates(None))

    def test_single_node(self):
        self.assertEqual([1], flatten_list(self.deleteDuplicates(build_list([1]))))

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        h = head
        while h.next:
            if h.val == h.next.val:
                h.next = h.next.next
            else:
                h = h.next

        return head
