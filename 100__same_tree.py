import unittest
from typing import Optional

from lib.TreeNode import TreeNode, build_tree


class Solution(unittest.TestCase):
    def generate_test_options(self):
        options = [
            (True, [1, 2, 3], [1, 2, 3]),
            (True, [], []),
            (False, [1, 2, 1], [1, 1, 2]),
            (False, [], [1]),
            (True, [1], [1]),
            (False, [1, 2, None], [1, None, 2])
        ]

        for expected, left, right in options:
            yield (expected, build_tree(left), build_tree(right))

    def test(self) -> None:
        for expected, left, right in self.generate_test_options():
            with self.subTest():
                self.assertEqual(expected, self.isSameTree(left, right))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
