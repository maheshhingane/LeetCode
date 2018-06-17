"""
https://leetcode.com/problems/first-bad-version/description/
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def isBadVersionBetween(self, low, high):
        if high < low:
            return False
        if high == low:
            return isBadVersion(high)
        if isBadVersion(low) != isBadVersion(high):
            return True
        return False

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low_index = 1
        high_index = n
        while low_index <= high_index:
            if low_index == high_index:
                if isBadVersion(low_index):
                    return low_index
            else:
                mid_index = (low_index + high_index) // 2
                if self.isBadVersionBetween(low_index, mid_index):
                    high_index = mid_index
                elif self.isBadVersionBetween(mid_index + 1, high_index):
                    low_index = (mid_index + 1)
