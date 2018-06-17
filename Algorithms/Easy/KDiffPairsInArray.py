"""
https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
"""


class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sorted_nums = sorted(nums)
        seen_nums = []

        for i in range(len(sorted_nums)):
            if sorted_nums[i] in seen_nums:
                continue
            else:
                seen_nums.append(sorted_nums[i])
            if (sorted_nums[i] + k) in sorted_nums[i + 1:]:
                count += 1

        return count
