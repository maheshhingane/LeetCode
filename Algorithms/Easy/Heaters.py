"""
https://leetcode.com/problems/heaters/description/
"""
import sys


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses = sorted(houses)
        heaters = sorted(heaters)

        min_radius = -sys.maxsize

        for house in houses:
            heaters_to_left = [heater for heater in heaters if heater <= house]
            left_heater = (house - heaters_to_left[-1]) if heaters_to_left else sys.maxsize
            heaters_to_right = [heater for heater in heaters if heater > house]
            right_heater = (heaters_to_right[0] - house) if heaters_to_right else sys.maxsize

            radius = min(left_heater, right_heater)
            if radius > min_radius:
                min_radius = radius

        return min_radius
