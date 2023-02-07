from unittest import TestCase

from lib.TreeNode import TreeNode, build_tree


class Solution(TestCase):
    def test_example_1(self):
        root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = root.left
        q = root.right

        self.assertEqual(root, self.lowestCommonAncestor(root, p, q))
        self.assertEqual(root, self.lowestCommonAncestorFirstApproach(root, p, q))

    def test_example_2(self):
        root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = root.left
        q = root.left.right

        self.assertEqual(root.left, self.lowestCommonAncestor(root, p, q))
        self.assertEqual(root.left, self.lowestCommonAncestorFirstApproach(root, p, q))

    def test_example_3(self):
        root = build_tree([2, 1, None])
        p = root
        q = root.left

        self.assertEqual(root, self.lowestCommonAncestor(root, p, q))
        self.assertEqual(root, self.lowestCommonAncestorFirstApproach(root, p, q))

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return root

    def lowestCommonAncestorFirstApproach(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path = []

        def trace_path(start: TreeNode, target: int) -> None:
            path.append(start.val)

            if start.val == target:
                return

            if target > start.val:
                return trace_path(start.right, target)
            return trace_path(start.left, target)

        trace_path(root, p.val)
        path1 = path.copy()
        path = []
        trace_path(root, q.val)
        path2 = path

        if len(path1) >= len(path2):
            search_in = set(path1)
            search_from = path2
        else:
            search_in = set(path2)
            search_from = path1
        while search_from:
            t = search_from.pop()
            if t in search_in:
                intersection = t
                break
        h = root
        while True:
            if h.val == intersection:
                return h

            if intersection > h.val:
                h = h.right
            else:
                h = h.left
