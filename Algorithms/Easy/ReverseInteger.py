"""
https://leetcode.com/problems/reverse-integer/description/
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        abs_x = abs(x)
        return_val = 0
        multiple = (10 ** len(str(abs_x))) // 10

        while abs_x > 0:
            return_val += ((abs_x % 10) * multiple)
            abs_x = abs_x // 10
            multiple //= 10

        if x < 0:
            return_val *= -1

        if (-2 ** 31) <= return_val <= ((2 ** 31) - 1):
            return return_val
        else:
            return 0
