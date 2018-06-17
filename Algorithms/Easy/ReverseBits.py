"""
https://leetcode.com/problems/reverse-bits/description/
"""


class Solution:
    # @param n, an integer
    # @return an integer

    def toBinary(self, n):
        if n < 2:
            return str(n % 2)

        return (self.toBinary(n // 2) + str(n % 2))

    def toDecimal(self, n):
        i = 0
        return_val = 0

        while len(n) > 0:
            mod = int(n[-1])
            return_val += (mod * (2 ** i))
            i += 1
            n = n[:-1]

        return return_val

    def reverseBits(self, n):
        binary = self.toBinary(n).rjust(32, "0")
        return self.toDecimal(binary[::-1])
