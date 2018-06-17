"""
https://leetcode.com/problems/non-decreasing-array/description/
"""


class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        violation_found_at = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if violation_found_at is not None:
                    return False
                violation_found_at = i

        return (violation_found_at is None) or (violation_found_at == 0) or (violation_found_at == len(nums) - 2) or (
                    nums[violation_found_at - 1] <= nums[violation_found_at + 1]) or (
                           nums[violation_found_at] <= nums[violation_found_at + 2])
