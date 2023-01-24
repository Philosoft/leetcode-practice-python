"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1
=========

Input:
    mat = [
        [ 0, 0, 0 ],
        [ 0, 1, 0 ],
        [ 0, 0, 0 ],
    ]
Output:
    [
        [ 0, 0, 0 ],
        [ 0, 1, 0 ],
        [ 0, 0, 0 ],
    ]

Example 2
=========

Input:
    mat = [
        [ 0, 0, 0 ],
        [ 0, 1, 0 ],
        [ 1, 1, 1 ],
    ]
Output:
    [
        [ 0, 0, 0 ],
        [ 0, 1, 0 ],
        [ 1, 2, 1 ],
    ]


Constraints
===========

* m == mat.length
* n == mat[i].length
* 1 <= m, n <= 10^4
* 1 <= m * n <= 10^4
* mat[i][j] is either 0 or 1.
* There is at least one 0 in mat.
"""
from collections import deque
from typing import List, Tuple, Set
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        mat = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]
        expected = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]

        self.assertEqual(expected, self.updateMatrix(mat))

    def test_example_2(self):
        mat = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 1, 1],
        ]
        expected = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 2, 1],
        ]

        self.assertEqual(expected, self.updateMatrix(mat))

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        first idea

        simply go through matrix, when encounter 1 - launch BFS to find closest 0, update current position
        rinse, repeat, victory

        T: O(n ^ 2)
            O(n) - go through matrix once
            O(n) - for each separate BFS
        S: O(n)
            for queue and visited set

        second idea

        same as first, but with "dynamic programming". since when going from left to right, top to bottom
        at the moment when we encounter 1, we already computed everything on the left and on the top of current cell
        so BFS will be half as short (right and bottom)
        may be there is a way to optimize it further

        third idea

        do it in reverse. go through every cell in a matrix and put "zero" cells in a q
        then work inwards with usual 1 pass BFS
        since it's guaranteed for at least one zero to be present in matrix, that's a sure fire way
        """
        result = mat.copy()
        q = deque([])
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 0:
                    q.append((row, col))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited: Set[Tuple[int, int]] = set()
        while q:
            current_row, current_col = q.popleft()
            for dr, dc in directions:
                r, c = current_row + dr, current_col + dc
                if 0 <= r < len(mat) and 0 <= c < len(mat[r]) and (r, c) not in visited and mat[r][c] != 0:
                    result[r][c] = mat[current_row][current_col] + 1
                    visited.add((r, c))
                    q.append((r, c))
        return result
