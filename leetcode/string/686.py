class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        q = (m + n - 1) // n
        for i in range(2):
            if b in a * (q + i):
                return q + i
        return -1
