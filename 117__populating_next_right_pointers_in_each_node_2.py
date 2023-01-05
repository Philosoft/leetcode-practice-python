from collections import deque
from typing import Optional

from lib.TreeNode import TreeNode


class Solution:
    def connect(self, root: TreeNode) -> Optional[TreeNode]:
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
