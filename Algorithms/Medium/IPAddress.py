"""
https://leetcode.com/problems/validate-ip-address/description/
"""


class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if "." in IP:
            allowed_chars = "0123456789"
            parts = IP.split(".")
            if len(parts) != 4:
                return "Neither"
            for part in parts:
                if not part or [c for c in part if c not in allowed_chars] or (
                        part.startswith("0") and len(part) != 1) or int(part) > 255:
                    return "Neither"
            return "IPv4"
        elif ":" in IP:
            allowed_chars = "0123456789abcdefABCDEF"
            parts = IP.split(":")
            if len(parts) != 8:
                return "Neither"
            for part in parts:
                if not part or len(part) > 4 or [c for c in part if c not in allowed_chars]:
                    return "Neither"
            return "IPv6"

        return "Neither"
