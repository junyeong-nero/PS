class Solution:
    def countAndSay(self, n: int) -> str:

        def func(s):
            res = ""
            target = ""
            count = 0
            for c in s:
                if c == target:
                    count += 1
                else:
                    if count > 0:
                        res += str(count) + target
                    target = c
                    count = 1
            if count > 0:
                res += str(count) + target
            return res

        res = "1"
        for _ in range(n - 1):
            res = func(res)
            # print(res)

        return res
