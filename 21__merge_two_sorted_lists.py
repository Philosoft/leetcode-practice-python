"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.


Example 1:

Input:
    list1 = [1,2,4]
    list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input:
    list1 = []
    list2 = []
Output: []

Example 3:

Input:
    list1 = []
    list2 = [0]
Output: [0]

Constraints:

* The number of nodes in both lists is in the range [0, 50].
* -100 <= Node.val <= 100
* Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional
from unittest import TestCase

from lib.ListNode import ListNode, build_list, flatten_list


class Solution(TestCase):
    def test(self):
        options = [
            ('2 empty lists', [], [], []),
            ('1st is empty', [1], [1], []),
            ('2nd is empty', [2], [], [2]),
            ('generic case', [1, 1, 2, 3, 4, 4], [1, 2, 4], [1, 3, 4]),
        ]

        for name, expected, l1, l2 in options:
            with self.subTest(name):
                h1, h2 = build_list(l1), build_list(l2)
                self.assertEqual(expected, flatten_list(self.mergeTwoLists(h1, h2)))

                h1, h2 = build_list(l1), build_list(l2)
                self.assertEqual(expected, flatten_list(self.mergeTwoListsRecursive(h1, h2)))

    def mergeTwoListsRecursive(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            if list1:
                return list1
            if list2:
                return list2
            return None

        dummy = ListNode()
        h = dummy
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    h.next = list1
                    h = h.next
                    list1 = list1.next
                else:
                    h.next = list2
                    h = h.next
                    list2 = list2.next
            elif list1:
                h.next = list1
                list1 = None
            else: # list2
                h.next = list2
                list2 = None

        return dummy.next
