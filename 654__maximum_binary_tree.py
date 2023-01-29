"""
You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using
the following algorithm:

* Create a root node whose value is the maximum value in nums.
* Recursively build the left subtree on the subarray prefix to the left of the maximum value.
* Recursively build the right subtree on the subarray suffix to the right of the maximum value.
* Return the maximum binary tree built from nums.

## Example 1:

Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation:

The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.

## Example 2:

Input: nums = [3,2,1]
Output: [3,null,2,null,1]

## Constraints:

* 1 <= nums.length <= 1000
* 0 <= nums[i] <= 1000
* All integers in nums are unique.
"""
from collections import deque
from typing import List, Optional
from unittest import TestCase

from lib.TreeNode import TreeNode


class Solution(TestCase):
    def test_example_1(self):
        roots = []
        nums = [3, 2, 1, 6, 0, 5]
        roots.append(self.constructMaximumBinaryTree(nums))
        roots.append(self.constructMaximumBinaryTreeIterative(nums))

        for root in roots:
            self.assertEqual(6, root.val)
            self.assertEqual(5, root.right.val)
            self.assertEqual(3, root.left.val)

    def constructMaximumBinaryTreeIterative(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        process = deque()
        build = deque()

        m = max(nums)
        m_idx = nums.index(m)
        root = TreeNode(m)
        process.append(nums[:m_idx])
        process.append(nums[m_idx + 1:])
        while process:
            for partition in [process.popleft(), process.popleft()]:
                if partition:
                    part_max = max(partition)
                    part_idx = partition.index(part_max)
                    build.append(part_max)
                    process.append(partition[:part_idx])
                    process.append(partition[part_idx + 1:])
                else:
                    build.append(None)

        level = deque([root])
        while build:
            for _ in range(len(level)):
                node = level.popleft()
                left, right = build.popleft(), build.popleft()
                if node:
                    node.left = TreeNode(left) if left is not None else None
                    node.right = TreeNode(right) if right is not None else None
                    if node.left:
                        level.append(node.left)
                    if node.right:
                        level.append(node.right)

        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        m = max(nums)
        m_idx = nums.index(m)
        node = TreeNode(m)
        node.left, node.right = self.constructMaximumBinaryTree(nums[:m_idx]), self.constructMaximumBinaryTree(
            nums[m_idx + 1:])

        return node
