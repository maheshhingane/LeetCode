"""
https://leetcode.com/problems/contains-duplicate-iii/description/
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for start in range(0, len(nums)):
            sublist = nums[start:start+k+1]
            for i in range(len(sublist)):
                for j in range(i+1, len(sublist)):
                    if abs(sublist[i] - sublist[j]) <= t:
                        return True
        return False
