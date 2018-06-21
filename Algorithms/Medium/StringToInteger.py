"""
https://leetcode.com/problems/string-to-integer-atoi/description/
"""


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        if not str:
            return 0

        i = 0
        is_negative = False
        if not str[0].isdigit():
            if str[0] == "-":
                is_negative = True
                i = 1
                if len(str) > 1 and not str[1].isdigit():
                    return 0
            elif str[0] == "+":
                i = 1
                if len(str) > 1 and not str[1].isdigit():
                    return 0
            else:
                return 0

        number = ""
        while i < len(str):
            if str[i].isdigit():
                number += str[i]
            else:
                break
            i += 1

        if not number:
            return 0

        if is_negative:
            number = "-" + number

        number = int(number)

        if number < ((-2) ** 31):
            return (-2) ** 31
        elif number > ((2 ** 31) - 1):
            return (2 ** 31) - 1
        else:
            return number
