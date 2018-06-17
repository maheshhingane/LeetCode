"""
https://leetcode.com/problems/count-primes/description/
"""


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes_list = []
        for i in range(2, n):
            is_divisible = False
            for prime in primes_list:
                if i % prime == 0:
                    is_divisible = True
                    break
            if is_divisible:
                continue
            primes_list.append(i)

        return len(primes_list)
