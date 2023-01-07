def isBadVersion(ver: int) -> bool:
    return True

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        first_bad = -1
        while left <= right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                first_bad = mid
                right = mid - 1
            else:
                left = mid + 1

        return first_bad
