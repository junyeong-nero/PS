class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)

        res = []
        for i in range(0, n, k):
            res.append(s[i : i + k])

        res[-1] = res[-1] + fill * (k - len(res[-1]))
        return res
