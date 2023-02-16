from dataclasses import dataclass
from typing import List, Tuple, Set
from unittest import TestCase


@dataclass
class PointInfo:
    pacific: bool = False
    atlantic: bool = False


class Solution(TestCase):
    def test_example_1(self):
        heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        expected.sort()
        answer = self.pacificAtlantic(heights)
        answer.sort()

        self.assertEqual(expected, answer)

    def test_leetcode_73(self):
        heights = [[1, 1], [1, 1], [1, 1]]
        expected = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
        expected.sort()
        answer = self.pacificAtlantic(heights)
        answer.sort()

        self.assertEqual(expected, answer)

    def test_big(self):
        heights = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 13],
                   [43, 80, 81, 82, 83, 84, 85, 86, 87, 88, 55, 14],
                   [42, 79, 108, 109, 110, 111, 112, 113, 114, 89, 56, 15],
                   [41, 78, 107, 128, 129, 130, 131, 132, 115, 90, 57, 16],
                   [40, 77, 106, 127, 140, 141, 142, 133, 116, 91, 58, 17],
                   [39, 76, 105, 126, 139, 144, 143, 134, 117, 92, 59, 18],
                   [38, 75, 104, 125, 138, 137, 136, 135, 118, 93, 60, 19],
                   [37, 74, 103, 124, 123, 122, 121, 120, 119, 94, 61, 20],
                   [36, 73, 102, 101, 100, 99, 98, 97, 96, 95, 62, 21],
                   [35, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 22], [34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23]]
        expected = [[0, 11], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10],
                    [1, 11], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10],
                    [2, 11], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10],
                    [3, 11], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10],
                    [4, 11], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10],
                    [5, 11], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [6, 10],
                    [6, 11], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [7, 9], [7, 10],
                    [7, 11], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9], [8, 10],
                    [8, 11], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9], [9, 10],
                    [9, 11], [10, 0], [10, 1], [10, 2], [10, 3], [10, 4], [10, 5], [10, 6], [10, 7], [10, 8], [10, 9],
                    [10, 10], [10, 11], [11, 0], [11, 1], [11, 2], [11, 3], [11, 4], [11, 5], [11, 6], [11, 7], [11, 8],
                    [11, 9], [11, 10], [11, 11]]
        expected.sort()
        answer = self.pacificAtlantic(heights)
        answer.sort()

        self.assertEqual(expected, answer)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        can_reach_pacific: Set[Tuple[int, int]] = set()
        can_reach_atlantic: Set[Tuple[int, int]] = set()

        ROWS = len(heights)
        COLS = len(heights[0])

        path = set()

        def dfs(row: int, col: int, type: str) -> None:
            p = (row, col)
            if type == 'pacific':
                can_reach_pacific.add(p)
            else:
                can_reach_atlantic.add(p)

            path.add(p)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                new_p = (new_row, new_col)

                if (
                    new_row < 0 or new_row >= ROWS
                    or new_col < 0 or new_col >= COLS
                    or heights[row][col] > heights[new_row][new_col]
                    or new_p in path
                    or new_p in (can_reach_pacific if type == 'pacific' else can_reach_atlantic)
                ):
                    continue

                dfs(new_row, new_col, type)

            path.remove(p)

        for col in range(COLS):
            dfs(0, col, 'pacific')
            dfs(ROWS - 1, col, 'atlantic')

        for row in range(ROWS):
            dfs(row, 0, 'pacific')
            dfs(row, COLS - 1, 'atlantic')

        return list(map(list, can_reach_pacific & can_reach_atlantic))
