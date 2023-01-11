from heapq import heappop, heappush
from typing import List, Tuple
from unittest import TestCase

"""
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers
are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

* The number of soldiers in row i is less than the number of soldiers in row j.
* Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

 
Example 1:

Input:
    mat = [
        [1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]
    ], 
    k = 3
Output: [2,0,3]

Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 | 2
- Row 1: 4 | 5
- Row 2: 1 | 3
- Row 3: 2 | 5
- Row 4: 5 | 9
The rows ordered from weakest to strongest are [2,0,3,1,4].


Example 2:

Input:
    mat = [
        [1,0,0,0],
        [1,1,1,1],
        [1,0,0,0],
        [1,0,0,0]
    ], 
    k = 2
Output: [0,2]

Explanation: 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].
 
Constraints:

* m == mat.length
* n == mat[i].length
* 2 <= n, m <= 100
* 1 <= k <= m
* matrix[i][j] is either 0 or 1.
"""


class Solution(TestCase):
    def test_example_1(self):
        mat = [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]]

        self.assertEqual([2, 0, 3], self.kWeakestRows(mat, 3))

    def test_example_2(self):
        mat = [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]]

        self.assertEqual([0, 2], self.kWeakestRows(mat, 2))

    def test_same_strength_rows(self):
        mat = [
            [0, 0, 0],
            [1, 1, 1],
            [1, 1, 1],
            [0, 0, 0],
        ]

        self.assertEqual([0, 3], self.kWeakestRows(mat, 2))

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        Brute force
        calculate everything: O(n * m)
        sort result: O(n * log n)
        take k smallest O(k)

        T: O(n * m + n * log n + k) = O(n * m)
        S: O(n) - for additional array

        BS + min heap

        Go row by row and search for the rightmost 1 (w 2 edges for leftmost is 0 and rightmost is 1)
        ^^^ T: O(n * log n), S: O(1)
        Put result of each row in min heap.
        ^^^ T: O(n * log n), S: O(n)
        Pop everything from heap
        ^^^ T: O(k * log n), S: O(n)
        Total: T(n * log n + n * log n + k * log n) = O(n * log n). S: O(n)
        """
        # heap values are (strength, row_idx). where strength is row_idx + number_of_soldiers
        heap: List[Tuple[int, int]] = []
        for row in range(len(mat)):
            # edge case 1. all soldiers
            if mat[row][-1] == 1:
                heappush(heap, (len(mat[row]), row))
                continue

            # edge case 2. all peasants
            if mat[row][0] == 0:
                heappush(heap, (0, row))
                continue

            # general case
            left, right = 0, len(mat[row])
            while left <= right:
                mid = left + (right - left) // 2

                if mat[row][mid] == 1:
                    left = mid + 1
                else:
                    right = mid - 1

            heappush(heap, (right + 1, row))

        answer = []
        while heap and k:
            answer.append(heappop(heap)[1])
            k -= 1

        return answer
