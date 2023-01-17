"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique
element appears at most twice. The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed
in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the
first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1)
extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.


Example 1:

Input:
    nums = [1,1,1,2,2,3]
Output:
    5
    nums = [1,1,2,2,3,_]
Explanation:
    Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input:
    nums = [0,0,1,1,1,1,2,3,3]
Output:
    7
    nums = [0,0,1,1,2,3,3,_,_]
Explanation:
    Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

* 1 <= nums.length <= 3 * 10^4
* -10^4 <= nums[i] <= 10^4
* nums is sorted in non-decreasing order.
"""
import math
from typing import List
from unittest import TestCase


class Solution(TestCase):
    def test(self):
        options = [
            ([1, 1, 2, 2, 3], [1, 1, 1, 2, 2, 3]),
            ([1,1], [1,1]),
        ]

        for expected, nums in options:
            with self.subTest():
                expected_size = len(expected)
                nums_copy = nums.copy()

                self.assertEqual(expected_size, self.removeDuplicates(nums))
                self.assertEqual(expected, nums[:expected_size])

                self.assertEqual(expected_size, self.removeDuplicateClean(nums_copy))
                self.assertEqual(expected, nums_copy[:expected_size])

    def removeDuplicateClean(self, nums: List[int]) -> int:
        length = 0
        for n in nums:
            if length < 2 or nums[length - 2] != n:
                nums[length] = n
                length += 1

        return length

    def removeDuplicates(self, nums: List[int]) -> int:
        snowball_size = 0
        prev = math.inf
        for i, n in enumerate(nums):
            if snowball_size > 0:
                if n != prev:
                    # new number, move left
                    prev = n
                    nums[i - snowball_size], nums[i] = nums[i], nums[i - snowball_size]
                else:
                    # repeating number
                    if nums[i - snowball_size - 2] == n:
                        # that's 3rd occurance
                        # just grow snowball, it will be skipped later
                        snowball_size += 1
                    else:
                        # second occurance
                        # move left
                        nums[i - snowball_size], nums[i] = nums[i], nums[i - snowball_size]
            else:
                # if current number is differnt, just proceed
                if prev != n:
                    prev = n
                else:
                    # if it's the same as prev, check if it's second or 2+
                    if i - 2 >= 0 and nums[i - 2] == n:
                        # that's the third
                        # strt snowballing
                        snowball_size += 1
                    else:
                        # second, just proceed
                        pass

        return len(nums) - snowball_size
