import unittest
from collections import deque
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

        self.assertEqual(expected, self.floodFill(image, 1, 1, 2))

    def test_example_2(self):
        image = [[0, 0, 0], [0, 0, 0]]
        expected = [[0, 0, 0], [0, 0, 0]]

        self.assertEqual(expected, self.floodFill(image, 0, 0, 0))

    def test_whole_image(self):
        image = [[0] * 100] * 100
        expected = [[1] * 100] * 100

        self.assertEqual(expected, self.floodFill(image, 50, 50, 1))

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        new_image = image.copy()
        visited = set()
        q = deque([(sr, sc)])
        target_color = image[sr][sc]
        while q:
            r, c = q.popleft()
            if (r, c) in visited or new_image[r][c] != target_color:
                continue

            visited.add((r, c))
            new_image[r][c] = color

            top, bottom, left, right = (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)

            if top not in visited and top[0] >= 0:
                q.append(top)

            if bottom not in visited and bottom[0] < len(new_image):
                q.append(bottom)

            if left not in visited and left[1] >= 0:
                q.append(left)

            if right not in visited and right[1] < len(new_image[r]):
                q.append(right)

        return new_image
