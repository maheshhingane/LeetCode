"""
https://leetcode.com/problems/excel-sheet-column-title/description/
"""


class Solution:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 26:
            return self.alphabet[n-1]
        else:
            mod = (n-1) % 26
            return self.convertToTitle((n-1)//26) + self.alphabet[mod]
