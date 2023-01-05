from collections import deque
from typing import Optional

from lib.TreeNode import TreeNode


class Solution:
    def connect(selfself, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        left = TreeNode()
        leftmost = root.left if root.left else root.right
        if root.left and root.right:
            root.left.next = root.right

        parent = leftmost

        while parent:
            if not leftmost:
                leftmost = parent.left if parent.left else parent.right

            if parent.left:
                left.next = parent.left
                left = parent.left
            if parent.right:
                left.next = parent.right
                left = parent.right

            if parent.next:
                parent = parent.next
            else:
                parent = leftmost
                leftmost = None
                left = TreeNode()

        return root

    def connectBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = deque([root])
        while q:
            left = None
            for _ in range(len(q)):
                node = q.popleft()
                if not left:
                    left = node
                else:
                    left.next = node
                    left = node

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root
