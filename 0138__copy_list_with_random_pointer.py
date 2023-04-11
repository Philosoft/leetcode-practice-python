"""
LeetCode: https://leetcode.com/problems/copy-list-with-random-pointer/description/
"""
from typing import Optional
from unittest import TestCase
from dataclasses import dataclass


@dataclass
class Node:
    val: int = 0
    next: 'Node' = None
    random: 'Node' = None


class Solution(TestCase):
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        mapping = {}

        def deep(node: Optional[Node]) -> Optional[Node]:
            if not node:
                return None

            if node in mapping:
                return mapping[node]

            new_node = Node(node.val)
            mapping[node] = new_node
            new_node.random = deep(node.random)
            new_node.next = deep(node.next)

            return new_node

        return deep(head)
