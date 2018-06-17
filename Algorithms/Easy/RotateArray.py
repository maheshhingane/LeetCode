"""
https://leetcode.com/problems/rotate-array/description/
"""


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            last_digit = nums[-1]
            for i in range(len(nums)-1, 0, -1):
                nums[i] = nums[i-1]
            nums[0] = last_digit
