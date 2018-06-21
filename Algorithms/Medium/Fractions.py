"""
https://leetcode.com/problems/fraction-to-recurring-decimal/description/
"""


class Solution:
    def fraction(self, numerator, denominator):
        if numerator == 0:
            return 0

        sign = 1
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            sign = -1

        numerator = abs(numerator)
        denominator = abs(denominator)

        answer = ""
        divisions = {}
        while numerator != 0:
            if numerator in divisions:
                # if answer.endswith(str(divisions[numerator])):
                #     answer = answer.replace(str(divisions[numerator]), "")
                answer += "(" + str(divisions[numerator]) + ")"
                break
            elif numerator < denominator:
                if "." not in answer:
                    if not answer:
                        answer = "0."
                    else:
                        answer += "."
                numerator *= 10
            else:
                div = numerator // denominator
                mod = numerator % denominator
                answer += str(div)
                divisions[numerator] = div
                numerator = mod
            # print()
            # print("divisions")
            # print(divisions)
            # print("answer", answer)
            # print("numerator", numerator)

        if sign == 1:
            return answer
        else:
            return "-" + answer


# print(Solution().fraction(1, 2))
# print(Solution().fraction(13, 2))
# print(Solution().fraction(1, 9))
# print(Solution().fraction(1, 3))
# print(Solution().fraction(200, 6))
# print(Solution().fraction(17, 6))
# print(Solution().fraction(2, 3))