class Solution:
    def numSub(self, s: str) -> int:
        # with n 1's - n + n - 1 + ... 2 + 1 = n * (n + 1) // 2
        i = res = 0
        MOD = 10**9 + 7
        n = len(s)
        while i < n:
            if s[i] == "0":
                i += 1
                continue

            j = i
            while j < n and s[i] == s[j]:
                j += 1

            temp = j - i
            res += temp * (temp + 1) // 2
            res %= MOD
            i = j

        return res
