"""
LeetCode: https://leetcode.com/problems/where-will-the-ball-fall
"""
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(
            [1, -1, -1, -1, -1],
            self.findBall([
                [1, 1, 1, -1, -1],
                [1, 1, 1, -1, -1],
                [-1, -1, -1, 1, 1],
                [1, 1, 1, 1, -1],
                [-1, -1, -1, -1, -1],
            ])
        )

    def test_example_2(self):
        self.assertEqual([-1], self.findBall([[-1]]))

    def test_example_3(self):
        self.assertEqual([0, 1, 2, 3, 4, -1], self.findBall(
            [[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]))

    def test_one_row(self):
        self.assertEqual([-1, 0, 3, -1], self.findBall([[-1, -1, 1, 1]]))

    def test_two_rows(self):
        self.assertEqual([2, -1, -1, -1, -1], self.findBall([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1]]))

    def test_three_rows(self):
        self.assertEqual([1, -1, -1, -1, -1], self.findBall([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1]]))

    def findBall(self, grid: List[List[int]]) -> List[int]:
        COLS = len(grid[0])
        balls = [x for x in range(len(grid[0]))]

        for row in grid:
            for idx, ball_idx in enumerate(balls):
                if ball_idx == -1:
                    # ball is already stuck somewhere - skip it
                    continue

                if (ball_idx == 0 and row[ball_idx] == -1) or (ball_idx == COLS - 1 and row[ball_idx] == 1):
                    # near the boundary and tube is a dead-end
                    balls[idx] = -1
                    continue

                if (ball_idx + 1 < COLS and row[ball_idx] == 1 and row[ball_idx + 1] == -1) or (ball_idx > 0 and row[ball_idx] == -1 and row[ball_idx - 1] == 1):
                    # v-shape, ball is stuck
                    balls[idx] = -1
                    continue

                # otherwise move the ball accordingly
                balls[idx] = ball_idx + row[ball_idx]

        return balls
