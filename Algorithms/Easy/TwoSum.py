"""
https://leetcode.com/problems/two-sum/description/
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for n1 in range(len(nums)):
            for n2 in range(n1 + 1, len(nums)):
                if nums[n1] + nums[n2] == target:
                    return [n1, n2]
