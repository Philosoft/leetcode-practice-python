"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:

* The number of nodes in the list is in the range [1, 100].
* 1 <= Node.val <= 100
"""
from typing import Optional
from unittest import TestCase

from lib.ListNode import ListNode, build_list, flatten_list


class Solution(TestCase):
    def test_example_1(self):
        head = build_list([1, 2, 3, 4, 5])
        out = self.middleNode(head)

        self.assertEqual([3, 4, 5], flatten_list(out))

    def test_example_2(self):
        head = build_list([1, 2, 3, 4, 5, 6])
        out = self.middleNode(head)

        self.assertEqual([4, 5, 6], flatten_list(out))

    def test_empty_list(self):
        self.assertIsNone(self.middleNode(None))

    def test_single_node(self):
        head = build_list([1])
        out = self.middleNode(head)

        self.assertEqual([1], flatten_list(out))

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        return slow.next if fast else slow
