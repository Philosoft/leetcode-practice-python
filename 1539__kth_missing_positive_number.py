import unittest
from typing import List


class Solution(unittest.TestCase):
    def test_example_1(self):
        """
        Explanation: The missing positive integers are [1, 5, 6, 8, 9, 10, 12, 13, ...].
        The 5 th missing positive integer is 9.
        """
        arr = [2, 3, 4, 7, 11]
        k = 5
        expected = 9

        self.assertEqual(expected, self.findKthPositive(arr, k))

    def test_example_2(self):
        """
        Explanation: The missing positive integers are[5, 6, 7, ...].
        The 2 nd missing positive integer is 6.
        """
        arr = [1, 2, 3, 4]
        k = 2
        expected = 6

        self.assertEqual(expected, self.findKthPositive(arr, k))

    def test_kek(self):
        self.assertEqual(10, self.findKthPositive([1], 9))

    def test_single_array_missing_left(self):
        self.assertEqual(1, self.findKthPositive([2], 1))

    def test_single_array_missing_far_left(self):
        self.assertEqual(1, self.findKthPositive([200], 1))

    def test_single_array_missing_right(self):
        self.assertEqual(3, self.findKthPositive([2], 2))

    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) # len(arr) is not a mistake
        while left < right:
            mid = left + (right - left) // 2

            # constrains help a lot
            # * 1 <= arr[i] <= 1000 <- starts from 1
            # * arr[i] < arr[i + 1] <- no repeating numbers
            # since array is sorted it's not possible to have arr[i] < i + 1 (+ 1, since there is no 0)
            # it's either eq (arr[i] == i + 1, which means nothing is skipped up to i-th position)
            # or >, means something was missed
            missed_up_to_mid = arr[mid] - mid - 1
            if missed_up_to_mid < k:
                # missing item is on the right
                left = mid + 1
            else:
                right = mid

        # when the search is over. r will be exactly  t - k, where t is target of a search
        '''
            (1) [2 3 4 (5) (6) 7** (8) (9) (10) 11]
                                        ^
            (x) - missing number
            x** - right pointer
            ^   - target

            r = 4 (arr[4] = 7)
            k = 5
            t = 9
            
            t = r + k
            
            another example
            (1 ... 199) [200]
             ^
             
             r = 0
             k = 1
             t = 1
             answer = r + k = 0 + 1 = 1 == t 
             
             another one
             (1 ... 199) [200]
             k = 200
             r = 1
             t = 201
             answer = r + k = 1 + 200 = 201 == t
        '''
        return right + k

    def findKthPositiveBrute(self, arr: List[int], k: int) -> int:
        searching_for = 1
        ptr = 0
        while ptr < len(arr):
            if arr[ptr] != searching_for:
                while searching_for < arr[ptr]:
                    k -= 1
                    if k == 0:
                        return searching_for
                    searching_for += 1

            ptr += 1
            searching_for += 1

        return searching_for + k - 1
