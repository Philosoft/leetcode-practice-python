"""
LeetCode: https://leetcode.com/problems/shortest-path-to-get-all-keys/description/
"""
from collections import deque
from typing import List, Set, Tuple, Deque
from unittest import TestCase


class Solution(TestCase):
    def test_example_1(self):
        self.assertEqual(8, self.shortestPathAllKeys(["@.a..", "###.#", "b.A.B"]))

    def test_example_2(self):
        self.assertEqual(6, self.shortestPathAllKeys(["@..aA", "..B#.", "....b"]))

    def test_example_3(self):
        self.assertEqual(-1, self.shortestPathAllKeys(["@Aa"]))

    def tst_case_7(self):
        self.assertEqual(-1, self.shortestPathAllKeys(["@abcdeABCDEFf"]))

    def test_case_26(self):
        self.assertEqual(35, self.shortestPathAllKeys(
            [
                ".#......###..#.",
                ".###C..#...b...",
                "..#..#.........",
                ".........#.....",
                ".....@#.#......",
                "#.##...#..##...",
                "..d#...a...#...",
                "..###..........",
                "........#....#.",
                "..#.#..#...c#.#",
                "D#..........#.#",
                "............#A.",
                "..#..##...#....",
                "#...#..#..B....",
                ".....##.....#.."
            ]))

    def test_case_28(self):
        self.assertEqual(
            42,
            self.shortestPathAllKeys([
                "..Ff..#..e.#...",
                ".....#.##...#..",
                "....#.#...#....",
                "##.......##...#",
                "...@#.##....#..",
                "#........b.....",
                "..#...#.....##.",
                ".#....#E...#...",
                "......A.#D.#...",
                "...#...#..#....",
                "...a.#B#.......",
                ".......c.....#.",
                "....#...C#...#.",
                "##.#.....d..#..",
                ".#..#......#..."
             ])
        )

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        all_keys: Set[str] = set()
        all_doors: Set[str] = set()
        q: Deque[Tuple[int, int, int]] = deque()
        total_number_of_keys: int = 0

        real_grid: List[List[str]] = [list(row) for row in grid]
        for row in range(len(real_grid)):
            for col in range(len(real_grid[row])):
                cell = real_grid[row][col]

                if cell == '@':
                    q.append((row, col, 0))
                elif cell.islower():
                    total_number_of_keys |= 1 << (ord(cell) - ord('a'))
                    all_keys.add(cell)
                elif cell.isupper():
                    all_doors.add(cell)

        visited: Set[Tuple[int, int, int]] = set()
        steps: int = 0

        while q:
            for _ in range(len(q)):
                row, col, keys = q.popleft()

                # is it a key?
                if real_grid[row][col] in all_keys:
                    # pick it up
                    keys |= 1 << (ord(real_grid[row][col]) - ord('a'))

                    # the moment we have all keys for the first time
                    # is the moment we triumph
                    if keys == total_number_of_keys:
                        return steps

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_row, new_col = row + dr, col + dc
                    if (
                        # out of bounds
                        min(new_row, new_col) < 0 or new_row >= len(real_grid) or new_col >= len(real_grid[new_row])
                        # wall
                        or real_grid[new_row][new_col] == '#'
                        # already visited
                        or (new_row, new_col, keys) in visited
                    ):
                        continue

                    # is a door and do not have key right now
                    if real_grid[new_row][new_col] in all_doors:
                        mask = 1 << (ord(real_grid[new_row][new_col].lower()) - ord('a'))
                        if keys & mask != mask:
                            continue

                    # that's an ok cell
                    q.append((new_row, new_col, keys))
                    visited.add((new_row, new_col, keys))

            steps += 1

        return -1
