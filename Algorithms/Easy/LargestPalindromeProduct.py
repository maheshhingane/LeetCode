"""
https://leetcode.com/problems/largest-palindrome-product/description/
"""


class Solution:
    def isPalindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        largest_n_digit_number = int("9" * n)
        smallest_n_digit_number = int("1" + ("0" * (n - 1)))

        max = 0

        for i in reversed(range(smallest_n_digit_number, largest_n_digit_number + 1)):
            for j in reversed(range(smallest_n_digit_number, i + 1)):
                product = i * j
                if product > max:
                    if self.isPalindrome(str(product)):
                        max = product
                else:
                    break

        return max % 1337
