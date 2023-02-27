"""
LeetCode: https://leetcode.com/problems/construct-quad-tree/
"""
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Node:
    val: bool
    isLeaf: bool
    topLeft: Optional['Node'] = None
    topRight: Optional['Node'] = None
    bottomLeft: Optional['Node'] = None
    bottomRight: Optional['Node'] = None


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(size: int, origin_row: int, origin_column: int):
            all_the_same = True
            for row_offset in range(size):
                for col_offset in range(size):
                    if grid[origin_row][origin_column] != grid[origin_row + row_offset][origin_column + col_offset]:
                        all_the_same = False
                        break

            if all_the_same:
                return Node(grid[origin_row][origin_column] == 1, True)

            size //= 2
            root = Node(False, False)
            root.topLeft = helper(size, origin_row, origin_column)
            root.topRight = helper(size, origin_row, origin_column + size)
            root.bottomLeft = helper(size, origin_row + size, origin_column)
            root.bottomRight = helper(size, origin_row + size, origin_column + size)

            return root

        return helper(len(grid), 0, 0)
