"""
https://leetcode.com/problems/valid-palindrome/description/
"""


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        z = len(s) - 1
        while a < z:
            if not s[a].isalnum():
                a += 1
                continue
            if not s[z].isalnum():
                z -= 1
                continue
            if s[a].lower() != s[z].lower():
                return False

            a += 1
            z -= 1

        return True
