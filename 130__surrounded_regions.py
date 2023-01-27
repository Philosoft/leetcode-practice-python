"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

## Example 1:

Input:
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
Output:
    [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]
    ]
Explanation:
    Notice that an 'O' should not be flipped if:
    - It is on the border, or
    - It is adjacent to an 'O' that should not be flipped.
    The bottom 'O' is on the border, so it is not flipped.
    The other three 'O' form a surrounded region, so they are flipped.

## Example 2:

Input: board = [["X"]]
Output: [["X"]]

## Constraints:

* m == board.length
* n == board[i].length
* 1 <= m, n <= 200
* board[i][j] is 'X' or 'O'.
"""
from collections import deque
from typing import Set, Tuple, List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
        expected = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"]
        ]

        self.solve(board)
        self.assertEqual(expected, board)

    def test_example_2(self):
        board = [["X"]]
        expected = [["X"]]

        self.solve(board)
        self.assertEqual(expected, board)

    def test_all_xes(self):
        board = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"]]
        expected = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"]]

        self.solve(board)
        self.assertEqual(expected, board)

    def test_all_zeroes(self):
        board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
        expected = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]

        self.solve(board)
        self.assertEqual(expected, board)

    def test_single_o_in_the_middle(self):
        board = [["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]]
        expected = [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]

        self.solve(board)
        self.assertEqual(expected, board)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        checked: Set[Tuple[int, int]] = set()

        def bfs(start_row: int, start_col: int):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            q = deque([(start_row, start_col)])

            checked.add((start_row, start_col))
            to_flip: Set[Tuple[int, int]] = set()
            should_flip = True
            already_in_q = set()
            while q:
                row, col = q.popleft()
                ok_directions = 0
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < len(board) and 0 <= new_col < len(board[new_row]):
                        ok_directions += 1
                        if board[new_row][new_col] == "O":
                            p = (new_row, new_col)
                            checked.add(p)
                            if p not in already_in_q:
                                already_in_q.add(p)
                                q.append(p)
                    else:
                        # edge -> not surrounded -> no flipping
                        should_flip = False
                if ok_directions == 4:
                    to_flip.add((row, col))

            if should_flip:
                for row, col in to_flip:
                    board[row][col] = "X"

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "O" and (r, c) not in checked:
                    bfs(r, c)
