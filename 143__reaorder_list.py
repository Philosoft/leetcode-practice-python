"""
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

## Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

## Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

## Constraints:

* The number of nodes in the list is in the range [1, 5 * 10^4].
* 1 <= Node.val <= 1000
"""
from typing import Optional
from unittest import TestCase

from lib.ListNode import ListNode, build_list, flatten_list


class Solution(TestCase):
    def test_example_1(self):
        head = build_list([1, 2, 3, 4])
        expected = [1, 4, 2, 3]
        self.reorderList(head)

        self.assertEqual(expected, flatten_list(head))

    def test_example_2(self):
        head = build_list([1, 2, 3, 4, 5])
        expected = [1, 5, 2, 4, 3]
        self.reorderList(head)

        self.assertEqual(expected, flatten_list(head))

    def test_longer_even(self):
        head = build_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        expected = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

        self.reorderList(head)

        self.assertEqual(expected, flatten_list(head))

    def test_longer_odd(self):
        head = build_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        expected = [1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]

        self.reorderList(head)

        self.assertEqual(expected, flatten_list(head))

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # first, let's find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is now pointing exactly at the middle
        # now let's reverse second half of the list
        # that way we will have SLL tail -> middle
        def reverse(node: Optional[ListNode]) -> Optional[ListNode]:
            if not node or not node.next:
                return node

            parent = reverse(node.next)
            node.next.next = node
            node.next = None

            return parent

        tail = reverse(slow)

        # no we virtually have two lists
        # head -> middle
        # tail -> middle
        # all that's left to do is just rearrange pointers a bit
        h = head
        nxt = tail
        while h and tail and h != tail:
            if nxt == tail:
                h.next, nxt = nxt, h.next
                tail = tail.next
                h = h.next
            else:
                h.next, nxt = nxt, tail
                h = h.next
