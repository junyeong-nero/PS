class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:

        # s = s[::-1]
        n = len(s)
        digit_limit = math.floor(log(k, 2)) + 1
        # print(digit_limit)

        count = 0
        res = 0

        def convert(s):
            num = 0
            for c in s:
                num = num * 2 + (0 if c == "0" else 1)
            return num

        for i, c in enumerate(s):
            if c == "0":
                count += 1
            elif c == "1":
                temp = s[i : i + digit_limit]
                if convert(temp) <= k:
                    res = max(res, count + len(temp))

        res = max(res, count)
        return res
