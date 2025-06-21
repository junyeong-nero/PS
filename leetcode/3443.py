class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        res = 0
        for diag in [{"N", "E"}, {"N", "W"}, {"S", "E"}, {"S", "W"}]:
            kk, dist = k, 0
            for ch in s:
                if ch in diag or kk:
                    dist += 1
                    kk -= ch not in diag
                else:
                    dist -= 1
                res = max(res, dist)
        return res