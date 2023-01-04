import unittest
from typing import Optional, List

from lib.TreeNode import TreeNode, build_tree


class Solution(unittest.TestCase):
    def test_example_1(self):
        root = build_tree([1, 2, 3, None, 5])
        expected = ["1->2->5", "1->3"]
        expected.sort()

        answer = self.binaryTreePaths(root)
        answer.sort()

        self.assertEqual(answer, expected)

    def test_example_2(self):
        root = build_tree([1])
        expected = ["1"]

        self.assertEqual(self.binaryTreePaths(root), expected)

    def test_empty_tree(self):
        self.assertEqual(self.binaryTreePaths(None), [])

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        paths = []
        path = []

        def dfs(node: TreeNode):
            if not node.left and not node.right:
                path.append(node.val)
                paths.append('->'.join(map(str, path)))
                path.pop()
                return

            path.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

            if path:
                path.pop()

        dfs(root)

        return paths
