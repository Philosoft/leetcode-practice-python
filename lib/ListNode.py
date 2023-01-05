import unittest
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class ListNode:
    val: int = 0
    next: Optional['ListNode'] = None


def build_list(nums: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    h = dummy
    for n in nums:
        h.next = ListNode(n)
        h = h.next

    return dummy.next


def flatten_list(head: Optional[ListNode]) -> List[int]:
    flat = []
    h = head
    while h:
        flat.append(h.val)
        h = h.next

    return flat


class TestList(unittest.TestCase):
    def test_empty_build(self):
        self.assertIsNone(build_list([]))

    def test_empty_flatten(self):
        self.assertEqual([], flatten_list(None))

    def test_build_1(self):
        head = build_list([1])

        self.assertIsNotNone(head)
        self.assertIsInstance(head, ListNode)
        self.assertEqual(1, head.val)
        self.assertIsNone(head.next)

    def test_flatten_1(self):
        head = ListNode(1)

        self.assertEqual([1], flatten_list(head))

    def test_flatten_2(self):
        head = ListNode(1)
        head.next = ListNode(10)

        self.assertEqual([1, 10], flatten_list(head))

    def test_build_2(self):
        self.assertEqual([1, 2, 3], flatten_list(build_list([1, 2, 3])))
