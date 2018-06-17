"""
https://leetcode.com/problems/third-maximum-number/description/
"""


class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_max = None
        second_max = None
        third_max = None

        for num in set(nums):
            if first_max is None or (num > first_max):
                third_max = second_max
                second_max = first_max
                first_max = num
            elif second_max is None or (first_max > num > second_max):
                third_max = second_max
                second_max = num
            elif third_max is None or (second_max > num > third_max):
                third_max = num

        return third_max if third_max is not None else first_max
