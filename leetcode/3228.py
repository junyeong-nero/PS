class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        count = res = 0
        i = 0
        while i < n:
            if s[i] == "0":
                i += 1
                continue
            j = i
            while j < n and s[j] == "1":
                j += 1
            if j < n:
                count += j - i
                res += count
            i = j
        return res
