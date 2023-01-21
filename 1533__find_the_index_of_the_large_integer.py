"""
We have an integer array arr, where all the integers in arr are equal except for one integer which is larger than the
rest of the integers. You will not be given direct access to the array, instead, you will have an API ArrayReader
which have the following functions:

int compareSub(int l, int r, int x, int y): where 0 <= l, r, x, y < ArrayReader.length(), l <= r and x <= y. The
function compares the sum of sub-array arr[l..r] with the sum of the sub-array arr[x..y] and returns:
1 if arr[l]+arr[l+1]+...+arr[r] > arr[x]+arr[x+1]+...+arr[y].
0 if arr[l]+arr[l+1]+...+arr[r] == arr[x]+arr[x+1]+...+arr[y].
-1 if arr[l]+arr[l+1]+...+arr[r] < arr[x]+arr[x+1]+...+arr[y].
int length(): Returns the size of the array.
You are allowed to call compareSub() 20 times at most. You can assume both functions work in O(1) time.

Return the index of the array arr which has the largest integer.

## Example 1:

Input:
    arr = [7,7,7,7,10,7,7,7]
Output:
    4
Explanation:
    The following calls to the API
        reader.compareSub(0, 0, 1, 1)
            // ^^^ returns 0 this is a query comparing the sub-array (0, 0) with the sub array (1, 1),
            // (i.e. compares arr[0] with arr[1]).
            // Thus we know that arr[0] and arr[1] doesn't contain the largest element.
        reader.compareSub(2, 2, 3, 3) // returns 0, we can exclude arr[2] and arr[3].
        reader.compareSub(4, 4, 5, 5) // returns 1, thus for sure arr[4] is the largest element in the array.
    Notice that we made only 3 calls, so the answer is valid.

## Example 2:

Input: nums = [6,6,12]
Output: 2

## Constraints:

* 2 <= arr.length <= 5 * 10^5
* 1 <= arr[i] <= 100
* All elements of arr are equal except for one element which is larger than all other elements.

## Follow up:

* What if there are two numbers in arr that are bigger than all other numbers?
* What if there is one number that is bigger than other numbers and one number that is smaller than other numbers?
"""
from typing import List
from unittest import TestCase


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class ArrayReader:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def length(self) -> int:
        return len(self.nums)

    def compareSub(self, l1, r1, l2, r2):
        left_sum = sum(self.nums[l1:r1 + 1])
        right_sum = sum(self.nums[l2:r2 + 1])

        if left_sum > right_sum:
            return 1
        elif left_sum < right_sum:
            return -1
        else:
            return 0


class TestSolution(TestCase):
    def test_example_1(self):
        reader = ArrayReader([7, 7, 7, 7, 10, 7, 7, 7])
        solution = Solution()

        self.assertEqual(4, solution.getIndex(reader))

    def test_example_2(self):
        reader = ArrayReader([6, 6, 12])
        solution = Solution()

        self.assertEqual(2, solution.getIndex(reader))

    def test_tricky(self):
        reader = ArrayReader(
            [46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 57, 46, 46, 46, 46])
        solution = Solution()

        self.assertEqual(reader.nums.index(57), solution.getIndex(reader))


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        l, r = 0, reader.length() - 1
        while l <= r:
            if l == r:
                return l
            mid = l + (r - l) // 2
            l1, r1 = l, mid
            l2, r2 = mid + 1, r
            length = r - l + 1
            if length % 2 == 0:
                # even parts
                cmp_result = reader.compareSub(l1, r1, l2, r2)
            else:
                # uneven parts - make it even :troll:
                cmp_result = reader.compareSub(l1, r1, l2 - 1, r2)

            if cmp_result == -1:
                l = l2
            else:
                r = r1
        return l
