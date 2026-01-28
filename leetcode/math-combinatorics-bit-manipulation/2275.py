class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        def check(i):
            # check i-th bit is 1
            count = 0
            for cand in candidates:
                if cand & (1 << i):
                    count += 1
            return count

        res = 0
        for i in range(32):
            res = max(res, check(i))

        return res
