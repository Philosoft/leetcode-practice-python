import unittest
from collections import deque
from typing import Optional, List

from TreeNode import TreeNode, build_tree


class Solution(unittest.TestCase):
    def test_example_1(self):
        root = build_tree([1, 2, 3, None, 5, None, 4])
        expected = [1, 3, 4]

        self.assertEquals(self.rightSideView(root), expected)

    def test_example_2(self):
        root = build_tree([1, None, 3])

        self.assertEquals(self.rightSideView(root), [1, 3])

    def test_example_3(self):
        self.assertEquals(self.rightSideView(build_tree([])), [])

    def test_root_plus_left(self):
        self.assertEquals(self.rightSideView(build_tree([1, 2, None])), [1, 2])

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([])
        if root:
            q.append(root)

        result = []
        while q:
            for _ in range(len(q) - 1):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            rightmost_node = q.popleft()
            result.append(rightmost_node.val)
            if rightmost_node.left:
                q.append(rightmost_node.left)
            if rightmost_node.right:
                q.append(rightmost_node.right)

        return result
