"""
LeetCode: https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.

## Example 1

Input:
    board = [
        [ "A", "B", "C", "E" ],
        [ "S", "F", "C", "S" ],
        [ "A", "D", "E", "E" ],
    ]
    word = "ABCCED"
Output: true

## Example 2

Input:
    board = [
        [ "A", "B", "C", "E" ],
        [ "S", "F", "C", "S" ],
        [ "A", "D", "E", "E" ],
    ]
    word = "SEE"
Output: true

## Example 3

Input:
    board = [
        [ "A", "B", "C", "E" ],
        [ "S", "F", "C", "S" ],
        [ "A", "D", "E", "E" ],
    ]
    word = "ABCB"
Output: false

## Constraints

* m == board.length
* n = board[i].length
* 1 <= m, n <= 6
* 1 <= word.length <= 15
* board and word consists of only lowercase and uppercase English letters.

## Follow up

Could you use search pruning to make your solution faster with a larger board?
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"], ]
        word = "ABCCED"

        self.assertTrue(self.exist(board, word))

    def test_example_2(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"], ]
        word = "SEE"

        self.assertTrue(self.exist(board, word))

    def test_example_3(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"], ]
        word = "ABCB"

        self.assertFalse(self.exist(board, word))

    def test_case_70(self):
        board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
        word = "ABCESEEEFS"

        self.assertTrue(self.exist(board, word))

    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "":
            return True

        def dfs(r: int, c: int, ptr: 0) -> bool:
            if (
                ptr >= len(word)
                or r < 0 or r >= len(board)
                or c < 0 or c >= len(board[r])
                or board[r][c] != word[ptr]
                or (r, c) in visited
            ):
                return False

            visited.add((r, c))

            if ptr == len(word) - 1:
                return True
            res = any(dfs(nr, nc, ptr + 1) for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)])
            if res:
                return True

            visited.remove((r, c))
            return False

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    visited = set()
                    if dfs(row, col, 0):
                        return True

        return False
