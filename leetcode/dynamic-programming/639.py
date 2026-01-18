class Solution:
    def numDecodings(self, s: str) -> int:

        # solution with DP
        # dp[i]: numbers of ways to decode s[:i]
        # dp[i] = + dp[i - 2] * number of ways to decode(valid s[i - 2:i])
        #         + dp[i - 1] * number of ways to decode(valid s[i - 1:i])

        def ways(arr):
            n = len(arr)
            if n == 1:
                if arr[0] == "*":
                    # (1 ~ 9)
                    return 9
                return 0 if arr[0] == "0" else 1

            if arr == "**":
                # 11, 12 ... 19 : 9
                # 21, 22 ... 26 : 6
                return 15

            if arr[0] == "*":
                # *1, *2, ... *6 => * can be 1 or 2
                # *7, *8, *9     => * should be only 1.
                return 2 if arr[1] <= "6" else 1

            if arr[1] == "*":
                # 0* => impossible
                # 1* => 1 ~ 9
                # 2* => 1 ~ 6
                if arr[0] == "0":
                    return 0
                if arr[0] == "1":
                    return 9
                if arr[0] == "2":
                    return 6
                else:
                    return 0

            # 06, 07 or somethings.
            if arr[0] == "0":
                return 0

            # validation check
            if 1 <= int(arr) <= 26:
                return 1

            # bigger than 26. such as 35.
            return 0

        n = len(s)
        MOD = 10**9 + 7

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            a, b = 0, 0
            if i - 2 >= 0:
                a = dp[i - 2] * ways(s[i - 2 : i])
            if i - 1 >= 0:
                b = dp[i - 1] * ways(s[i - 1 : i])

            dp[i] = (a + b) % MOD

        # print(dp)
        return dp[-1]
