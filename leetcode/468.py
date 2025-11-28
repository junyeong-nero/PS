class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        def is_ipv4(ip: str) -> bool:
            parts = ip.split(".")
            if len(parts) != 4:
                return False

            for part in parts:
                if not part or (part[0] == "0" and len(part) > 1):
                    return False
                if not part.isdigit():
                    return False
                if int(part) > 255:
                    return False
            return True

        def is_ipv6(ip: str) -> bool:
            parts = ip.split(":")
            if len(parts) != 8:
                return False

            hex_digits = set("0123456789abcdefABCDEF")
            for part in parts:
                if not (1 <= len(part) <= 4):
                    return False
                if not all(c in hex_digits for c in part):
                    return False
            return True

        if is_ipv4(queryIP):
            return "IPv4"
        if is_ipv6(queryIP):
            return "IPv6"
        return "Neither"
