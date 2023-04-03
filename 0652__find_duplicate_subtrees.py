"""
LeetCode: https://leetcode.com/problems/find-duplicate-subtrees/description/
"""
from collections import defaultdict
from typing import Optional, List, Dict

from lib.TreeNode import TreeNode


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hash_to_roots: Dict[str, List[TreeNode]] = defaultdict(list)

        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                return 'x'

            tree_hash = '(' + '(' + dfs(node.left) + ')' + f'({node.val})' + '(' + dfs(node.right) + ')' + ')'
            hash_to_roots[tree_hash].append(node)

            return tree_hash

        dfs(root)

        return list(map(lambda x: x[0], filter(lambda x: len(x) > 1, hash_to_roots.values())))
