"""
LeetCode: https://leetcode.com/problems/last-day-where-you-can-still-cross/
"""
from collections import deque
from typing import List, Deque, Tuple, Set
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(2, self.latestDayToCross(2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]))

    def test_example_2(self):
        self.assertEqual(1, self.latestDayToCross(2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]]))

    def test_example_3(self):
        self.assertEqual(
            3,
            self.latestDayToCross(3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]])
        )

    def test_case_4(self):
        self.assertEqual(
            3,
            self.latestDayToCross(
                6,
                2,
                [
                    [4, 2], [6, 2], [2, 1], [4, 1], [6, 1], [3, 1],
                    [2, 2], [3, 2], [1, 1], [5, 1], [5, 2], [1, 2]
                ]
            )
        )

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def check(day: int) -> bool:
            q: Deque[Tuple[int, int]] = deque()
            visited: Set[Tuple[int, int]] = set()

            water = set([tuple(cell) for cell in cells[:day]])  # ⚠️ but days are counting from 0 ... 🙈
            # start with top row
            for c in range(1, col + 1):
                possible_starting_point = (1, c)
                if possible_starting_point not in water:
                    q.append(possible_starting_point)  # ⚠️ 1-based matrix
                    visited.add(possible_starting_point)

            visited: Set[Tuple[int, int]]
            while q:
                r, c = q.popleft()
                cell = (r, c)

                if (
                    # step in water
                    cell in water
                    # step out of bounds
                    or min(r, c) < 1
                    or r > row
                    or c > col
                ):
                    continue

                if r == row:
                    return True

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_row, new_col = r + dr, c + dc
                    next_step = (new_row, new_col)
                    if next_step not in visited and next_step not in water:
                        q.append(next_step)
                        visited.add(next_step)

            return False

        left, right = 0, len(cells) - 1
        result = 0
        while left <= right:
            # pick a day
            mid = left + (right - left) // 2

            # check the day
            if check(mid):
                # if there is a path
                result = mid
                left = mid + 1
            else:
                # no path, no reason to check later days
                right = mid - 1

        return result
